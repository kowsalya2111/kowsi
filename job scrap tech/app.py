from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import time
import random

app = Flask(__name__)
app.secret_key = "supersecretkey" 


def get_jobs(simulate_scraped=13):
    print("🔄 Fetching jobs...")
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0.3, 0.6))
    print("\nParsing job listings.....")
    time.sleep(0.5 + random.random() * 0.5)

    conn = sqlite3.connect('jobs.db')
    cur = conn.cursor()
    cur.execute('SELECT title, company, location, link FROM jobs LIMIT ?', (simulate_scraped,))
    rows = cur.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    jobs = get_jobs()
    return render_template('index.html', jobs=jobs)


users = {'admin': 'admin123'} 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user in users and users[user] == pwd:
            session['user'] = user
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user not in users:
            users[user] = pwd
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User already exists!', 'error')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully!', 'info')
    return redirect(url_for('login'))
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('login'))
    jobs = get_jobs(8)
    return render_template('dashboard.html', jobs=jobs, user=session['user'])

if __name__ == '__main__':
    app.run(debug=True)
