import  requests
from bs4 import BeautifulSoup

url="http://bbs.ruliweb.com/market/board/1020"
source_code=requests.get(url)
saramin_text = source_code.text
soup = BeautifulSoup(saramin_text, "html")

for corpname in soup.find_all("a",{"class":"deco"}):
    corpnametitle=corpname.get_text(strip=True)
    print(corpnametitle)

#corptitle=soup.find("a",{"class":"link_title_recruit"})



