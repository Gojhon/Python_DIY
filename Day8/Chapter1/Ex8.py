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
strings=body_tag.strings
for string in strings:
    print(string)

print(body_tag.get_text())