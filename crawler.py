import unirest
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

	#beautiful soupify the first result
	result = unirest.get(url).body
	soup = BeautifulSoup(result)

	#retrieve stalkee attributes from soup
	nametemp = find_stalkee_attribute_text(soup, "id", "name-container")
	if nametemp:
		stalkee.name = nametemp

	positiontemp = find_stalkee_attribute_text(soup, "class", "title")
	if positiontemp:
		stalkee.position = positiontemp

	imagetemp = find_stalkee_attribute_markup(soup, "alt", stalkee.name)
	if imagetemp:
		stalkee.image = imagetemp

	#TODO: Location, industry

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




