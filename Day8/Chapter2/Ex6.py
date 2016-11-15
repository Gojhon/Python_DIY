import urllib.request
from bs4 import BeautifulSoup
target_url='http://52.68.130.249/textboard'

def fetch_post_list():
    URL=target_url
    res=urllib.request.urlopen(URL)
    html=res.read()
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find('table',class_='kingkongboard-table')
    title_list=table.find_all('td',class_='kingkongboard-list-title')
    links=[]
    links=[td.find('a')['href']for td in title_list]
    return links

def fetch_post_contents(link):
    URL=link
    res=urllib.request.urlopen(URL)
    html=res.read()
    soup=BeautifulSoup(html,'html.parser')
    content_table = soup.find('div', id="kingkongboard-read-table")

    title_section=content_table.find('div',class_='title-section')
    title=title_section.find('h1').text
    date=title_section.find('div',class_='regist-date').find('h2').text

    writer=content_table.find('div',class_='regist-writer').find('h2').text
    content=content_table.find('div',class_='content-section').find('p').text

    return {
        'title':title,
        'date':date,
        'writer':writer,
        'content':content
    }

links=fetch_post_list()
for link in links:
    result=fetch_post_contents(link)
    print(result)