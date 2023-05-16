from flask import Flask, jsonify 
import time 
import hashlib, requests
from keys import PUBLIC_KEY, PRIVATE_KEY

app = Flask(__name__)
PUBLIC_KEY = PUBLIC_KEY
PRIVATE_KEY = PRIVATE_KEY
BASE_URL = 'https://gateway.marvel.com/v1/public/'

def generate_hash(ts, private_key, public_key):
    m = hashlib.md5()
    m.update(f"{ts}{private_key}{public_key}".encode('utf-8'))
    return m.hexdigest()

@app.route('/characters')
def get_characters():
    ts = str(time.time())
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash,
        'limit': 100
    }
    response = requests.get(f"{BASE_URL}characters", params=params)
    return response.json()

app.run(debug=True)