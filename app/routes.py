from app import app
from flask import render_template, request, redirect, url_for
import os
import json
from pymongo import MongoClient

#connection to our Database MongoDB
# client = MongoClient("mongodb://saadahmed20940:syed2094@ds241968.mlab.com:41968/fullstack")
# db = client['test']
uri = 'mongodb://saadahmed20940:syed2saad@ds241968.mlab.com:41968/fullstack?retryWrites=false'
client = MongoClient(uri,connectTimeoutMS=30000,socketTimeoutMS=None,socketKeepAlive=True)
db = client.get_default_database()


#home page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


#for submitting the fields to DB
@app.route('/submit', methods=['GET', 'POST'])
def hello():
	#here we have to add scrappers for different news websites available in the JSON file.
	print('hello inside submit')
	if request.method == 'POST':
		data = request.get_json()
		# beleivabilityindex=request.form['_beleivabilityindex']
		# priorknowledge=request.form['_priorknowledge']
		# headline=request.form['_headline']
		# body=request.form['_body']
		data_insertion = [{
			"beleivabilityindex":data['_beleivabilityindex'],
			"priorknowledge":data['_priorknowledge'],
			"headline":data['_headline'],
			"body":data['_body']
		}]
		db.test.insert_many(data_insertion)
		return json.dumps(True)
	else:
		return render_template('index.html')


#rendering the data from JSON file for display
@app.route('/render')
def render():
    # filename = os.path.join(app.static_folder, 'sample.json')
    # with open(filename) as blog_file:
    #     #json_data = json.dumps(json.loads(blog_file.read()))
    #     json_data = json.loads(blog_file.read())
    #     work_url = json_data[0]['url']
    #     print(work_url)


    filename = os.path.join(app.static_folder, 'sample.json')
    with open(filename) as blog_file:
        return json.dumps(json.loads(blog_file.read()))
