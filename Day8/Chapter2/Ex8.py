import re
import urllib.request

fileNum = 0
todayHumorUrl = 'http://humor.oceanmate.co.kr/bbs/board.php?bo_table=humor&wr_id='
for postNo in range(2100, 2200):
   url = todayHumorUrl + str(postNo)
   f = urllib.request.urlopen(url)
   html = f.read()
   imageUrls = re.findall("http://humor.oceanmate.co.kr/fun_img/[^\"\s>]+",str(html))
   for url in imageUrls:
        contents = urllib.request.urlopen(url)
        file = open("C:\\Users\\Jhon\\Pictures\\Screenshots" + str(fileNum) + '.jpg' , 'wb')
        file.write(contents.read())
        file.close()
        fileNum += 1