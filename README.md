![The Dude](thedude.jpg)

---

# Resume Tailoring & Cover Letter Generator

Hey man, need to polish up your resume? Tailor it to a specific job posting? Maybe even get a cover letter that doesn’t sound like it was written by a corporate drone? This tool's got you covered. 

A command-line interface that leverages OpenAI’s API to help you build, refine, and enhance your resume for specific jobs—all while keeping things smooth and easy. If you want, you can even enjoy some background MIDI tunes while you work. Because, hey, vibes matter.

---

## Features

- **Interactive Resume Builder:**  
  A guided, no-fuss way to enter your experience, skills, and all that jazz.

- **Tailored Resume Generation:**  
  Input a job posting, and this tool will update your resume so it actually speaks to that job. No more sending the same generic resume everywhere, dude.

- **Job Posting Scraping & Cleaning:**  
  - Scrapes job details from a URL (yeah, the internet is wild).  
  - Uses OpenAI’s GPT-4 to extract only the good stuff—no fluff, just what you need.

- **Cover Letter Creation:**  
  Generates a unique, well-crafted cover letter. None of that robotic “Dear Sir or Madam” nonsense.

- **Structured Output with AI:**  
  Ensures the resume stays formatted properly while only updating what’s necessary.

- **MIDI Background Playback (Optional, but rad):**  
  Drop some `.mid` files in the `midi` folder and set the mood while you apply for jobs.

