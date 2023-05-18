from flask import Flask, jsonify, render_template 
import time 
import hashlib, requests
from keys import PUBLIC_KEY, PRIVATE_KEY, BASE_URL
from flask_bootstrap import Bootstrap
from models import events



app = Flask(__name__)
Bootstrap(app)
PUBLIC_KEY = PUBLIC_KEY
PRIVATE_KEY = PRIVATE_KEY
BASE_URL = BASE_URL

def generate_hash(ts, private_key, public_key):
    m = hashlib.md5()
    m.update(f"{ts}{private_key}{public_key}".encode('utf-8'))
    return m.hexdigest()

@app.route('/comics', methods=['GET'])
def get_comics():
    ts = str(time.time())
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash,
        'limit': 21
    }
    response = requests.get(f"{BASE_URL}comics", params=params)
    return response.json()



@app.route('/bootycharacters', methods=['GET'])
def get_booycharacters():
    ts = str(time.time())
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash,
        'limit': 1
    }
    response = requests.get(f"{BASE_URL}characters", params=params)
    my_characters = response.json()['data']['results'][0]
    return render_template('my_characters.html', character=my_characters)



@app.route('/events', methods=['GET'])
def get_events():
    ts = str(time.time())
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash,
        'limit': 5,
        'offset': 3
    }
    response = requests.get(f"{BASE_URL}events", params=params)
    event_data = response.json()['data']['results']
    my_real_data = event_data[0]['series']
    return render_template('character.html', seriesDetails=my_real_data)
            
            


@app.route('/creators', methods=['GET'])
def get_creators():
    ts = str(time.time())
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash,
        'limit': 21
    }
    response = requests.get(f"{BASE_URL}creators", params=params)
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
    my_chararcters = response.json()['data']['results'][0]
    return render_template('character.html', character=my_chararcters)



app.run(debug=True)

