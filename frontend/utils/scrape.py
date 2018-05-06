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
        self.imageurl=""
        self.body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eleifend nisl pellentesque diam dictum varius. Vivamus scelerisque porttitor magna sed tristique. Sed id magna suscipit, iaculis nulla aliquam, pretium augue. Pellentesque ac quam et est rhoncus scelerisque. Nullam quis libero non nibh hendrerit sagittis. Sed id placerat ipsum, a pellentesque mi. Donec facilisis urna et tincidunt ornare. Morbi arcu ex, volutpat non finibus eu, tincidunt ac neque. Praesent interdum vehicula est, sit amet interdum quam tempus sit amet. Pellentesque lorem justo, bibendum tempor ante in, rutrum facilisis eros. Curabitur scelerisque, metus et congue rhoncus, justo lorem finibus diam, sit amet mattis augue augue eu lectus. Nam mattis massa ac venenatis tempus. Nullam mauris urna, tempus ut tincidunt non, consequat non ante. Curabitur rutrum malesuada lorem, id rutrum elit consectetur id. Nunc at blandit nibh. Praesent ut libero placerat nibh eleifend sollicitudin. Quisque ligula velit, vulputate non libero id, tincidunt tincidunt ligula. Vivamus feugiat tincidunt enim, eget facilisis dolor tincidunt a. Donec neque turpis, consequat eu porta sit amet, maximus et tortor. Vivamus vestibulum sodales eros, in scelerisque felis finibus sit amet. Vivamus sodales, nulla ac scelerisque finibus, mauris dolor varius eros, at vehicula nulla elit ut turpis. Sed rutrum nunc at odio luctus porta. Aliquam quam elit, congue ac risus a, consectetur facilisis neque. Cras lacinia diam eget mi laoreet, ac lacinia tellus faucibus."

    def article_contents(self):
        # use goose3 or beautifulsoup API here
        article = {'header':self.header, 'body':self.body, 'imageurl':self.imageurl}
        return article