from flask import Flask, jsonify
import random
import json
  
# creating a Flask app
app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
    return(
        '''
    <h1>hadith api</h1>
    <h2>get random</h2>
    <a href="/bukhari">sahih al-bukhari </a>
    <br>
    <a href="/muslim">sahih muslim</a>
    <h2>get custom</h2>
    <p>bukhari limit 1-7563
        <br>
        muslim limit 1-3032
    </p>
    <a href="/bukhari/1">/bukhari/1</a>
    <br>
    <a href="/muslim/1">/muslim/1</a>
    '''
    )
  
@app.route('/muslim/')
@app.route('/muslim/<int:id>', methods = ['GET'])
def muslim(id=None):
    if id is None:
        id = random.randint(1, 3034)
    if(id):
        id = id-1
    with open('muslim.json') as f:
        data = json.load(f)
    d = data['hadith'][id]
    return jsonify({'data': d})

@app.route('/bukhari/')
@app.route('/bukhari/<int:id>', methods = ['GET'])
def bukhari(id=None):
    if id is None:
        id = random.randint(1, 7564)
    if(id):
        id = id-1
    with open('bukhari.json') as f:
        data = json.load(f)
    d = data['hadith'][id]
    return jsonify({'data': d})
  
if __name__ == "__main__":
    app.run()