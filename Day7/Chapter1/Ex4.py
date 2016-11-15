import urllib.request

req=urllib.request
d=req.urlopen("http://www.softlab365.com/wordpress/")
print(d.status)
print(d.read())