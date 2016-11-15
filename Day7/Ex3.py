import urllib.request

req=urllib.request
d=req.urlopen("http://www.youtube.com/")
status=d.getheaders()
for s in status:
    print(s)
