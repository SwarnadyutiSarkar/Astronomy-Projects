import sqlite3

# Create SQLite database
conn = sqlite3.connect('bird_sightings.db')
c = conn.cursor()

# Create table for bird sightings
c.execute('''CREATE TABLE IF NOT EXISTS sightings
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              species TEXT,
              location TEXT,
              latitude REAL,
              longitude REAL)''')

# Commit changes and close connection
conn.commit()
conn.close()
