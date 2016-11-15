import urllib.request

req=urllib.request
d=req.urlopen("https://wikidocs.net/")
status=d.getheaders()
for s in status:
    print(s)