from bs4 import BeautifulSoup
import requests
from requests.compat import urljoin

base_url = "http://www.saramin.co.kr/zf_user/upjikjong-recruit/upjikjong-list/recruitform_type/classified/categoryCode/9%7C4/code/407/category_level/sub"
header = {'User-Agent': 'Mozilla/5.0'}
r = requests.post(base_url,headers=header)
r.encoding = "utf-8"

bs4_saramin = BeautifulSoup(r.text,"html.parser")
find_mytr = bs4_saramin.find_all("tr",attrs={'class':"position-detail"})
for t in find_mytr:
    try:
        print(t.find('td',attrs={'class':'company_name'}).get_text())
        print("지역 : {}".format(t.find('td',attrs={'class':'first'}).get_text()))
        print("url : {}".format(urljoin(base_url,t.find('td',attrs={'post_subject'}).a.get('href'))))
        print("경력 : {}".format(t.find('td',attrs={'class' : 'post_name'}).get_text()))
    except AttributeError:
        continue