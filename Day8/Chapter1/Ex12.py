from bs4 import BeautifulSoup
html='''
<html>
    <head>
        <title>test web</title>
    </head>
    <body>
        <p class="ptag black"  align="center"> text contents1</p>
        <p class="ptag yellow" align="center"> text contents2</p>
        <p class="ptag red"    align="center"> text contents3</p>
        <img src="C:\\Python34\\Koala.jpg" width="500" height="300">
    </body>
</html>
'''
bs=BeautifulSoup(html)
p_tag=bs.find('p')
print(p_tag)
print(p_tag.find_parent('body'))
title_tag=bs.find('title')
print(title_tag)
print(title_tag.find_parent('head'))
