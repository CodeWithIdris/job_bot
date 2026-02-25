from scraper import fetch_jobs
from matcher import filter_jobs
from generator import generate_cover_letter
from sender import send_application

skills = "research strategy academic writing policy analysis data analysis consulting evaluation"

jobs = fetch_jobs()
qualified = filter_jobs(jobs, skills)

for job in qualified[:5]:  # limit daily sends
    if job.get("email"):
        cover = generate_cover_letter(job)
        send_application(job, cover)

        