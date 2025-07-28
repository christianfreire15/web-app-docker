import os
import sqlite3
import requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

DB_PATH = "db/analysis.db"
os.makedirs("db", exist_ok=True)

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
conn.execute('''CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_url TEXT,
    tag1 TEXT,
    tag2 TEXT,
    confidence1 REAL,
    confidence2 REAL
)''')

conn.commit()

IMAGGA_API_KEY = "acc_704360b1c3b0aa3"
IMAGGA_API_SECRET = "369915311813a75e4a6908428c8e6e43"
IMAGGA_ENDPOINT = "https://api.imagga.com/v2/tags"

@app.route('/')
def main():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    results = []

    for image_url in data["images"]:

        response = requests.get(
            IMAGGA_ENDPOINT,
            params={"image_url": image_url},
            auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET)
        )

        tags = response.json()["result"]["tags"][:2]
        tag1, conf1 = tags[0]["tag"]["en"], tags[0]["confidence"]
        tag2, conf2 = tags[1]["tag"]["en"], tags[1]["confidence"]

        results.append({
            "image": image_url,
            "tags": [tag1, tag2],
            "confidences": [conf1, conf2]
        })
        
        conn.execute("INSERT INTO results (image_url, tag1, tag2, confidence1, confidence2) VALUES (?, ?, ?, ?, ?)", (image_url, tag1, tag2, conf1, conf2))
        conn.commit()
    
    return jsonify(results)

@app.route("/results", methods=["GET"])
def results():

    conn.row_factory = sqlite3.Row
    results = conn.execute("SELECT * FROM results").fetchall()

    return render_template('results.html', results=results)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)