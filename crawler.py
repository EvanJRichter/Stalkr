import unirest
import requests
from person import Person
from pygoogle import pygoogle
from bs4 import BeautifulSoup

#takes a name and a location, googles for that, gets information from the first result.
def linkedin_stalk(name, location):
	stalkee = Person()

	googlestring = name.replace(" ", "+") + "+" + location + "+linkedin" 
	url = google_first_result(googlestring)

	#if the google search does not return a linkedin profile
	if "vsearch" in url:
		return stalkee

	#get data not logged in
	result = unirest.get(url).body
	anonymous_soup = BeautifulSoup(result)
	stalkee = linkedin_retrieve_data(anonymous_soup, stalkee)

	#log into linkedin to get more information, since it may differ
	client = login_linkedin();
	logged_in_page = client.get(url)
	logged_in_soup = BeautifulSoup(logged_in_page.text)
	stalkee = linkedin_retrieve_data(logged_in_soup, stalkee)

	return stalkee

#retrieve stalkee attributes from soup
def linkedin_retrieve_data(soup, stalkee):
	nametemp = find_stalkee_attribute_text(soup, "id", "name-container")
	if nametemp:
		stalkee.name = nametemp

	positiontemp = find_stalkee_attribute_text(soup, "class", "title")
	if positiontemp:
		stalkee.position = positiontemp

	imagetemp = find_stalkee_attribute_markup(soup, "alt", stalkee.name)
	if imagetemp:
		stalkee.image = imagetemp

	locationtemp = find_stalkee_attribute_text(soup, "class", "locality")
	if locationtemp:
		stalkee.location = locationtemp

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

def facebook_stalk(name, location):
	url = "facebook.com/public/"
	url = url + name + location
	results = unirest.get(url).body
	resultssoup = BeautifulSoup(result)




