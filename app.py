from flask import Flask, render_template
from flask_s3 import FlaskS3
import uuid
import os


app = Flask(__name__)
app.config['FLASKS3_REGION'] = 'us-west-2'

@app.route('/', methods=['GET', 'POST'])
def index():
        render_template('index.html')

 