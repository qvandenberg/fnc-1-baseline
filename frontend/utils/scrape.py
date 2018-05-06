# from goose3 import Goose

# url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'
# g = Goose()
# article = g.extract(url=url)
# print(article.title)



    
# # import libraries
# import urllib2
# from bs4 import BeautifulSoup

# class scrape():
#     def __init__(self, url):
#         self.url = url
    
#     def retrieve_article():
#         page = urllib2.urlopen(url)
#         soup = BeautifulSoup(page, ‘html.parser’)

# # specify url
# quote_page = ‘https://www.nytimes.com/2018/05/05/business/dealbook/berkshire-hathaway-annual-meeting-stock.html?rref=collection%2Fsectioncollection%2Fbusiness&action=click&contentCollection=business&region=rank&module=package&version=highlights&contentPlacement=1&pgtype=sectionfront'

# # query the website and return the html to the variable ‘page’

# # parse the html using beautiful soup and store in variable `soup`


# # Take out the <div> of name and get its value
# name_box = soup.find(‘h1’, attrs={‘class’: headline})

# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print name

class extractArticle():

    def __init__(self, url):
        self.url = url
        self.header ="sample header"
        self.body="sample body"
        self.imageurl=""

    def article_contents(self):
        article = {'header':self.header, 'body':self.body, 'imageurl':self.imageurl}
        return article