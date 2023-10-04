from flask import Flask
from flask import request
from waitress import serve
from flask import jsonify
from flask_cors import CORS
import TTS
import requests
import urllib.parse
import base64
import os
import yaml, json
from yaml import SafeLoader
import subprocess
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



p = subprocess.Popen(req, stdout=subprocess.PIPE, shell=True)