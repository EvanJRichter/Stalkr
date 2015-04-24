from flask import Flask, render_template, url_for, copy_current_request_context, request, jsonify, Response, json, redirect
import requests
import crawler

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

		linkedin_info = crawler.linkedin_stalk(stalkee_name, stalkee_location)

	return render_template("results.html", facebook_information = linkedin_info)



if __name__ == '__main__':
    app.run(debug=True, threaded=True)


