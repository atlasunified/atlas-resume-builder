import os
import json
import openai
import requests
import random
import unicodedata
from bs4 import BeautifulSoup
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt, Confirm
import pygame  # for MIDI playback

# Import the structured output class from the external module.
from structured_output import ResumeTailorStructuredOutput

# Check for API key from environment variable, then file.
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    if os.path.exists("openai-api-key.txt"):
        with open("openai-api-key.txt", "r") as f:
            api_key = f.read().strip()
openai.api_key = api_key

console = Console()

RESUMES_DIR = "resumes"
MIDI_DIR = "midi"

def play_midi_background():
    """Initialize pygame mixer and play a random MIDI file from MIDI_DIR."""
    if os.path.exists(MIDI_DIR) and os.path.isdir(MIDI_DIR):
        midi_files = [os.path.join(MIDI_DIR, f) for f in os.listdir(MIDI_DIR) if f.lower().endswith((".mid", ".midi"))]
        if midi_files:
            try:
                pygame.mixer.init()
                selected_midi = random.choice(midi_files)
                pygame.mixer.music.load(selected_midi)
                pygame.mixer.music.play(-1)  # Loop indefinitely
            except Exception as e:
                console.print(f"[red]Error playing MIDI file: {e}[/red]")
        else:
            console.print("[yellow]No MIDI files found in the 'midi' directory.[/yellow]")
    else:
        console.print("[yellow]'midi' directory not found.[/yellow]")

def scrape_job_posting(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract title using Open Graph or <title>
        og_title = soup.find("meta", property="og:title")
        if og_title and og_title.get("content"):
            title = og_title.get("content").strip()
        elif soup.title:
            title = soup.title.string.strip()
        else:
            title = "Job Posting"
        
        # Scrape the whole page text.
        full_text = soup.get_text(separator="\n", strip=True)
        
        # Use the text as-is for both human and AI versions.
        job_posting_data = {
            "url": url,
            "title": title,
            "description": full_text,       # Human-readable version
            "ai_description": full_text       # AI version
        }
        return json.dumps(job_posting_data, indent=4)
    except Exception as e:
        console.print(f"[red]Error scraping job posting from URL: {e}[/red]")
        return f"Job Posting URL: {url} (failed to scrape content)"

def process_job_posting_input(input_text):
    if input_text.startswith("http://") or input_text.startswith("https://"):
        return scrape_job_posting(input_text)
    else:
        return input_text

def clean_job_posting_text(ai_text):
    from openai import OpenAI
    client = OpenAI()
    prompt = f"Clean the following job announcement by stripping out extraneous content and return all the job details. Display the Title, Company, Location(s), and Salary Range First. Then, Outline the Role by combining what is in there with your summary as well, then Key Responsibilities in great detail if they're posted and create them if they arent, then Qualifications in great detail to the letter of the announcement and then your summary of additional skills you believe would be required, then a 'everything else' category that outlines what your AI synposis is of the job itself:':\n\n{ai_text}"
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )
        cleaned_text = completion.choices[0].message.content
        return cleaned_text
    except Exception as e:
        console.print(f"[red]Error cleaning job posting: {e}[/red]")
        return ai_text

def get_job_target():
    console.print("[bold cyan]Job Target Information[/bold cyan]")
    position_title = Prompt.ask("Desired Position Title")
    company = Prompt.ask("Desired Company")
    location = Prompt.ask("Desired Location")
    salary_desired = Prompt.ask("Desired Salary Range")
    return {
        "position_title": position_title,
        "company": company,
        "location": location,
        "salary_desired": salary_desired
    }

def get_personal_info():
    console.print("[bold cyan]Personal Information[/bold cyan]")
    name = Prompt.ask("Full Name")
    email = Prompt.ask("Email")
    phone = Prompt.ask("Phone Number")
    summary = Prompt.ask("Enter your professional summary (optional)", default="")
    return {"name": name, "email": email, "phone": phone, "summary": summary}

