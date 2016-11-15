import urllib.parse

def input_query():
    q=str(input("검색어를 입력하세요.:"))
    return "&query="+q

def input_query_plus():
    q=urllib.parse.quote_plus(input("검색어를 입력하세요.:"))
    return "&query="+q

print(input_query())
print(input_query_plus())


