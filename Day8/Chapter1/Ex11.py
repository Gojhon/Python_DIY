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
body_tag=bs.find('body')
print(body_tag)

for child in body_tag.children:
    print(child)

img_tag=bs.find("img")
print(img_tag.parent)