def get_work_experience():
    experiences = []
    add_more = True
    while add_more:
        console.print("\n[bold cyan]Work Experience Entry[/bold cyan]")
        job_title = Prompt.ask("Job Title")
        company = Prompt.ask("Company")
        location = Prompt.ask("Location")
        start_date = Prompt.ask("Start Date (e.g., Jan 2020)")
        end_date = Prompt.ask("End Date (e.g., Dec 2020 or Present)")
        responsibilities_input = Prompt.ask("Enter responsibilities (separate each with a semicolon ';')")
        responsibilities = [r.strip() for r in responsibilities_input.split(";") if r.strip()]
        achievements_input = Prompt.ask("Enter achievements (separate each with a semicolon ';')")
        achievements = [a.strip() for a in achievements_input.split(";") if a.strip()]
        programs_input = Prompt.ask("Enter programs managed (separate each with a semicolon ';')", default="")
        programs_managed = [p.strip() for p in programs_input.split(";") if p.strip()]
        technologies_input = Prompt.ask("Enter technologies (separate each with a comma ',')", default="")
        technologies = [t.strip() for t in technologies_input.split(",") if t.strip()]
        experience = {
            "job_title": job_title,
            "company": company,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "responsibilities": responsibilities,
            "achievements": achievements,
            "programs_managed": programs_managed,
            "technologies": technologies,
        }
        experiences.append(experience)
        add_more = Confirm.ask("Would you like to add another job?")
    return experiences

def get_education():
    educations = []
    add_more = True
    while add_more:
        console.print("\n[bold cyan]Education Entry[/bold cyan]")
        institution = Prompt.ask("Institution Name")
        degree = Prompt.ask("Degree / Certification")
        location = Prompt.ask("Location")
        start_date = Prompt.ask("Start Date")
        end_date = Prompt.ask("End Date (or Graduation Year)")
        details = Prompt.ask("Enter details about your education (optional)", default="")
        educations.append({
            "institution": institution,
            "degree": degree,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "details": details
        })
        add_more = Confirm.ask("Would you like to add another education entry?")
    return educations

def get_certifications():
    certs = []
    if Confirm.ask("Do you have any certifications?"):
        add_more = True
        while add_more:
            console.print("[bold cyan]Certification Entry[/bold cyan]")
            name = Prompt.ask("Certification Name")
            specialization = Prompt.ask("Specialization")
            awarded_by = Prompt.ask("Awarded By")
            year = Prompt.ask("Year (or N/A)")
            certs.append({
                "name": name,
                "specialization": specialization,
                "awarded_by": awarded_by,
                "year": year
            })
            add_more = Confirm.ask("Would you like to add another certification?")
    return certs

def get_leadership_skills():
    skills = Prompt.ask("Enter your leadership skills separated by commas (if any)", default="")
    return [s.strip() for s in skills.split(",") if s.strip()]

def get_tools():
    tools = Prompt.ask("Enter the tools you are proficient with, separated by commas (if any)", default="")
    return [t.strip() for t in tools.split(",") if t.strip()]

def get_online_profiles():
    console.print("[bold cyan]Online Profiles[/bold cyan]")
    hugging_face = Prompt.ask("Enter your Hugging Face profile (if any)", default="")
    github = Prompt.ask("Enter your GitHub profile (if any)", default="")
    return {"hugging_face": hugging_face, "github": github}

def create_resume():
    job_target = get_job_target()
    personal_info = get_personal_info()
    work_experience = get_work_experience()
    education = get_education()
    certifications = get_certifications()
    leadership_skills = get_leadership_skills()
    tools = get_tools()
    online_profiles = get_online_profiles()
    
    complete = Confirm.ask("Is this resume complete?")
    status = "complete" if complete else "in progress"
    last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    resume = {
        "job_target": job_target,
        "personal_info": personal_info,
        "work_experience": work_experience,
        "education": education,
        "certifications": certifications,
        "leadership_skills": leadership_skills,
        "tools": tools,
        "online_profiles": online_profiles
    }
    
    return {
        "resume": resume,
        "status": status,
        "last_modified": last_modified
    }

