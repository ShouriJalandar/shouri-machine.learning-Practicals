import sqlite3

def add_new_project(title, description):
    # 1. Connect to the database
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()
    
    # 2. SQL Insert Command
    # We use '?' placeholders to prevent SQL Injection (a common security risk)
    query = "INSERT INTO projects (title, description) VALUES (?, ?)"
    data = (title, description)
    
    try:
        cursor.execute(query, data)
        conn.commit()
        print(f"✅ Success! '{title}' has been added to your SQL database.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()

# --- INPUT YOUR PROJECTS HERE ---

# Example 1: Your IoT Project
add_new_project("EcoPulse: IoT Analytics", "Real-time sensor data processing using Raspberry Pi and Python.")

# Example 2: Your Gas Leak Detector
add_new_project("Gas Leak Detector", "Safety system using MQ2/MQ5 sensors to monitor air quality.")

# Example 3: AWS Cloud Project (Optional)
# add_new_project("AWS Cloud Resume", "Hosting a resume website using S3 and CloudFront.")