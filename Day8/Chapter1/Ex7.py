from bs4 import BeautifulSoup
import re
html="""
<html>
    <head>
        <title>test web</title>
    </haed>
    <body>
        <p align="center">text contents 1 </p>
        <p align="center">text contents 2 </p>
        <p align="center">text contents 3</p>
    <img src="C:\\python\\Koala.jpg" width="500" height="300">
    </body>
</html>
"""
bs=BeautifulSoup(html)
body_tag=bs.find('body')
p_tag=body_tag.find('p')
print(body_tag.find('p'))
print(p_tag.string)