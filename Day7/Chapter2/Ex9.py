jhon_image=open("C:\\Users\\Jhon\\Pictures\\이력서.jpg","rb")
jhon_image2=open("C:\\Users\\Jhon\\Pictures\\이력서2.jpg","wb")
jhon_image2.write(jhon_image.read())
jhon_image.close()
jhon_image2.close()