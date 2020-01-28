from flask import (Flask, request)
import csv
import codecs

app = Flask(__name__)

@app.route('/vrb2json/v1/convert', methods=['POST'])
def convert():
    return request.get_data()

@app.route('/vrb2json/v1/info', methods=['GET'])
def info():
    return 'This is the vrs2json service.'
