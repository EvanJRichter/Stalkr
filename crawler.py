import unirest
from person import Person
from pygoogle import pygoogle
from bs4 import BeautifulSoup

#takes a name and a location, googles for that, gets information from the first result.
def linkedin_stalk(name, location):
	stalkee = Person()

	googlestring = name.replace(" ", "+") + "+" + location + "+linkedin" 
	url = google_first_result(googlestring)

	#beautiful soupify the first result
	result = unirest.get(url).body
	soup = BeautifulSoup(result)

	#look for header information
	"""
	profile_info_raw = soup.find_all(True, {"data-li-template":"p2_basic_info"})
	try:
		profile_info_text = ''.join(profile_info_raw[0].find_all(text=True))
		profile_info = profile_info_text.strip()
		total_info.append(profile_info)
	except IndexError:
		total_info.append("Couldn't find information...")
	"""

	#look for name information
	profile_name_raw = soup.find_all(True, {"id":"name-container"})
	try:
		profile_name_text = ''.join(profile_name_raw[0].find_all(text=True))
		stalkee.name = profile_name_text.strip()
	except IndexError:
		stalkee.name = "Couldn't find name..."

	#look for position information
	profile_position_raw = soup.find_all(True, {"class":"title"})
	try:
		profile_position_text = ''.join(profile_position_raw[0].find_all(text=True))
		stalkee.position = profile_position_text.strip()
	except IndexError:
		stalkee.name = "Couldn't find position..."


	#TODO: Location, industry


	#get picture
	profile_pic_raw = soup.find_all(True, {"alt":stalkee.name})
	try:
		stalkee.image = profile_pic_raw[0]
	except IndexError:
		stalkee.image = "Couldn't find image..."

	return stalkee

#returns first google result of string
def google_first_result(googlestring):
	pygoog = pygoogle(googlestring)
	pygoog.pages = 1
	urls = pygoog.get_urls()
	return urls[0]



