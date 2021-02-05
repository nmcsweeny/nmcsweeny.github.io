import bs4
from datetime import datetime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from flask import Flask, render_template, url_for



app = Flask(__name__)


my_url = 'https://en.wikipedia.org/wiki/Main_Page'
#grabbing page, html
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#soup, html parsing
page_soup = soup(page_html, 'html.parser')
div = page_soup.find('div', {'id': 'mp-otd'})
#grabs main a tags
main_tag = [[i.text for i in b.find_all('a')] for b in div.find_all('p')]
a_tag = [[i.text for i in b.find_all('li')] for b in div.find_all('ul')]
date = main_tag[0][0]
events = a_tag[0][:5]
title_tag = page_soup.title.text
current_time_tag = datetime.date(datetime.now())



posts = [
	{
		'author': title_tag,
		'title': date,
		'content':  events,
		'date': current_time_tag
	},
]




@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)
	
	
@app.route('/about')
def about():
    return render_template('about.html', title='About')
	
if __name__ == '__main__':
	app.run(debug=True)
	