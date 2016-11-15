from bs4 import BeautifulSoup
html="""
<html>
    <head>
        <title>test web</title>
    </haed>
    <body>
        <p align="center">text contents 1 </p>
        <p align="right">text contents 2 </p>
        <p align="left">text contents 3</p>
    <img src="C:\\python\\Koala.jpg" width="500" height="300">
    </body>
</html>
"""
bs=BeautifulSoup(html)

body_tag=bs.find('body')
list1=body_tag.find_all(['p','img'])

for tag in list1:
    print(tag)

print(bs.find_all('p'))