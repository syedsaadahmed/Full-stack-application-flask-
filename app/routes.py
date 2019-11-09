from app import app
from flask import render_template, request, redirect, url_for, jsonify
import os
import json
from pymongo import MongoClient
from bson import json_util

#connection to our Database MongoDB hosted on mLab
uri = 'mongodb://saadahmed20940:syed2saad@ds241968.mlab.com:41968/fullstack?retryWrites=false'
client = MongoClient(uri,connectTimeoutMS=30000,socketTimeoutMS=None,socketKeepAlive=True)
db = client.get_default_database()


#home page / Main Page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


#for displaying all the data in DB to a HTML page, interface to DB.
@app.route('/display', methods=['GET'])
def get_all_data():
	try:
		all_data  = list(db.test.find())
		return json.dumps(all_data, default=json_util.default, sort_keys=True, indent=4)
	except Exception as e:
		return json.dumps({'error' : str(e)})








#for submitting the fields to DB
@app.route('/submit', methods=['GET', 'POST'])
def hello():
	#got the data from HTML web form
	data = request.get_json()


	# #scrappers for every URL, deciding whether multiple needs the same or not
	# #This work here is being done for the param "Source Name", all the scraping 
	# #will be done and we get the param and will submit it to DB along with other params.



	# import requests
	# from bs4 import BeautifulSoup
	# page = requests.get(data['_newsurl'])
	# soup = BeautifulSoup(page.text, 'html.parser')

	# artist_name_list = soup.find(class_='BodyText')

	# artist_name_list_items = artist_name_list.find_all('a')

	# for artist_name in artist_name_list_items:
	#     print(artist_name.prettify())





	#submitting all the params to DB
	if request.method == 'POST':
		data_insertion = [{
			"beleivabilityindex":data['_beleivabilityindex'],
			"priorknowledge":data['_priorknowledge'],
			"headline":data['_headline'],
			"body":data['_body'],
			"newsurl":data['_newsurl'],
			"newslabel":data['_newslabel'],
			"newsdate":data['_newsdate']
		}]
		db.test.insert_many(data_insertion)
		return json.dumps(True)
	else:
		return render_template('index.html')




#rendering the data from JSON file for display
@app.route('/render')
def render():
    filename = os.path.join(app.static_folder, 'sample.json')
    with open(filename) as blog_file:
        return json.dumps(json.loads(blog_file.read()))
