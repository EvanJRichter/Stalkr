import unirest
from pygoogle import pygoogle
from bs4 import BeautifulSoup

#takes a name and a location, googles for that, gets information from the first result.
def linkedin_stalk(name, location):
	# search google for name + location + linkedin
	# get first result
	# soup 
	googlestring = name.replace(" ", "+") + "+" + location + "+linkedin" 
	print "googling this: " + googlestring
	pygoog = pygoogle(googlestring)
	pygoog.pages = 1
	urls = pygoog.get_urls()

	for url in urls:
		print url

	#beautiful soupify the first result
	result = unirest.get(urls[0]).body
	soup = BeautifulSoup(result)

	#look for cover photo
	name = soup.findAll(True, {"data-li-template":"p2_basic_info"})

	nametext = ''.join(name[0].findAll(text=True))
	return nametext.strip()

def facebook_stalk(name, location):
	url = "facebook.com/public/"
	url = url + name + location
	results = unirest.get(url).body
	resultssoup = BeautifulSoup(result)

	






#linkedin profile
# get https://www.linkedin.com/pub/dir/Firstname/Lastname
