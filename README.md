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
  echo '#!/bin/bash
python3 main.py' > run.sh
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

## Resume Tailoring & Cover Letter Generator - Examples

This document provides examples of how the Resume Tailoring & Cover Letter Generator transforms a baseline resume into a tailored one based on a job posting. Additionally, it showcases an AI-generated cover letter.

---

### Example: Baseline Resume

The following is a sample baseline resume before tailoring:

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
            "summary": "Laid-back, easygoing professional with years of experience in casual philosophy, recreational bowling, and conflict resolution through nonchalance..."
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
                    "Handled disputes with fellow players with a relaxed attitude..."
                ],
                "achievements": [
                    "Successfully avoided unnecessary aggression in competitive environments.",
                    "Influenced an entire subculture of nonchalant enthusiasts."
                ]
            }
        ],
        "education": [
            {
                "institution": "University of Life",
                "degree": "Master of Chill",
                "location": "Various Locations",
                "start_date": "Ongoing",
                "end_date": "Eternal"
            }
        ]
    },
    "status": "complete",
    "last_modified": "2025-02-19 12:00:00"
}
```

---

### Example: Tailored Resume

After running the tailoring process with a job posting for a **Product Manager, Core Product at Anthropic**, the resume is updated to align with the position's requirements:

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
            "summary": "Laid-back, easygoing professional with years of experience in casual philosophy and innovative strategy. Adept at developing and articulating product strategies that enhance collaboration..."
        },
        "work_experience": [
            {
                "job_title": "Professional Bowler & Lounge Enthusiast",
                "company": "The Bowling Alley",
                "location": "Los Angeles, California",
                "responsibilities": [
                    "Advocated for a more laid-back approach to life while maintaining a respectable bowling average.",
                    "Developed strategic frameworks for player collaboration and long-term performance consistency."
                ]
            }
        ],
        "leadership_skills": [
            "Maintaining a Chill Attitude",
            "Cross-functional Leadership in Complex Product Environments"
        ],
        "tools": [
            "Bowling Ball",
            "Modern AI Collaboration Platforms"
        ]
    },
    "status": "complete",
    "last_modified": "2025-02-19 19:55:05"
}
```

The AI has updated the **job target, personal summary, and leadership skills** to better align with the Product Manager role, while retaining the essence of the original resume.

---

### Example: AI-Generated Cover Letter

A tailored cover letter is generated based on the customized resume and job posting:

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

This cover letter highlights **alignment with the company's mission, product strategy insights, and unique soft skills** while keeping the tone engaging and memorable.

---

### Summary of Features Demonstrated

1. **Baseline Resume Creation** – Start with a structured resume template.
2. **AI-Powered Tailoring** – Aligns experience with specific job descriptions.
3. **Cover Letter Generation** – Produces a job-specific, compelling letter.
4. **Minimal Effort, Maximum Impact** – Automates the application customization process.

This tool makes job applications effortless while ensuring each submission is uniquely crafted for the role.

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
