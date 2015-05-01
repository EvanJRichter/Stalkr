import os
import hello
import crawler
from person import Person
from pygoogle import pygoogle

import unittest
import tempfile

class HelloTestCase(unittest.TestCase):

	def setUp(self):
		hello.app.config['TESTING'] = True
		self.app = hello.app.test_client()


	def tearDown(self):
		print "finishing..."
        #os.close(self.db_fd)
        #os.unlink(hello.app.config['DATABASE'])

	def test_google_first_result(self):
		pygoog = pygoogle("hello world")
		pygoog.pages = 1
		urls = pygoog.get_urls()
		print urls[0]
		assert urls[0] == "http://en.wikipedia.org/wiki/\"Hello,_World!\"_program"

	def test_linkedin_stalk_name(self):
		stalkee = crawler.linkedin_stalk("Colton Cannon", "Champaign")
		assert stalkee.name == "Colton Cannon"

	def test_linkedin_stalk_position(self):
		stalkee = crawler.linkedin_stalk("Colton Cannon", "Champaign")
		assert stalkee.position == "Student at University of Illinois at Urbana-Champaign"

	def test_create_person(self):
		person = Person()
		assert person != None

	def test_person_defaults(self):
		person = Person()
		assert person.name == "John Doe"

	def test_person_name(self):
		person = Person(name = "Stephen Herring")
		assert person.name == "Stephen Herring"

	



if __name__ == '__main__':
	unittest.main()



















