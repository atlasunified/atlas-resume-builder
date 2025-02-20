# Resume Tailoring & Cover Letter Generator

A command-line tool that leverages the power of OpenAI's API to help you build, tailor, and enhance your resume for specific job postings. This project provides an interactive interface to create a baseline resume, customize it to match job posting details, and even generate an engaging cover letter—all while delivering a unique user experience with background MIDI playback.

---

## Features

- **Interactive Resume Builder:**  
  Prompt-based creation of a comprehensive baseline resume with sections for personal details, work experience, education, certifications, and more.

- **Tailored Resume Generation:**  
  Automatically tailor your baseline resume to match specific job postings by updating key fields such as job target, personal summary, work experience details, leadership skills, and tools.

- **Job Posting Scraping & Cleaning:**  
  - Scrape job posting details from a URL using BeautifulSoup.  
  - Clean and process job posting text using OpenAI's GPT-4 model to extract relevant job details.

- **Cover Letter Creation:**  
  Generate a captivating cover letter in JSON format using your tailored resume and job posting details.

- **Structured Output with AI:**  
  Uses a dedicated module (`structured_output.py`) that defines a JSON schema to ensure the tailored resume output meets a strict format and only modifies specific fields.

- **MIDI Background Playback:**  
  Enjoy a random MIDI track playing in the background while you work, courtesy of the Pygame library (optional).

- **Rich CLI Experience:**  
  Leverages the [Rich](https://github.com/Textualize/rich) library for colorful, formatted terminal output and interactive prompts.

---

## Installation

1. **Clone the Repository:**

   ```
   git clone https://github.com/yourusername/resume-tailor.git
   cd resume-tailor
   ```

2. **Install Dependencies:**

   Ensure you have Python 3.x installed. Then, install the required packages:

   ```
   pip install openai requests beautifulsoup4 rich pygame
   ```

3. **Set Up Your OpenAI API Key:**

   - **Environment Variable:**  
     Set the `OPENAI_API_KEY` environment variable.

   - **Or, API Key File:**  
     Create a file named `openai-api-key.txt` in the project root and paste your API key inside.

4. **(Optional) Add MIDI Files:**

   Create a `midi` directory in the project root and add `.mid` or `.midi` files to enhance your experience with background music.

---

## Usage

Run the main script to launch the interactive CLI:

```
python main.py
```

Upon starting, you'll see a welcome banner and a main menu offering the following options:

1. **Create/Edit Baseline Resume:**  
   Build your baseline resume by providing personal, work, and educational details through guided prompts.

2. **Create a Tailored Resume for a Job Posting:**  
   - Select an existing baseline resume.
   - Input a job posting URL or paste the job details.
   - The tool will scrape, clean, and tailor your resume to match the job requirements using the structured output module.

3. **List All Resumes:**  
   View all resumes saved in the `resumes` directory along with their status and last modified timestamp.

4. **Load and View a Resume:**  
   Load a specific resume and view its JSON content directly in the terminal.

5. **Create Cover Letter for a Tailored Resume:**  
   Generate a custom cover letter (in JSON format) using a tailored resume and its associated job posting data.

6. **Quit:**  
   Exit the application.

---

## Directory Structure

```
resume-tailor/
├── main.py                   # Main interactive CLI application
├── structured_output.py      # Module handling resume tailoring via structured AI output
├── openai-api-key.txt        # (Optional) File to store your OpenAI API key
├── resumes/                  # Directory where all resumes and related job posting data are stored
└── midi/                     # (Optional) Directory containing MIDI files for background playback
```

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
