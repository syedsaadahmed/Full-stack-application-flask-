from app import app
from flask import render_template
import os
import json
from pymongo import MongoClient

#connection to our Database MongoDB
client = MongoClient("mongodb://saadahmed20940:syed2094@ds241968.mlab.com:41968/fullstack")
db = client['test']

#home page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


#for submitting the fields to DB
@app.route('/submit')
def hello():
	return "blah blah blah"
	#here we have to add scrappers for different news websites available in the JSON file.



#rendering the data from JSON file for display
@app.route('/render')
def render():
    filename = os.path.join(app.static_folder, 'sample.json')
    with open(filename) as blog_file:
        return json.dumps(json.loads(blog_file.read()))

