import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
with open('userstable.sql') as f:
    conn.executescript(f.read())
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('Sanjith','password123'))
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('Alex','abcdefg'))
conn.commit()
conn.close()

print("Database initialized")
