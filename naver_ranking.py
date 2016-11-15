import  requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page=1
    while page<=max_pages:
        url="http://www.naver.com"
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html")

        ranks=soup.find("div",{"class":"rankup"})
        print("네이버 검색 순위 ")
        for rk,keywords in zip( range(1,11),ranks.findAll("li") ):
            print(str(rk)+". "+keywords.a['title'])
        page+=1

spider(1)
