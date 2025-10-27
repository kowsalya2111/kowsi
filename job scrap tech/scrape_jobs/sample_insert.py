import sqlite3

jobs = [
    ("Python Dev/Capgemini Eng", "Capgemini", "Bengaluru, Karnataka", "https://in.indeed.com/q-software-developer-l-bengaluru%2C-karnataka-jobs.html?vjk=..."),
    ("Python Dev/CygniSoft Tech", "CygniSoft Tech", "Chennai, Tamil Nadu", "https://in.indeed.com/q-software-developer-l-chennai%2C-tamil-nadu-jobs.html?vjk=..."),
    ("Python Dev/Bahwan Cyber", "Bahwan Cyber", "Chennai, Tamil Nadu", "https://in.indeed.com/q-software-engineer-l-chennai%2C-tamil-nadu-jobs.html?vjk=..."),
    ("Python Dev/Amdocs", "Amdocs", "Pune, Maharashtra", "https://in.indeed.com/q-software-developer-l-pune%2C-maharashtra-jobs.html?vjk=..."),
    ("Python Dev/Kairosoft PVT", "Kairosoft PVT", "Ahmedabad, Gujarat", "https://in.indeed.com/q-software-developer-l-ahmedabad%2C-gujarat-jobs.html?vjk=..."),
    ("Python Developer/L&T", "L&T", "Ahmedabad, Gujarat", "https://in.indeed.com/q-software-developer-l-ahmedabad%2C-gujarat-jobs.html?vjk=..."),
    ("Python Dev/CygniSoft Tech", "CygniSoft Tech", "Nagpur, Maharashtra", "https://in.indeed.com/q-software-developer-l-maharashtra-jobs.html?vjk=..."),
    ("Python Dev/P4group", "P4group", "Mumbai, Maharashtra", "https://in.indeed.com/q-software-developer-l-mumbai%2C-maharashtra-jobs.html?vjk=..."),
    ("Python Dev/Accenture", "Accenture", "Ahmedabad, Gujarat", "https://in.indeed.com/company/Accenture/jobs/Python-Developer-a3cb343469d4949f"),
    ("Python Dev/eInfochips", "eInfochips", "Gandhinagar, Gujarat", "https://in.indeed.com/cmp/eInfochips/jobs/Python-Developer-fbf4223403b5b159"),
    ("Java Developer", "Unknown Company", "Bangalore, Karnataka", "https://in.indeed.com/q-java-developer-l-bangalore%2C-karnataka-jobs.html?vjk=..."),
    ("FULL STACK - Optum", "Optum", "Chennai, Tamil Nadu", "https://in.indeed.com/c-Optum/jobs/Full-Stack-d572..."),
    ("Cloud Engineer", "Unknown Company", "Hyderabad, Telangana", "https://in.indeed.com/q-cloud-engineer-l-hyderabad%2C-telangana-jobs.html?vjk=...")
]

conn = sqlite3.connect('jobs.db')
cur = conn.cursor()

# Insert jobs safely
for job in jobs:
    try:
        cur.execute('INSERT INTO jobs (title, company, location, link) VALUES (?, ?, ?, ?)', job)
    except sqlite3.IntegrityError:
        pass  # Skip duplicate links

conn.commit()
conn.close()
print(f"Inserted {len(jobs)} jobs into 'jobs.db' successfully!")