def ensure_resumes_dir():
    if not os.path.exists(RESUMES_DIR):
        os.makedirs(RESUMES_DIR)
        console.print(f"[green]Created '{RESUMES_DIR}' directory.[/green]")

def get_resume_path(resume_name):
    return os.path.join(RESUMES_DIR, resume_name)

def save_resume(resume_data, resume_name):
    ensure_resumes_dir()
    dir_path = get_resume_path(resume_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, "resume.json")
    try:
        with open(file_path, "w") as f:
            json.dump(resume_data, f, indent=4)
        console.print(f"[green]Saved resume to {file_path}[/green]")
    except Exception as e:
        console.print(f"[red]Error saving resume: {e}[/red]")

def list_resumes():
    ensure_resumes_dir()
    resumes_found = {}
    for entry in os.listdir(RESUMES_DIR):
        dir_path = os.path.join(RESUMES_DIR, entry)
        if os.path.isdir(dir_path):
            file_path = os.path.join(dir_path, "resume.json")
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    resumes_found[entry] = data
                except Exception as e:
                    console.print(f"[red]Error loading resume from {file_path}: {e}[/red]")
    return resumes_found

def load_resume(resume_name):
    file_path = os.path.join(get_resume_path(resume_name), "resume.json")
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        console.print(f"[red]Error loading resume {resume_name}: {e}[/red]")
        return None

def clean_unicode(text):
    """Normalize and clean up any weird Unicode characters."""
    return unicodedata.normalize("NFKC", text)

def create_cover_letter(tailored_resume, job_posting_data):
    """
    Generate a cover letter in JSON format using the provided resume and job posting.
    This function sends both inputs to the OpenAI Chat Completion API and instructs the AI
    to output a cover letter (with header, salutation, body, and closing) in JSON format.
    """
    # Ensure job_posting_data is a dictionary (if not, try to parse it)
    if isinstance(job_posting_data, str):
        try:
            job_posting_dict = json.loads(job_posting_data)
        except Exception:
            job_posting_dict = {"description": job_posting_data}
    else:
        job_posting_dict = job_posting_data

    # Convert the resume and job posting to formatted JSON strings for clarity.
    resume_str = json.dumps(tailored_resume, indent=2, ensure_ascii=False)
    job_posting_str = json.dumps(job_posting_dict, indent=2, ensure_ascii=False)

    prompt = (
        "Using the resume and job posting provided below, generate a captivating, award-winning cover letter in JSON format. "
        "This cover letter must break the mold of generic templates by showcasing creativity, passion, and specificity to both the candidate's achievements and the job requirements. "
        "Ensure the response is free from any encoded Unicode escape sequences like \\u2019 and outputs clean, natural text. "
        "The output should be a well-structured JSON object with the following sections:\n\n"
        "1. Header: Include the current date, the candidate's full name, and their contact information (email and phone number).\n"
        "2. Salutation: A personalized greeting addressing the hiring manager directly.\n"
        "3. Body:\n"
        "   a. Introduction: Craft a strong, engaging opening that grabs attention and clearly expresses the candidate’s enthusiasm for the position.\n"
        "   b. Reference to Job Posting: Specifically mention details from the job posting, explaining how the candidate's background and achievements uniquely align with the role.\n"
        "   c. Summary of Relevant Experience: Provide a detailed, dynamic account of the candidate’s accomplishments and skills, highlighting what sets them apart and how they will add value to the organization.\n"
        "   d. Conclusion: Offer a compelling closing statement that reiterates enthusiasm, includes a call to action, and leaves a memorable impression.\n"
        "4. Closing: A professional sign-off with the candidate’s name.\n\n"
        "Output strictly as a JSON object with no markdown formatting or explanations.\n\n"
        f"Resume:\n{resume_str}\n\n"
        f"Job Posting:\n{job_posting_str}"
    )

    try:
        from openai import OpenAI
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )
        cover_letter_output = completion.choices[0].message.content

        # Step 1: Clean Unicode in the raw text (before parsing)
        cover_letter_output = clean_unicode(cover_letter_output)

        # Remove markdown formatting if present
        lines = cover_letter_output.splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        cover_letter_output = "\n".join(lines).strip()

        # Step 2: Try parsing the cleaned text as JSON
        try:
            cover_letter_json = json.loads(cover_letter_output)
        except json.JSONDecodeError:
            console.print("[yellow]Warning: First JSON parse failed. Retrying cleanup...[/yellow]")
            cover_letter_output = clean_unicode(cover_letter_output)
            cover_letter_json = json.loads(cover_letter_output)

        # Step 3: Dump and load JSON with ensure_ascii=False and repeatedly clean until no escape sequences remain.
        cleaned_json_str = json.dumps(cover_letter_json, indent=4, ensure_ascii=False)
        # Loop until there are no Unicode escapes in the dumped string
        while "\\u" in cleaned_json_str:
            cleaned_json_str = clean_unicode(cleaned_json_str)
        cover_letter_json = json.loads(cleaned_json_str)

        return cover_letter_json

    except Exception as e:
        console.print(f"[red]Error generating cover letter: {e}[/red]")
        return None

