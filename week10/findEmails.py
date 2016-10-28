import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

def main(args):
	# Get Webpage
	originalWebsite = str(input('What website do you want to search for email adresses for?'))
	levelDeep = int(input('How many levels deep in ' + originalWebsite + ' do you want to go?'))
	
	# Get First Batch of Links and Emails
	websiteSoup = getWebsite(originalWebsite)
	text = getText(websiteSoup)
	originalLinks = getLinks(originalWebsite, websiteSoup)
	links = originalLinks
	emails = getEmails(text)
	
	# How deep do you go
	for level in range(1,levelDeep):
		for url in links:
			websiteSoup = getWebsite(url)
			tempText = getText(websiteSoup)
			links = links + getLinks(url, websiteSoup)
			emails = emails + getEmails(tempText)
			
	print('Emails:', emails)

def getWebsite(website):
	# get website
	response = requests.get(website)
	response.raise_for_status()
	
	soup = BeautifulSoup(response.text, "html.parser")
	
	return soup

def getText(soup):
	# get text of website
	words = soup.get_text()
	
	return words

def getEmails(words):
	# get email adresses
	emails = re.findall(r'[\w\.-]+@[\w\.-]+', words)
	
	return emails
	
def getLinks(website, soup):
	# get links
	aTags = soup.select('a')
	links = [a.get('href') for a in aTags]
	
	# remove non links
	links = [link for link in links if link is not None]
	links = [link for link in links if 'javascript' not in link]
	
	# make some links absolute
	unabsoluteLinks = [urllib.parse.urljoin(website, link) for link in links if 'http' not in link]
	
	# remove unabsolute links
	removeablelinks = [link for link in links if 'http' not in link]
	links = [goodLink for goodLink in links if goodLink not in removeablelinks]
	
	# add remaining links to absolute links
	links = links + unabsoluteLinks
	
	# filter links to target website
	links = [localLink for localLink in links if website in localLink]
	
	return links

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
