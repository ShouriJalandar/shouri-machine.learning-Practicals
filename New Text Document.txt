import sqlite3

# This line creates a file named 'resume.db' automatically
connection = sqlite3.connect('resume.db')
cursor = connection.cursor()

# 1. Create a table for your Personal Info
cursor.execute('''
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY,
        name TEXT,
        college TEXT,
        skills TEXT
    )
''')

# 2. Create a table for your Projects (like EcoPulse)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT
    )
''')

# 3. Put YOUR data into the tables
cursor.execute("INSERT INTO profile (name, college, skills) VALUES (?, ?, ?)", 
               ('Shouri', 'S.B. Jain Institute', 'Python, C++, AWS, Java'))

cursor.execute("INSERT INTO projects (title, description) VALUES (?, ?)", 
               ('EcoPulse', 'IoT Data Analytics using Raspberry Pi and sensors.'))

# Save the changes and close
connection.commit()
connection.close()

print("Database created and Shouri's data saved successfully!")