- **Rich CLI Experience:**  
  Colorful, formatted text powered by [Rich](https://github.com/Textualize/rich). Because why should terminals be boring?

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/atlasunified/atlas-resume-builder.git
   cd atlas-resume-builder
   ```

2. **Install Dependencies:**  
   Make sure you have Python 3.x installed, then install the necessary packages:

   ```bash
   pip install openai requests beautifulsoup4 rich pygame
   ```

3. **Set Up Your OpenAI API Key:**  

   - **Option 1: Use an environment variable:**  
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```

   - **Option 2: Use a file (for the forgetful among us):**  
     Create a file named `openai-api-key.txt` in the project root and drop your API key inside.

4. **(Optional) Add MIDI Files:**  
   If you like working with a soundtrack, throw some `.mid` or `.midi` files in the `midi` directory.

---

## Usage

Run the main script to launch the interactive CLI:

```bash
python main.py
```

### What You’ll See

Once it starts, you’ll be greeted with a menu that lets you:

1. **Create/Edit Baseline Resume** – Start fresh or edit an existing resume.
2. **Create a Tailored Resume for a Job Posting** – Customize your resume to match a specific job.
3. **List All Resumes** – See all the resumes you’ve saved.
4. **Load and View a Resume** – Open a specific resume and view the details.
5. **Create Cover Letter for a Tailored Resume** – Let the AI generate a slick, job-specific cover letter.
6. **Quit** – Because sometimes, you just need to take it easy.

---

## Running Without an IDE

No need for fancy software, man. This thing runs right in your terminal.

- **Basic Command:**  
  ```bash
  python main.py
  ```
- **Want an easy one-click method?**  
  Create a simple Bash script:

  ```bash
  echo -e '#!/bin/bash\npython3 main.py' > run.sh
  chmod +x run.sh
  ./run.sh
  ```

  Or, for Windows folks, a batch script:

  ```bat
  echo python main.py > run.bat
  ```

  Then double-click `run.bat` to launch.

---

## Directory Structure

```
atlas-resume-builder/
├── main.py                   # Main interactive CLI application
├── structured_output.py      # Handles AI-powered resume tailoring
├── openai-api-key.txt        # (Optional) Store your API key here
├── resumes/                  # Where all your resumes and job postings are stored
└── midi/                     # (Optional) Drop MIDI files here for background music
```

---

# Resume Tailoring & Cover Letter Generator - Examples

Alright, man, here’s how this thing works. This document lays out how the Resume Tailoring & Cover Letter Generator takes your baseline resume and—like a chill, AI-powered rug—ties it all together with a job posting. You’ll also see an AI-generated cover letter, because, y'know, sometimes you gotta make it official.

---

### Example: Baseline Resume

Here’s what we’re working with before the AI steps in. This is the raw material, the unshaped clay of your professional existence:

```json
{
    "resume": {
        "job_target": {
            "position_title": "",
            "company": "",
            "location": "",
            "salary_desired": ""
        },
        "personal_info": {
            "name": "Jeffrey Lebowski",
            "email": "thedude@ruglover.com",
            "phone": "(310) 555-1998",
            "summary": "Laid-back, easygoing professional with years of experience in casual philosophy, recreational bowling, and conflict resolution through nonchalance. Adept at maintaining an even keel in chaotic situations. Passionate about achieving inner peace, mixing the perfect White Russian, and ensuring that rugs really tie the room together."
        },
        "work_experience": [
            {
                "job_title": "Professional Bowler & Lounge Enthusiast",
                "company": "The Bowling Alley",
                "location": "Los Angeles, California",
                "start_date": "1980",
                "end_date": "Present",
                "responsibilities": [
                    "Maintained an impeccable record of showing up for league nights and engaging in friendly competition.",
                    "Developed a signature smooth bowling style that\u2019s been admired (and occasionally questioned) by peers.",
                    "Handled disputes with fellow players with a relaxed attitude, even in moments of extreme tension.",
                    "Advocated for a more laid-back approach to life while maintaining a respectable bowling average."
                ],
                "achievements": [
                    "Successfully avoided unnecessary aggression in competitive environments.",
                    "Influenced an entire subculture of nonchalant enthusiasts.",
                    "Ensured rugs across multiple residences truly tied the rooms together."
                ],
                "programs_managed": [
                    "Local Bowling League",
                    "The Art of Doing Nothing",
                    "Philosophical Discussions Over White Russians"
                ],
                "technologies": [
                    "Bowling Balls",
                    "Rug Maintenance",
                    "Classic Vinyl Records",
                    "Couch Optimization"
                ]
            },
            {
                "job_title": "Casual Detective",
                "company": "Independent Investigator",
                "location": "Los Angeles, California",
                "start_date": "1991",
                "end_date": "1998",
                "responsibilities": [
                    "Investigated the mystery of a missing rug that was integral to home decor.",
                    "Engaged in diplomatic negotiations with eccentric individuals, including nihilists and eccentric businessmen.",
                    "Leveraged casual charisma to obtain key information without exerting undue effort.",
                    "Survived multiple life-threatening situations while maintaining a chilled-out demeanor."
                ],
                "achievements": [
                    "Recovered a fraction of what was lost.",
                    "Navigated treacherous social circles without compromising personal ethics.",
                    "Successfully avoided paying for a new rug."
                ],
                "programs_managed": [
                    "Amateur Investigations",
                    "Surviving Unusual Social Encounters",
                    "Crisis Management Through Relaxation"
                ],
                "technologies": [
                    "Sunglasses",
                    "Taped-Up Jellies",
                    "Answering Machine",
                    "Bowling Lanes"
                ]
            }
        ],
        "education": [
            {
                "institution": "University of Life",
                "degree": "Master of Chill",
                "location": "Various Locations",
                "start_date": "Ongoing",
                "end_date": "Eternal",
                "details": "Deep study into the art of relaxation, casual philosophy, and knowing when to let things slide."
            }
        ],
        "certifications": [
            {
                "name": "League Champion",
                "specialization": "Bowling Excellence",
                "awarded_by": "Local Bowling League",
                "year": "1997"
            },
            {
                "name": "White Russian Mixology",
                "specialization": "Drink Crafting",
                "awarded_by": "Self-Taught",
                "year": "1993"
            }
        ],
        "leadership_skills": [
            "Maintaining a Chill Attitude",
            "Conflict Avoidance",
            "Bowling Strategy",
            "Carpet Appreciation"
        ],
        "tools": [
            "Bowling Ball",
            "Blender (for White Russians)",
            "Sunglasses",
            "Robe & Pajamas"
        ],
        "online_profiles": {
            "hugging_face": "TheDudeAbides",
            "github": "RugLover42"
        }
    },
    "status": "complete",
    "last_modified": "2025-02-19 12:00:00"
}
```

---

### Example: Tailored Resume

Now, we throw in a job posting—let’s say, **Product Manager at Anthropic**—and let the AI work its magic, man. What comes out is something that actually looks like it belongs in that job.

```json
{
    "resume": {
        "job_target": {
            "position_title": "Product Manager, Core Product",
            "company": "Anthropic",
            "location": "San Francisco, CA | New York City, NY",
            "salary_desired": "$305,000 - $385,000 USD"
        },
        "personal_info": {
            "name": "Jeffrey Lebowski",
            "email": "thedude@ruglover.com",
            "phone": "(310) 555-1998",
            "summary": "Laid-back, easygoing professional with years of experience in casual philosophy and innovative strategy. Adept at developing and articulating product strategies that enhance collaboration. Passionate about ensuring that AI capabilities really tie user experiences together."
        },
        "work_experience": [
            {
                "job_title": "Professional Bowler & Lounge Enthusiast",
                "company": "The Bowling Alley",
                "location": "Los Angeles, California",
                "start_date": "1980",
                "end_date": "Present",
                "responsibilities": [
                    "Maintained an impeccable record of showing up for league nights and engaging in friendly competition.",
                    "Developed a signature smooth bowling style that\u2019s been admired (and occasionally questioned) by peers.",
                    "Handled disputes with fellow players with a relaxed attitude, even in moments of extreme tension.",
                    "Advocated for a more laid-back approach to life while maintaining a respectable bowling average."
                ],
                "achievements": [
                    "Successfully avoided unnecessary aggression in competitive environments.",
                    "Influenced an entire subculture of nonchalant enthusiasts.",
                    "Ensured rugs across multiple residences truly tied the rooms together."
                ],
                "programs_managed": [
                    "Local Bowling League",
                    "The Art of Doing Nothing",
                    "Philosophical Discussions Over White Russians"
                ],
                "technologies": [
                    "Bowling Balls",
                    "Rug Maintenance",
                    "Classic Vinyl Records",
                    "Couch Optimization"
                ]
            },
            {
                "job_title": "Casual Detective",
                "company": "Independent Investigator",
                "location": "Los Angeles, California",
                "start_date": "1991",
                "end_date": "1998",
                "responsibilities": [
                    "Investigated the mystery of a missing rug that was integral to home decor.",
                    "Engaged in diplomatic negotiations with eccentric individuals, including nihilists and eccentric businessmen.",
                    "Leveraged casual charisma to obtain key information without exerting undue effort.",
                    "Survived multiple life-threatening situations while maintaining a chilled-out demeanor."
                ],
                "achievements": [
                    "Recovered a fraction of what was lost.",
                    "Navigated treacherous social circles without compromising personal ethics.",
                    "Successfully avoided paying for a new rug."
                ],
                "programs_managed": [
                    "Amateur Investigations",
                    "Surviving Unusual Social Encounters",
                    "Crisis Management Through Relaxation"
                ],
                "technologies": [
                    "Sunglasses",
                    "Taped-Up Jellies",
                    "Answering Machine",
                    "Bowling Lanes"
                ]
            }
        ],
        "education": [
            {
                "institution": "University of Life",
                "degree": "Master of Chill",
                "location": "Various Locations",
                "start_date": "Ongoing",
                "end_date": "Eternal",
                "details": "Deep study into the art of relaxation, casual philosophy, and knowing when to let things slide."
            }
        ],
        "certifications": [
            {
                "name": "League Champion",
                "specialization": "Bowling Excellence",
                "awarded_by": "Local Bowling League",
                "year": "1997"
            },
            {
                "name": "White Russian Mixology",
                "specialization": "Drink Crafting",
                "awarded_by": "Self-Taught",
                "year": "1993"
            }
        ],
        "leadership_skills": [
            "Maintaining a Chill Attitude",
            "Conflict Avoidance",
            "Bowling Strategy",
            "Carpet Appreciation",
            "Cross-functional Leadership in Complex Product Environments"
        ],
        "tools": [
            "Bowling Ball",
            "Blender (for White Russians)",
            "Sunglasses",
            "Robe & Pajamas",
            "Modern AI Collaboration Platforms"
        ],
        "online_profiles": {
            "hugging_face": "TheDudeAbides",
            "github": "RugLover42"
        }
    },
    "status": "complete",
    "last_modified": "2025-02-19 19:55:05"
}
```
See? No unnecessary aggression, just a smooth, job-ready document.

---

### Example: AI-Generated Cover Letter

And if you need a cover letter (which, let’s be honest, a lot of places still want), here’s one generated straight from the tailored resume and job posting:

```json
{
    "Header": {
        "Date": "2025-02-19",
        "Name": "Jeffrey Lebowski",
        "Email": "thedude@ruglover.com",
        "Phone": "(310) 555-1998"
    },
    "Salutation": "Dear Hiring Manager at Anthropic,",
    "Body": {
        "Introduction": "I hope this message finds you well. My name is Jeffrey Lebowski, although many know me as 'The Dude,' a title earned through years of laid-back yet innovative strategizing...",
        "Reference to Job Posting": "Your quest to transform Claude.ai from a conventional AI into an indispensable cognitive partner mirrors my own journey of advocating for collaboration...",
        "Summary of Relevant Experience": "At The Bowling Alley, I maintained a chill ethos while engaging in complex negotiations and maintained integrity and ease under pressure...",
        "Conclusion": "In a world chasing fast-paced progress, I offer an unconventional yet immensely effective approach to innovation and collaboration..."
    },
    "Closing": "Sincerely, Jeffrey Lebowski"
}
```

No corporate fluff, no forced enthusiasm—just a relaxed but confident application.

---

## The Big Picture, Man

1. **Start with Your Baseline Resume** – Something simple, something true to you.  
2. **Run the Tailoring Process** – Let the AI tweak it so it actually fits the job.  
3. **Generate a Cover Letter** – If needed, this thing’ll write one that actually sounds like you.  
4. **Send It Off and Keep It Chill** – No stress, just a solid application.

---

## Configuration & Customization

- **OpenAI Model:**  
  The default model used for generating tailored resumes and cover letters is `gpt-4o`. You can change this in the `ResumeTailorStructuredOutput` class within `structured_output.py`.

- **JSON Schema:**  
  The JSON schema defined in `structured_output.py` ensures that only specific fields are updated during resume tailoring. This schema can be modified if you need to include additional fields or change the structure.

- **Error Handling:**  
  The tool provides console messages (using Rich) to help troubleshoot any issues during scraping, file I/O, or API interactions.

---

## License

This project is distributed under the **Creative Commons CC0 1.0 Universal (Public Domain Dedication)**.

```
CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER.

For these and/or other purposes and motivations, and without any expectation of additional consideration or compensation, the person associating CC0 with a Work (the "Affirmer"), to the extent that he or she is an owner of Copyright and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and publicly distribute the Work under its terms, with knowledge of his or her Copyright and Related Rights in the Work and the meaning and intended legal effect of CC0 on those rights.
```
