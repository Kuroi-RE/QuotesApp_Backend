# Satria
from flask import Flask, jsonify, request
import json
from flask_cors import CORS, cross_origin
import random
from utils import load_quotes, filter_by_lang

app = Flask(__name__)
cors = CORS(app)
quotes = load_quotes()

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return jsonify({"message": "Endpoints: /quote, /quotes"}) 

@app.route('/quote', methods=['GET'])
@cross_origin()
def get_random_quote():
    lang = request.args.get('lang')
    filtered_quotes = filter_by_lang(quotes, lang) if lang else quotes
    return jsonify(random.choice(filtered_quotes))

#Gesa
@app.route('/quotes', methods=['GET'])
@cross_origin()
def get_all_quotes():
    return jsonify(quotes)

if __name__ == '__main__':
    app.run(debug=True)