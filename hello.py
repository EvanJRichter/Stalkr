from flask import Flask, render_template, url_for, copy_current_request_context, request, jsonify, Response, json, redirect
from person import Person

import requests
import crawler
import jsonpickle

app = Flask(__name__)


@app.route('/')
def my_form():	
	return render_template("index.html")


#Takes input from template and adds it to the list
@app.route('/', methods=['POST'])
def my_form_post():
	#when form with value "Search for song" is requested
	if request.form['submit'] == 'Stalk!':
		stalkee_name = request.form['stalkee_name']
		stalkee_location = request.form['stalkee_location']

		linkedin_stalkee = Person()
		linkedin_stalkee.images = []
		linkedin_stalkee = crawler.linkedin_stalk(stalkee_name, stalkee_location, linkedin_stalkee)
		linkedin_stalkee = crawler.facebook_stalk(stalkee_name, stalkee_location, linkedin_stalkee)
		return render_template("results.html", linkedin_information = linkedin_stalkee)

	return render_template("index.html")

@app.route('/_auto_results')
def get_search():
	name = request.args.get("name", "", type = str)
	
	location = request.args.get("location", "", type = str)


	stalkee = Person()
	stalkee.images = []
	stalkee = crawler.linkedin_stalk(name, location, stalkee)
	stalkee = crawler.facebook_stalk(name, location, stalkee)

	
	return jsonpickle.encode(stalkee)




if __name__ == '__main__':
    app.run(debug=True, threaded=True)


