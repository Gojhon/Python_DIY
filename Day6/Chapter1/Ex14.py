import re
print(re.search("\d+","고요한는 1987년에 태어 났습니다."))
print(re.match("\d+","고요한는 1987년에 태어 났습니다."))
print(re.match("\d+","1987년에 고요한은 태어 났습니다."))
print(re.findall("\d+","고요한은 1987년 07월 03일입니다."))
print(re.findall("\d+","고요한은 1987년 07월 03일입니다."))
print(re.split("[:]+","Apple Orange : Grape Cherry"))
print(re.split("[: ]+","Apple Orange : Grape Cherry"))
print(re.sub("--",'**',"870703--1228311"))