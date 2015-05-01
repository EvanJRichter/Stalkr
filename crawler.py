import unirest
import requests
from person import Person
from pygoogle import pygoogle
from bs4 import BeautifulSoup

#takes a name and a location, googles for that, gets information from the first result.
def linkedin_stalk(name, location, stalkee):
	googlestring = name.replace(" ", "+") + "+" + location + "+linkedin" 
	url = google_first_result(googlestring)

	#if the google search does not return a linkedin profile
	if "vsearch" in url:
		return stalkee

	#get data not logged in
	result = unirest.get(url).body
	stalkee = linkedin_retrieve_data(result, stalkee)

	#log into linkedin to get more information, since it may differ
	client = login_linkedin();
	logged_in_page = client.get(url)
	stalkee = linkedin_retrieve_data(logged_in_page.text, stalkee)

	return stalkee

#retrieve stalkee attributes from soup
def linkedin_retrieve_data(page_html, stalkee):
	soup = BeautifulSoup(page_html)

	nametemp = find_stalkee_attribute_text(soup, "id", "name-container")
	if nametemp:
		stalkee.name = nametemp

	positiontemp = find_stalkee_attribute_text(soup, "class", "title")
	if positiontemp:
		stalkee.position = positiontemp

	imagetemp = find_stalkee_attribute_markup(soup, "alt", stalkee.name)
	if imagetemp:
		#get src from markup
		html_split = str(imagetemp).split("src=")
		html_split = html_split[1].split("width")

		stalkee.images.append(html_split[0])



	industrytemp = find_stalkee_attribute_text(soup, "class", "industry")
	if industrytemp:
		stalkee.industry = industrytemp

	contacttemp = find_stalkee_attribute_text(soup, "id", "contact-comments-view")
	if contacttemp:
		stalkee.contact = contacttemp


	return stalkee

#logs into linkedin and returns a client
def login_linkedin():
	client = requests.Session()

	HOMEPAGE_URL = 'https://www.linkedin.com'
	LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

	html = client.get(HOMEPAGE_URL).content
	soup = BeautifulSoup(html)
	csrf = soup.find(id="loginCsrfParam-login")['value']

	login_information = {
	    'session_key':'brumpotungis@gmail.com',
	    'session_password':'stalkingisfun',
	    'loginCsrfParam': csrf,
	}

	client.post(LOGIN_URL, data=login_information)
	return client

#retrieves URL of stalkee's page, then calls retrieve data with html of page
def facebook_stalk(name, location, stalkee):
	name = name.replace(" ", "-")
	fb_url = "https://www.facebook.com/public/"
	url = fb_url + name 
	results = unirest.get(url).body

	#facebook doesn't like beautiful soup, we have to find the URL ourselves
	result_split = results.split("instant_search_title fsl fwb fcb\"><a href=\"")
	result_split = result_split[1].split("\"")
	stalkee_url = result_split[0]

	results = unirest.get(stalkee_url).body
	resultssoup = BeautifulSoup(results)

	stalkee = facebook_retrieve_data(results, stalkee)
	return stalkee

def facebook_retrieve_data(page_html, stalkee):
	#get source of image from markup
	html_split = page_html.split("<img class=\"profilePic img\"")
	if len(html_split) < 2:
		return stalkee
	html_split = html_split[1].split("src=")
	html_split = html_split[1].split("/>")

	stalkee.images.append(html_split[0].replace("amp;", ""))

	html_split = page_html.split("<img class=\"coverPhotoImg photo img\"")
	html_split = html_split[1].split("src=")
	html_split = html_split[1].split("/>")

	stalkee.images.append(html_split[0].replace("amp;", ""))

	return stalkee




#searches soup for tag with specific value, returns text
def find_stalkee_attribute_text(soup, tag, tag_value):
	raw_markup = soup.find_all(True, {tag:tag_value})
	try:
		raw_text = ''.join(raw_markup[0].find_all(text=True))
		return raw_text.strip()
	except IndexError:
		return None

#searches soup for tag with specific value, returns raw markup
def find_stalkee_attribute_markup(soup, tag, tag_value):
	raw_markup = soup.find_all(True, {tag:tag_value})
	try:
		return raw_markup[0]
	except IndexError:
		return None

#returns first google result of string
def google_first_result(googlestring):
	pygoog = pygoogle(googlestring)
	pygoog.pages = 1
	urls = pygoog.get_urls()
	try:		
		return urls[0]
	except IndexError:
		return "http://www.google.com"






