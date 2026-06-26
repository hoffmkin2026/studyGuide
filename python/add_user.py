import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("study.db")

hashed_password = generate_password_hash("1234")

conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", hashed_password))

conn.commit()
conn.close()

print("User added.")
