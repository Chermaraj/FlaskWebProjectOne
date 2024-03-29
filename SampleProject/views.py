from flask import Flask
from SampleProject import app
from datetime import datetime
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
         title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)