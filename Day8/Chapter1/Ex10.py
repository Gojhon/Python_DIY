from bs4 import BeautifulSoup
import re
html="""
<html>
    <head>
        <title>test web</title>
    </haed>
    <body>
        <p class = "ptag black" align="center">text contents 1 </p>
        <p class = "ptag yello" aalign="center">text contents 2 </p>
        <p class = "ptag red" aalign="center">text contents 3</p>
    <img src="C:\\python\\Koala.jpg" width="500" height="300">
    </body>
</html>
"""
bs=BeautifulSoup(html)
p_tag=bs.find('p')
print(p_tag['class'])
p_tag['class'][1]="white"
print(p_tag['class'])
p_tag['id']='P-TAG'
print(p_tag['id'])
print('align')
del p_tag['align']
print(p_tag.attrs)
