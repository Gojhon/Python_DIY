from bs4 import BeautifulSoup
html='''
<html>
    <head>
        <title> test web</title>
    </head>
    <body>
        <p align="center">text cpmtemts </p>
        <img src="C:\\python32\\koala.jpg" width="500" height="300">
    </body>
</html>
'''
bs=BeautifulSoup(html)
print(bs.prettify())

print(bs.find('p'))
print(bs.find('a'))