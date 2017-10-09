import urllib2
import re
from bs4 import BeautifulSoup

class AccidentsScraper():

	def __init__(self):
		self.url = "https://aviation-safety.net/database/"
		self.data = []

	def scrape(self):
		# Download HTML
		response = urllib2.urlopen(self.url)
		html = response.read()
		bs = BeautifulSoup(html, 'html.parser')

		# Get the links for each year
		anchors = bs.findAll('a', href=True)
		years_links = []
		for a in anchors:
			# Match a year from 1900 to 2099
			if re.match("(19|20)[0-9][0-9]", a.text):
				years_links.append(a['href'])

		print years_links

	def data2csv(self, output_file):
		pass
