import json
import os
from datetime import datetime
from typing import Dict
import openai
from openai import OpenAI

class ResumeTailorStructuredOutput:
    def __init__(self, api_key: str = None, model: str = "gpt-4o"):
        """
        Initialize with an API key and the desired model.
        If no API key is provided, attempt to retrieve it from the environment
        variable or from a file named 'openai-api-key.txt'.
        """
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key and os.path.exists("openai-api-key.txt"):
                with open("openai-api-key.txt", "r") as f:
                    api_key = f.read().strip()
        if not api_key:
            raise ValueError("No OpenAI API key provided.")
        
        openai.api_key = api_key
        self.model = model
        # Instantiate a client instance.
        self.client = OpenAI(api_key=api_key)
        
        # Define a JSON schema that mirrors the desired resume structure.
        # Every object enforces additionalProperties: false.
        self.schema = {
            "name": "tailored_resume",
            "strict": True,
            "schema": {
                "type": "object",
                "additionalProperties": False,
                "required": ["resume", "status", "last_modified"],
                "properties": {
                    "resume": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": [
                            "job_target",
                            "personal_info",
                            "work_experience",
                            "education",
                            "certifications",
                            "leadership_skills",
                            "tools",
                            "online_profiles"
                        ],
                        "properties": {
                            "job_target": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["position_title", "company", "location", "salary_desired"],
                                "properties": {
                                    "position_title": {"type": "string"},
                                    "company": {"type": "string"},
                                    "location": {"type": "string"},
                                    "salary_desired": {"type": "string"}
                                }
                            },
                            "personal_info": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["name", "email", "phone", "summary"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "email": {"type": "string"},
                                    "phone": {"type": "string"},
                                    "summary": {"type": "string"}
                                }
                            },
                            "work_experience": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": [
                                        "job_title",
                                        "company",
                                        "location",
                                        "start_date",
                                        "end_date",
                                        "responsibilities",
                                        "achievements",
                                        "programs_managed",
                                        "technologies"
                                    ],
                                    "properties": {
                                        "job_title": {"type": "string"},
                                        "company": {"type": "string"},
                                        "location": {"type": "string"},
                                        "start_date": {"type": "string"},
                                        "end_date": {"type": "string"},
                                        "responsibilities": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        },
                                        "achievements": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        },
                                        "programs_managed": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        },
                                        "technologies": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        }
                                    }
                                }
                            },
                            "education": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": ["institution", "degree", "location", "start_date", "end_date", "details"],
                                    "properties": {
                                        "institution": {"type": "string"},
                                        "degree": {"type": "string"},
                                        "location": {"type": "string"},
                                        "start_date": {"type": "string"},
                                        "end_date": {"type": "string"},
                                        "details": {"type": "string"}
                                    }
                                }
                            },
                            "certifications": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": ["name", "specialization", "awarded_by", "year"],
                                    "properties": {
                                        "name": {"type": "string"},
                                        "specialization": {"type": "string"},
                                        "awarded_by": {"type": "string"},
                                        "year": {"type": "string"}
                                    }
                                }
                            },
                            "leadership_skills": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "tools": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "online_profiles": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["hugging_face", "github"],
                                "properties": {
                                    "hugging_face": {"type": "string"},
                                    "github": {"type": "string"}
                                }
                            }
                        }
                    },
                    "status": {"type": "string"},
                    "last_modified": {"type": "string"}
                }
            }
        }
    
    def tailor_resume(self, baseline_resume: Dict, job_posting: str) -> Dict:
        """
        Given a baseline resume (as a dict) and a job posting text,
        calls the OpenAI API using Structured Outputs to update only the allowed fields.
        Specifically, update:
         - job_target (all fields)
         - personal_info: update only 'summary'
         - work_experience: update only 'responsibilities', 'achievements', 'programs_managed', and 'technologies'
         - leadership_skills (all fields)
         - tools (all fields)
        Return the updated resume as a dict, with 'status' set to 'complete' and 'last_modified' updated.
        """
        system_message = (
            "You are a professional resume tailoring assistant with expertise in technical resumes. You will be provided with two inputs: a baseline resume and a job posting. "
            "Your task is to update the baseline resume by selectively tailoring it with the job posting details while preserving the original language of the baseline resume as much as possible. "
            "Only modify the specific fields required by the job posting and avoid altering the original phrasing of any work experience or other content that is not explicitly targeted for update. "
            "Make only minimal adjustments to align the content with the job posting. Specifically, update the following fields based on the job posting:\n"
            "1. 'job_target': Revise all fields (position_title, company, location, salary_desired) to reflect the job's requirements, using concise language.\n"
            "2. 'personal_info': Update only the 'summary' field to incorporate key technical qualifications, responsibilities, and outcomes from the job posting, while preserving the original style.\n"
            "3. 'work_experience': For each entry, update only the 'responsibilities', 'achievements', 'programs_managed', and 'technologies' fields if necessary. "
            "Use technical terminology and quantifiable outcomes only where directly relevant to the job posting. Do not add excessive or repetitive language; preserve the original wording as much as possible.\n"
            "4. 'leadership_skills': Update all entries to include any specific technical leadership aspects mentioned in the job posting, without altering the baseline language unnecessarily.\n"
            "5. 'tools': Update all entries to include relevant modern technical tools and platforms mentioned in the job posting, making minimal modifications.\n\n"
            "Do not modify other fields (e.g., education, certifications, online_profiles). "
            "Return the complete updated resume in valid JSON format according to the provided schema, setting 'status' to 'complete' and updating 'last_modified' to the current time."
        )

        user_message = (
            f"Baseline Resume (original):\n{json.dumps(baseline_resume, indent=4)}\n\n"
            f"Job Posting Details:\n{job_posting}\n\n"
            "Using the job posting details above, update the baseline resume accordingly. "
            "Ensure that only the specified fields are updated and all other data remains unchanged."
        )


        try:
            # Use the beta parsing method for Structured Outputs with an increased max_tokens limit
            completion = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                response_format={
                    "type": "json_schema",
                    "json_schema": self.schema
                },
                temperature=1,
                max_tokens=15000
            )
        except Exception as e:
            print("[ERROR] API call failed. Below is the JSON schema used:")
            print(json.dumps(self.schema, indent=2))
            raise Exception(f"Error calling OpenAI API: {e}")

        try:
            # Attempt to access the parsed structured output
            tailored_resume = completion.choices[0].message.parsed
            # If parsed output is None, fallback to parsing the raw content manually.
            if tailored_resume is None:
                content = completion.choices[0].message.content
                tailored_resume = json.loads(content)
            # Override/ensure fields according to the instructions.
            tailored_resume["status"] = "complete"
            tailored_resume["last_modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return tailored_resume
        except Exception as e:
            print("[ERROR] Failed to parse API response into structured JSON. Raw output:")
            print(str(completion))
            raise Exception(f"Failed to parse API response into structured JSON: {e}.")

    def tailor_resume_from_directory(self, directory: str) -> Dict:
        """
        Reads baseline_resume.json and job_posting.txt from the specified directory,
        then calls tailor_resume() with the read data.
        Returns the updated resume as a dict.
        """
        baseline_file = os.path.join(directory, "baseline_resume.json")
        job_posting_file = os.path.join(directory, "job_posting.txt")

        try:
            with open(baseline_file, "r") as bf:
                baseline_resume = json.load(bf)
        except Exception as e:
            raise Exception(f"Error reading baseline resume from {baseline_file}: {e}")

        try:
            with open(job_posting_file, "r") as jf:
                job_posting = jf.read()
        except Exception as e:
            raise Exception(f"Error reading job posting from {job_posting_file}: {e}")

        return self.tailor_resume(baseline_resume, job_posting)
