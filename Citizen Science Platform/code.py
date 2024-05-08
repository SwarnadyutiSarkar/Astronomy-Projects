from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def connect_db():
    return sqlite3.connect('bird_sightings.db')

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Data submission route
@app.route('/submit', methods=['POST'])
def submit():
    species = request.form['species']
    location = request.form['location']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    conn = connect_db()
    c = conn.cursor()
    c.execute('''INSERT INTO sightings (species, location, latitude, longitude)
                 VALUES (?, ?, ?, ?)''', (species, location, latitude, longitude))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3
import folium

# Load data from database
def load_data():
    conn = sqlite3.connect('bird_sightings.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM sightings''')
    data = c.fetchall()
    conn.close()
    return data

# Create map with markers for bird sightings
def create_map(data):
    bird_map = folium.Map(location=[0, 0], zoom_start=2)
    for row in data:
        folium.Marker(location=[row[3], row[4]], popup=row[1], tooltip=row[2]).add_to(bird_map)
    bird_map.save('bird_sightings_map.html')

if __name__ == '__main__':
    bird_data = load_data()
    create_map(bird_data)
