import urllib.request
from bs4 import BeautifulSoup
target_url='http://52.68.130.249/textboard'

def fetch_post_list():
    URL=target_url
    res=urllib.request.urlopen(URL)
    html=res.read()
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find('table',class_='kingkongboard-table')
    title_list=table.find_all('td',class_='link_title_recruit')
    links=[]
    links=[td.find['href']for td in title_list]
    return links

links=fetch_post_list()
print(links)