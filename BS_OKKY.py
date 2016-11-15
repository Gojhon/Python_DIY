from bs4 import BeautifulSoup
import  requests
from  datetime import datetime

now=datetime.now()
file_path=datetime.strftime(now,"%Y-%m-%d_%H_%M_%S.text")
file_pathtest="test.text"
url="http://okky.kr/articles/questions"

response=requests.get(url)

f=open(file_path,'w',encoding="utf-8")
data=''
soup=BeautifulSoup(response.text,'html.parser')
list=soup.select("li.list-group-item")
for li in list:
    a=li.find('h5').find('a')
    link=a['href']
    list_id=link.split('/')[-1]
    title=a.text.strip()
    data+="id :%s title: %s \n"%(list_id,title)
    print(title)
    f.write(data)

f.close()
