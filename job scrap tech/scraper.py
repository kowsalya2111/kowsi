import requests
from bs4 import BeautifulSoup
import time
import random

SIMULATE_SCRAPED = 15  

def scrape_jobs():
    print(" Fetching jobs...")
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0.4, 0.8))

    print("\nParsing job listings.......")
    time.sleep(0.8)

    url = "https://www.indeed.com/jobs?q=python+developer&l=India"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    
    job_cards = soup.find_all("div", class_="job_seen_beacon")

    jobs = []
    for job in job_cards[:SIMULATE_SCRAPED]:
        title_tag = job.find("h2", class_="jobTitle")
        company_tag = job.find("span", class_="companyName")
        location_tag = job.find("div", class_="companyLocation")
        link_tag = title_tag.find("a", href=True)

        title = title_tag.text.strip() if title_tag else "N/A"
        company = company_tag.text.strip() if company_tag else "N/A"
        location = location_tag.text.strip() if location_tag else "N/A"
        link = f"https://www.indeed.com{link_tag['href']}" if link_tag else "N/A"

        jobs.append((title, company, location, link))

    if not jobs:
        print("⚠️  No jobs found!")
        return

    print(f" {len(jobs)} jobs scraped successfully!\n")
    for idx, (title, company, location, link) in enumerate(jobs, start=1):
        time.sleep(random.uniform(0.1, 0.4))
        print(f"{idx}. {title} | {company} | {location} | Apply: {link}")

if __name__ == "__main__":
    scrape_jobs()
