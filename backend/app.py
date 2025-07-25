from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify(message="Hello from Flask!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
