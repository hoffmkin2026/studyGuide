import sqlite3

conn = sqlite3.connect("study.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE topics ADD COLUMN questions TEXT")
    print("Added 'questions' column successfully")
except Exception as e:
    print("Column may already exist or another error occurred:")
    print(e)

conn.commit()
conn.close()
