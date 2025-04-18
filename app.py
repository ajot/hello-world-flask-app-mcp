from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/joke')
def get_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        joke_data = response.json()
        return jsonify({
            'joke': joke_data['value'],
            'categories': joke_data['categories'],
            'id': joke_data['id']
        })
    else:
        return jsonify({'error': 'Failed to fetch joke'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port) 