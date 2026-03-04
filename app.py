import sqlite3
import os
from flask import Flask, render_template 

app = Flask(__name__)

# This helps Python find the database file even if you run it from different folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "resume.db")

def get_resume_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get user profile
        cursor.execute("SELECT * FROM profile")
        profile = cursor.fetchone() 
        
        # Get all projects
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall() 
        
        conn.close()
        
        # Fallback if database is empty so the website doesn't crash
        if profile is None:
            profile = [0, "Shouri Jalandar", "S.B. Jain Institute", "Python, SQL, IoT"]
            
        return profile, projects
    except Exception as e:
        print(f"Database Error: {e}")
        return [0, "Shouri Jalandar", "S.B. Jain Institute", "Python, SQL"], []

@app.route('/')
def index():
    # Calling the bridge function
    profile, projects = get_resume_data()
    
    # Passing the SQL data into our HTML template
    # Note: 'user' matches the {{ user[1] }} tags in your new HTML
    return render_template('index.html', user=profile, projects=projects)

if __name__ == '__main__':
    app.run(debug=True)