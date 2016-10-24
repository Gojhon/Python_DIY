from bs4 import BeautifulSoup
import requests
import csv

from requests.compat import urljoin

base_url = "http://www.clien.net/cs2/bbs/board.php?bo_table=jirum"
header = {'User-Agent': 'Mozilla/5.0'}
r = requests.post(base_url,headers=header)
r.encoding = "utf-8"

bs4_clien = BeautifulSoup(r.text,"html.parser")
find_mytr = bs4_clien.find_all("tr",attrs={'class':"mytr"})

for t in find_mytr:
    try:
        print(t.find('td',attrs={'class':'post_category'}).get_text())
        print("제목 : {}".format(t.find('td',attrs={'class':'post_subject'}).get_text()))
        print("url : {}".format(urljoin(base_url,t.find('td',attrs={'post_subject'}).a.get('href'))))
        print("글쓴이 : {}".format(t.find('td',attrs={'class' : 'post_name'}).get_text()))
        catregory = t.find('td', attrs={'class': 'post_category'}).get_text()
        post_subject = "제목 : {}".format(t.find('td', attrs={'class': 'post_subject'}).get_text())
        url="url : {}".format(urljoin(base_url,t.find('td',attrs={'post_subject'}).a.get('href')))
        post_name="글쓴이 : {}".format(t.find('td',attrs={'class' : 'post_name'}).get_text())
    except AttributeError:
        continue