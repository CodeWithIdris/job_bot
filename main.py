from scraper import fetch_jobs
from matcher import filter_jobs
from generator import generate_cover_letter
from sender import send_application
from apply_bot import apply_to_job
import time

skills = "research strategy academic writing policy analysis data analysis consulting evaluation"

print("🚀 Starting Job Bot...")

jobs = fetch_jobs()
print(f"📥 Total jobs fetched: {len(jobs)}")

qualified = filter_jobs(jobs, skills)
print(f"🎯 Qualified jobs: {len(qualified)}")

sent_count = 0

for job in qualified[:5]:  # limit daily sends
    print(f"\nChecking job: {job.get('position')} at {job.get('company')}")

    if job.get("email"):
        print("📧 Email found. Sending application...")
        cover = generate_cover_letter(job)
        send_application(job, cover)
        sent_count += 1
        time.sleep(5)
    else:
        print("❌ No email found. Skipping.")
for job in qualified[:3]:  # small limit

    print(f"\nChecking job: {job.get('position')} at {job.get('company')}")

    success = apply_to_job(job, "resume.pdf")

    if success:
        sent_count += 1

print(f"\n✅ Applications sent today: {sent_count}")
print("🏁 Job Bot finished.")