def main_menu():
    console.print(r"""    ___  ________    ___   _____    __  ___   __________________________           
   /   |/_  __/ /   /   | / ___/   / / / / | / /  _/ ____/  _/ ____/ __ \          
  / /| | / / / /   / /| | \__ \   / / / /  |/ // // /_   / // __/ / / / /          
 / ___ |/ / / /___/ ___ |___/ /  / /_/ / /|  // // __/ _/ // /___/ /_/ /           
/_/ _|_/_/_/_____/_/_ |_/____/  _\____/_/ |_/___/_/_  /___/_____/_____/ __________ 
   / __ \/ ____/ ___// / / /  |/  / ____/  / __ )/ / / /  _/ /   / __ \/ ____/ __ \
  / /_/ / __/  \__ \/ / / / /|_/ / __/    / __  / / / // // /   / / / / __/ / /_/ /
 / _, _/ /___ ___/ / /_/ / /  / / /___   / /_/ / /_/ // // /___/ /_/ / /___/ _, _/ 
/_/ |_/_____//____/\____/_/  /_/_____/  /_____/\____/___/_____/_____/_____/_/ |_|                             
    """, style="bold bright_magenta")

    play_midi_background()
    
    while True:
        console.print("\n[bold green]Main Menu[/bold green]")
        console.print("[bold blue]1.[/bold blue] Create/Edit Baseline Resume")
        console.print("[bold blue]2.[/bold blue] Create a Tailored Resume for a Job Posting")
        console.print("[bold blue]3.[/bold blue] List All Resumes")
        console.print("[bold blue]4.[/bold blue] Load and View a Resume")
        console.print("[bold blue]5.[/bold blue] Create Cover Letter for a Tailored Resume")
        console.print("[bold blue]6.[/bold blue] Quit")
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "6"])
        
        if choice == "1":
            console.print("[bold blue]Creating/Editing Baseline Resume...[/bold blue]")
            new_resume = create_resume()
            save_resume(new_resume, "baseline")
            console.print("[green]Baseline resume created/updated![/green]")
        
        elif choice == "2":
            tailored_name = Prompt.ask("Enter a name for this tailored resume (no spaces)")
            resumes_found = list_resumes()
            if not resumes_found:
                console.print("[red]No resumes available. Please create a baseline resume first.[/red]")
                continue
            console.print("[bold yellow]Available Baseline Resumes:[/bold yellow]")
            baseline_names = list(resumes_found.keys())
            for idx, name in enumerate(baseline_names, start=1):
                console.print(f"{idx}. {name}")
            baseline_choice = Prompt.ask("Enter the number or name of the resume to use as baseline")
            if baseline_choice.isdigit():
                idx = int(baseline_choice) - 1
                if 0 <= idx < len(baseline_names):
                    chosen_baseline_name = baseline_names[idx]
                else:
                    console.print("[red]Invalid selection.[/red]")
                    continue
            else:
                if baseline_choice in resumes_found:
                    chosen_baseline_name = baseline_choice
                else:
                    console.print("[red]Invalid selection.[/red]")
                    continue
            baseline_resume = load_resume(chosen_baseline_name)
            if not baseline_resume:
                console.print("[red]Failed to load the chosen baseline resume.[/red]")
                continue
            
            posting_input = Prompt.ask("Enter the job posting details or URL (paste the text)")
            job_posting = process_job_posting_input(posting_input)
            
            console.print("[bold cyan]Scraped Job Posting Data (Display Version):[/bold cyan]")
            try:
                job_posting_json = json.loads(job_posting)
                ai_job_posting = job_posting_json.get("ai_description", job_posting)
            except Exception:
                console.print(job_posting)
                ai_job_posting = job_posting
            
            # Automatically clean the AI version of the job posting.
            cleaned_job_posting = clean_job_posting_text(ai_job_posting)
            console.print("[bold cyan]Cleaned Job Posting for AI:[/bold cyan]")
            console.print(cleaned_job_posting)
            
            # Create a directory for the tailored resume.
            dir_path = get_resume_path(tailored_name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                console.print(f"[green]Created directory '{dir_path}' for the tailored resume.[/green]")
            
            # Save the cleaned AI job posting data.
            ai_job_posting_file = os.path.join(dir_path, "job_posting_ai.txt")
            try:
                with open(ai_job_posting_file, "w") as f:
                    f.write(cleaned_job_posting)
                console.print(f"[green]Saved cleaned AI job posting data to '{ai_job_posting_file}'.[/green]")
            except Exception as e:
                console.print(f"[red]Error saving AI job posting data: {e}[/red]")
            
            # Save the baseline resume.
            baseline_file = os.path.join(dir_path, "baseline_resume.json")
            try:
                with open(baseline_file, "w") as f:
                    json.dump(baseline_resume, f, indent=4)
                console.print(f"[green]Saved baseline resume to '{baseline_file}'.[/green]")
            except Exception as e:
                console.print(f"[red]Error saving baseline resume: {e}[/red]")
            
            # Ask if the pre-package is ready to send.
            ready = Confirm.ask("Is this tailored pre-package (job posting + baseline) ready to send?")
            if not ready:
                pre_package = {
                    "baseline": baseline_resume,
                    "job_posting": job_posting,
                    "status": "incomplete",
                    "last_modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                pre_package_file = os.path.join(dir_path, "resume.json")
                try:
                    with open(pre_package_file, "w") as f:
                        json.dump(pre_package, f, indent=4)
                    console.print(f"[green]Pre-package saved as incomplete to '{pre_package_file}'.[/green]")
                except Exception as e:
                    console.print(f"[red]Error saving pre-package: {e}[/red]")
                continue
            
            # If ready, call the external structured output class with the cleaned job posting.
            tailor = ResumeTailorStructuredOutput()
            try:
                tailored_resume = tailor.tailor_resume(baseline_resume, cleaned_job_posting)
                if tailored_resume:
                    tailored_resume["status"] = "complete"
            except Exception as e:
                console.print(f"[red]Tailoring failed: {e}[/red]")
                continue
            
            if tailored_resume:
                tailored_file = os.path.join(dir_path, "resume.json")
                try:
                    with open(tailored_file, "w") as f:
                        json.dump(tailored_resume, f, indent=4)
                    console.print(f"[green]Tailored resume saved to '{tailored_file}'.[/green]")
                except Exception as e:
                    console.print(f"[red]Error saving tailored resume: {e}[/red]")
        
        elif choice == "3":
            console.print("[bold yellow]Listing all resumes:[/bold yellow]")
            resumes_found = list_resumes()
            if resumes_found:
                for name, data in resumes_found.items():
                    status = data.get("status", "unknown")
                    last_modified = data.get("last_modified", "N/A")
                    console.print(f"[blue]{name}[/blue] - Status: [bold]{status}[/bold] | Last Modified: {last_modified}")
            else:
                console.print("[red]No resumes found.[/red]")
        
        elif choice == "4":
            resumes_found = list_resumes()
            if not resumes_found:
                console.print("[red]No resumes available to load.[/red]")
                continue
            console.print("[bold yellow]Available Resumes:[/bold yellow]")
            resume_names = list(resumes_found.keys())
            for idx, name in enumerate(resume_names, start=1):
                console.print(f"{idx}. {name}")
            selection = Prompt.ask("Enter the number or name of the resume you want to load")
            if selection.isdigit():
                selection_idx = int(selection) - 1
                if 0 <= selection_idx < len(resume_names):
                    selected_resume = resume_names[selection_idx]
                else:
                    console.print("[red]Invalid selection.[/red]")
                    continue
            else:
                if selection in resumes_found:
                    selected_resume = selection
                else:
                    console.print("[red]Invalid selection.[/red]")
                    continue
            loaded = load_resume(selected_resume)
            if loaded:
                console.print(f"[bold green]Resume: {selected_resume}[/bold green]")
                console.print_json(data=loaded)
            else:
                console.print("[red]Error loading resume.[/red]")
        
        elif choice == "5":
            # Create Cover Letter for a Tailored Resume
            resumes_found = list_resumes()
            if not resumes_found:
                console.print("[red]No resumes available to load.[/red]")
                continue
            console.print("[bold yellow]Available Tailored Resumes (must have job posting data):[/bold yellow]")
            tailored_options = []
            for name, data in resumes_found.items():
                # Check if this resume directory has a job posting file
                dir_path = get_resume_path(name)
                job_posting_path = os.path.join(dir_path, "job_posting_ai.txt")
                if os.path.exists(job_posting_path):
                    tailored_options.append(name)
                    console.print(f"- {name}")
            if not tailored_options:
                console.print("[red]No tailored resumes with job posting data found.[/red]")
                continue
            selected_resume = Prompt.ask("Enter the name of the tailored resume to use")
            if selected_resume not in tailored_options:
                console.print("[red]Invalid selection.[/red]")
                continue
            # Load the tailored resume
            tailored_resume = load_resume(selected_resume)
            if not tailored_resume:
                console.print("[red]Failed to load the tailored resume.[/red]")
                continue
            # Load job posting data from job_posting_ai.txt
            job_posting_path = os.path.join(get_resume_path(selected_resume), "job_posting_ai.txt")
            try:
                with open(job_posting_path, "r") as f:
                    job_posting_data = f.read()
            except Exception as e:
                console.print(f"[red]Error loading job posting data: {e}[/red]")
                continue
            # Generate the cover letter via OpenAI Chat Completion.
            cover_letter = create_cover_letter(tailored_resume, job_posting_data)
            if cover_letter is None:
                continue
            # Save the cover letter to cover_letter.json in the tailored resume directory
            cover_letter_file = os.path.join(get_resume_path(selected_resume), "cover_letter.json")
            try:
                with open(cover_letter_file, "w") as f:
                    json.dump(cover_letter, f, indent=4)
                console.print(f"[green]Cover letter saved to '{cover_letter_file}'.[/green]")
            except Exception as e:
                console.print(f"[red]Error saving cover letter: {e}[/red]")
            console.print("[bold cyan]Generated Cover Letter:[/bold cyan]")
            console.print_json(data=cover_letter)
        
        elif choice == "6":
            console.print("[bold magenta]Adios amigo![/bold magenta]")
            break

if __name__ == "__main__":
    main_menu()
