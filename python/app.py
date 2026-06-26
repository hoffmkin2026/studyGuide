from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash 
import sqlite3
import os 
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is not set")
    client = None
else:
    client = OpenAI(api_key=api_key)

app = Flask(__name__)
app.secret_key = "super_secure_key"

def get_db():
    conn = sqlite3.connect("study.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        db.close()

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect("/main")
        else:
            return render_template("index.html", error="Invalid username or password")
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/main")
def main():
    if "user" not in session: 
        return redirect("/")

    return render_template("main.html")

@app.route("/english")
def english():
    if "user" not in session:
        return redirect("/")

    db = get_db()
    topics = db.execute("SELECT title, content, questions FROM topics WHERE subject='English' ORDER BY title ASC").fetchall()
    db.close() 
    return render_template("english.html", topics=topics)

@app.route("/math")
def math():
    if "user" not in session:
        return redirect("/")

    db = get_db()
    topics = db.execute("SELECT title, content, questions FROM topics WHERE subject='Math' ORDER BY title ASC").fetchall()
    db.close()
    return render_template("math.html", topics=topics)

@app.route("/software")
def software():
    if "user" not in session:
        return redirect("/")

    db = get_db()
    topics = db.execute("SELECT title, content, questions FROM topics WHERE subject='Software' ORDER BY title ASC").fetchall()
    db.close()
    return render_template("software.html", topics=topics)

@app.route("/business")
def business():
    if "user" not in session:
        return redirect("/")

    db = get_db()
    topics = db.execute("SELECT title, content, questions FROM topics WHERE subject='Business' ORDER BY title ASC").fetchall()
    db.close()
    return render_template("business.html", topics=topics)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"reply": "No JSON received"}), 400

        user_message = data.get("message", "")

        print("Trying OpenAI...")
        print("Message:", user_message)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful software engineering tutor."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        print("OpenAI responded")

        ai_reply = response.choices[0].message.content

        return jsonify({
            "reply": ai_reply
        })

    except Exception as e:
        print("OPENAI ERROR:")
        print(str(e))

        return jsonify({
            "reply": f"Server Error: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run()







