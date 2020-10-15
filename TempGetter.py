'''
this aplication is used to scrape the web for my local temperature
'''

import requests
webPage = requests.get("https://weather.com/weather/today/l/cf78a7f7f03c6d6761310a3c4b8b450e9f1cb02c9dec7643e7029ab521d654fe")



from bs4 import BeautifulSoup


page = BeautifulSoup(webPage, 'html.parser')

print(page.head)