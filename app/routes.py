from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


#for submitting the fields to DB
@app.route('/submit')
def hello():
	return "blah blah blah"
