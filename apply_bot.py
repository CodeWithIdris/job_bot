from playwright.sync_api import sync_playwright
import time

def apply_to_job(job, resume_path):

    apply_url = job.get("apply_url")

    if not apply_url:
        print("No apply URL found.")
        return False

    print(f"Opening apply page: {apply_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(apply_url, timeout=60000)
            time.sleep(5)

            print("Page loaded.")

            # TEMPORARY: Just check title
            print("Page title:", page.title())

        except Exception as e:
            print("Error loading page:", e)
            browser.close()
            return False

        browser.close()

    return True
