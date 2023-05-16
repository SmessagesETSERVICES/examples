from flask import Flask, jsonify, render_template 
import time 
import hashlib, requests
from keys import PUBLIC_KEY, PRIVATE_KEY
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)
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
        'limit': 21
    }
    response = requests.get(f"{BASE_URL}characters", params=params)
    return response.json()

def generer_ts_hash():
    ts = str(time.time())
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    return {'ts': ts, 'hash': hash}

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_char(character_id):
    ts_hash = generer_ts_hash()
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts_hash['ts'],
        'hash': ts_hash['hash']
    }
    response = requests.get(f"{BASE_URL}characters/{character_id}", params=params)
    return response.json()


@app.route('/boot_charac/<int:character_id>', methods=['GET'])
def boot_charac(character_id):
    ts_hash = generer_ts_hash()
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts_hash['ts'],
        'hash': ts_hash['hash']
    }
    response = requests.get(f"{BASE_URL}characters/{character_id}", params=params)
    boot_character = response.json()['data']['results'][0]
    return render_template('character.html', character=boot_character)
app.run(debug=True)