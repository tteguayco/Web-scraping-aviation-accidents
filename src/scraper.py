import urllib2
import re
from bs4 import BeautifulSoup

class AccidentsScraper():

	def __init__(self):
		self.url = "http://www.planecrashinfo.com"
		self.subdomain = "/database.htm"
		self.data = []

	def __download_html(self, url):
		response = urllib2.urlopen(url)
		html = response.read()
		return html

	def __get_accidents_links(self, html):
		bs = BeautifulSoup(html, 'html.parser')
		tds = bs.findAll('td')
		accidents_links = []
		for td in tds:
			# Has this <td> element an <a> child?
			a = td.next_element.next_element
			if a.name == 'a':
				href = a['href']
				# Preppend '/' if needed
				if href[0] != '/':
					href = '/' + href
				accidents_links.append(href)

		return accidents_links

	def __scrape_variables_names(self, html):
		pass

	def __scrape_example_data(self, html):
		pass

	def __get_years_links(self, html):
		bs = BeautifulSoup(html, 'html.parser')
		anchors = bs.findAll('a', href=True)
		years_links = []
		for a in anchors:
			# Match a year from 1900 to 2099
			if re.match("(19|20)[0-9][0-9]", a.text.strip()):
				href = a['href']
				# Preppend '/' if needed
				if href[0] != '/':
					href = '/' + href
				years_links.append(href)

		return years_links

	def scrape(self):
		print "Web Scraping of planes' crushes data from " + \
			"'" + self.url + "'..."

		# Download HTML
		html = self.__download_html(self.url + self.subdomain)
		bs = BeautifulSoup(html, 'html.parser')

		# Get the links of each year
		years_links = self.__get_years_links(html)

		# For each year, get its accidents' links
		accidents_links = []
		for y in years_links:
			print self.url + y
			html = self.__download_html(self.url + y)
			current_year_accidents = self.__get_accidents_links(html)
			accidents_links.append(current_year_accidents)

		print accidents_links

	def data2csv(self, filename):
		# Write to the specified file.
		# Create it if it does not exist.
		file = open("../csv/" + filename, "w+")

		# Dump all the data with CSV format
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				file.write(self.data[i][j] + ",");
			file.write("\n");
