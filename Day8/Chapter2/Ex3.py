import urllib.request
from bs4 import BeautifulSoup
import re

list_url="http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
detail_url="http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"


def fetch_list_url():
   request_header=urllib.parse.urlencode({"page":"1"})
   #인코딩된 문자열의 형태로 변환해서 변수에 저장하는 역할을 합니다.
   request_header=request_header.encode("utf-8")
   #변수에 저장된 파라미터를 utf-8로 변환하비다.
   url=urllib.request.Request(list_url,request_header)
    #응답소의 민원 리스트 페이지에 파라미터를 전달합니다.
   res=urllib.request.urlopen(url).read().decode("utf-8")
    #리스트 페이지를 불러서 UTF-8형식으로 변환한다.
   bs=BeautifulSoup(res,"html.parser")
   #리스트 페이지를 Beautiful Soup 객체에 넣어서 필터링할  준비를 합니다.
   listbox=bs.find_all("li",class_="pclist_list_tit2")
   #응답소 리스트에는 민원의 제목에 파라미터로 쓰일 값이 존재합니다. 그 ㅐ그가 li태그 안에 있으므로
   #태그를 모두가져옵니다.
   params=[] #파라미터를 저장할 리스트를 생성합니다.
   for i in listbox:
       params.append(re.search("[0-9]{14}",i.find("a")["href"]).group())
        #for문을 이용해서 li태그 안에 이는 파라미터를 정규식으로 뽑아내서 리스트에 추가시키비다.
   return params #파라미터가 저장된 리스트를 반환합니다

def fetch_detail_url():#a민원의 내용이 들어 있는 페이지를 열어서 민원의 내용을 가져오기 위한 함수입니다.
    params =fetch_list_url() #fetch_list_url함수를 실행해서 파라미터를 얻어 변수에 저장
    for p in params:# 파라미터를 이용해서 for 문을 실행 시킵니다.
        request_header=urllib.parse.urlencode({"RCEPT_NO":str(p)}) # 민원페이지를 얻기위한 파라미터를 인코딩시켜 저장합니다.
        request_header=request_header.encode("utf-8")#헤더를 utf-8로 저장합니다.
        url=urllib.request.Request(detail_url,request_header)#민원 내용 페이지를 열어서 데이터를 읽어옵니다.
        res=urllib.request.urlopen(url).read().decode("utf-8") # 민원데이터를 열어서 가져옵니다.
        bs=BeautifulSoup(res,"html.parser") #읽어 들인 데이터를 뷰티풀 ㅜ프 객체로 생성하여 필터링할 준비를 합니다.
        div=bs.find("div",class_="form_table") # 민원 내용이 적혀있는 div태그를 가져옵니다.
        tables=div.find_all("table")#div태그 안에 table 태그로 내용이 분류되어있습니다. div태그안에 존재하는 모든 table태그를 가져옵니다.
        info=tables[0].find_all("td")#첫번째 td 태그는 민원 제목이 있습니다. td 태그의 텍스트를 공백을 제거하여 가져옵니다.
        title=info[0].get_text(strip=True) #첫번째 td태그는 민원 제목이 있습니다. td 태그의 텍스트를 공백을 제거하여 가져옵니다.
        date=info[1].get_text(strip=True)   #두번째 td태는 날짜가 있습니다. td태그의 텍스트공 백을 제거하여 가져옵니다.
        question=tables[1].find("div",class_="table_inner_desc").get_text(strip=True)
        #두번째 table 태그에는 민원의 내용이 있습니다. table태그에서 div 태그에는 div태그를 찾아와 공백을 제거하고 텍스트를 가져옵니다.
        answer=tables[2].find("div",class_="table_inner_desc").get_text(strip=True)
        #세번째 table 태그에는 민원에 대한 답변이 있습니다. table태그에서 di태그를 찾아와 공백을 제거하고 텍스트를 가져옵니다.
        print("=="*30+"\n")#출력구문
        print(title + "\n")
        print(date+"\n")
        print(question+"\n")
        print(answer+"\n")
        print("==" * 30 + "\n")

fetch_detail_url() #fetch deatil_url함수를 실행합니다.