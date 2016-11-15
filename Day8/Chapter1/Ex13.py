from bs4 import BeautifulSoup
html='''
<html>
    <head>
        <title> test web </title>
    </head>
    <body>
        <p class="ptag black"  align="center">text contents 1 </p>
        <p class="ptag yellow" align="center">text contents 2 </p>
        <p class="ptag red"    align="center">text contents 3 </p>
        <img src="C:\\python34\\Koala.jpg" width="500" height="300">

        <div class="container">
            <p class="text"></p>
        </div>
    </body>
</html>
'''
bs=BeautifulSoup(html)
p_tag=bs.find('p',class_='text')
parents=p_tag.find_parents()
for parent in parents:
    print(parent.name)