import facebook

obj=facebook.GraphAPI(access_token="EAACEdEose0cBAEvAP7gJBmYSpilMwK6GZBw34MvZB5ZAUqATYfUVtsZCnSBpHLNJ7MkJqqc9iAhjZBhqeQrcruc1NOxLh9cN0tItjUk8BU06G93YzeZAtH8WgmZAflabDcEwikwVp7tHOecjcf9WxYrAcumVVt90ZA0mHjlmy21ANQZDZD")
limit=int(input("몇건의 게시물을 검색할까요?"))
response=obj.get_connections(id="me",connection_name="posts",limit=limit)

for data in response[u"data"]:
    print("=="*30+"\n")
    print("게시물 작성자"+data[u"form"][u"name"].encode("utf-8")+"\n")
    print("게시물 아이디"+data[u"form"][u"name"].encode("utf-8")+"\n")
    print("최종 업데이트 시간"+data[u"form"][u"name"].encode("utf-8")+"\n")
    print("게시물 링크"+data[u"form"][u"name"].encode("utf-8")+"\n")