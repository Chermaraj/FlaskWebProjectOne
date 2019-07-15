from flask import Flask
from SampleProject import app

@app.route('/')
@app.route('/home')
def home():
    return "Hello Flask!"