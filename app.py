import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    return "<h1>Flask + Nginx + PostgreSQL on Docker!</h1>"

@app.route("/add")
def add_item():
    item = request.args.get("item", "default-item")
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) VALUES (%s)", (item,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"added": item})

@app.route("/items")
def get_items():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM items")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1]} for r in rows])

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
