# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify url
quote_page = ‘https://www.nytimes.com/2018/05/05/business/dealbook/berkshire-hathaway-annual-meeting-stock.html?rref=collection%2Fsectioncollection%2Fbusiness&action=click&contentCollection=business&region=rank&module=package&version=highlights&contentPlacement=1&pgtype=sectionfront'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)

# Take out the <div> of name and get its value
name_box = soup.find(‘h1’, attrs={‘class’: headline})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name