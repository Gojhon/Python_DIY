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
head_tag=bs.find('head')
print(head_tag)
print(head_tag.find('title'))
print(head_tag.find('p'))
