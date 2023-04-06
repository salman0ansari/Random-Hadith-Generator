from flask import Flask, jsonify
from flask_cors import CORS
import random
import json

# creating a Flask app
app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return """
    <html>
        <head>
            <title>Hadith API</title>
            <style>
                            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 50px;
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #333;
                text-align: center;
                margin-top: 50px;
            }
            h2 {
                color: #333;
                margin-top: 30px;
            }
            p {
                color: #666;
            }
            a {
                color: #333;
                text-decoration: none;
                border-bottom: 1px solid #333;
            }
            a:hover {
                color: #666;
                border-bottom: 1px solid #666;
            }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hadith API</h1>
                <h2>Get random</h2>
                <ul>
                    <li><a href="/bukhari">Sahih Al-Bukhari</a></li>
                    <li><a href="/muslim">Sahih Muslim</a></li>
                    <li><a href="/abudawud">Abu Dawud</a></li>
                    <li><a href="/ibnmajah">Ibn Majah</a></li>
                    <li><a href="/tirmidhi">Al-Tirmidhi</a></li>
                </ul>
                <h2>Get custom</h2>
                <p>
                    Bukhari limit 1-7563<br>
                    Muslim limit 1-3032<br>
                    Abu Dawud limit 1-3998<br>
                    Ibn Majah limit 1-4342<br>
                    Al-Tirmidhi limit 1-3956
                </p>
                <ul>
                    <li><a href="/bukhari/1">/bukhari/1</a></li>
                    <li><a href="/muslim/1">/muslim/1</a></li>
                    <li><a href="/abudawud/1">/abudawud/1</a></li>
                    <li><a href="/ibnmajah/1">/ibnmajah/1</a></li>
                    <li><a href="/tirmidhi/1">/tirmidhi/1</a></li>
                </ul>
                <h2>Web App</h2>
                <p>
                    Check out our <a href="https://salman0ansari.github.io/Random-Hadith-Generator">web app</a> for a better user experience.
                </p>
            </div>
        </body>
    </html>
"""


def get_hadith(filename, max_id, id=None):
    if id is None:
        id = random.randint(1, max_id)
    if id:
        id = id - 1
    with open(filename) as f:
        data = json.load(f)
    d = data["hadith"][id]
    return jsonify({"data": d})


@app.route("/muslim/")
@app.route("/muslim/<int:id>", methods=["GET"])
def muslim(id=None):
    return get_hadith("muslim.json", 3034, id)


@app.route("/bukhari/")
@app.route("/bukhari/<int:id>", methods=["GET"])
def bukhari(id=None):
    return get_hadith("bukhari.json", 7564, id)


@app.route("/abudawud/")
@app.route("/abudawud/<int:id>", methods=["GET"])
def abudawud(id=None):
    return get_hadith("abudawud.json", 3998, id)


@app.route("/ibnmajah/")
@app.route("/ibnmajah/<int:id>", methods=["GET"])
def ibnmajah(id=None):
    return get_hadith("ibnmajah.json", 4342, id)


@app.route("/tirmidhi/")
@app.route("/tirmidhi/<int:id>", methods=["GET"])
def tirmidhi(id=None):
    return get_hadith("tirmidhi.json", 3956, id)
