
##flask app to print "Hello Visnu"

from flask import Flask
import pandas as pd
import numpy as np

app=Flask(__name__)

@app.route("/")
def home():
    return 'Hello Visnu! welcome you'

@app.route('/hel/')
def hello():
    return 'My name is Visnu'


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
