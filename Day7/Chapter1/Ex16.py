import os

print(os.path.split("C:\\Users\\Jhon\\Downloads\\무한도전.E466.160206.HDTV.H264.720p-WITH.mp4")) #폴더 및 파일이름
print(os.path.splitext(("C:\\Users\\Jhon\\Downloads\\무한도전.E466.160206.HDTV.H264.720p-WITH.mp4"))) #확장자

samplejoin=os.path.split("C:\\Users\\Jhon\\Downloads\\무한도전.E466.160206.HDTV.H264.720p-WITH.mp4")
print(os.path.join(samplejoin[0],samplejoin[1]))
