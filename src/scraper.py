import urllib2
import re
from bs4 import BeautifulSoup

class AccidentsScraper():

	def __init__(self):
		self.url = "https://aviation-safety.net/database/"
		self.data = []

	def __download_html(self, url):
		response = urllib2.urlopen(url)
		html = response.read()
		return html

	def __scrape_variables(self, html):
		bs = BeautifulSoup(html, 'html.parser')
		td = bs.find('td', class_='list')
		accident_link = td.next_element.next_element['href']

		# Remove prefix '/database/'
		accident_link = accident_link.replace('/database/', '')
		print accident_link

		# Get the target fields
		fields_str = []
		html = self.__download_html(self.url + accident_link)
		bs = BeautifulSoup(html, 'html.parser')
		fields = bs.findAll('td', class_='caption')
		for field in fields:
			# Remove colon and add the name of the variable to the array
			fields_str.append(field.text.replace(':', ''))

		# Save fields
		self.data.append(fields_str)

	def scrape(self):
		# Download HTML
		html = self.__download_html(self.url)
		bs = BeautifulSoup(html, 'html.parser')

		# Get the links for each year
		anchors = bs.findAll('a', href=True)
		years_links = []
		for a in anchors:
			# Match a year from 1900 to 2099
			if re.match("(19|20)[0-9][0-9]", a.text):
				years_links.append(a['href'])

		# Get the headers of the dataset (variables' names)
		# using just the first href obtained
		first_link = self.url + years_links[0]
		print first_link
		first_link_html = self.__download_html(first_link)
		self.__scrape_variables(first_link_html)

	def data2csv(self, filename):
		# Write to the specified file.
		# Create it if it does not exist.
		file = open("../csv/" + filename, "w+")

		# Dump all the data with CSV format
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				file.write(self.data[i][j] + ",");
			file.write("\n");
