import sqlite3

conn = sqlite3.connect('jobs.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT NOT NULL,
    link TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("Table 'jobs' with location is ready!")
