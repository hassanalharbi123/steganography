from stegano import *
print("hide data[1] show data[2]")
ask=input("enter the options : ")
if ask=="1":
  img=input("enter the image name : ")
  nimg=input("enter the new imagr name : ")
  data=input("enter the data : ")
  lsb.hide(img,message=data).save(nimg)
if ask=="2":
  pic=lsb.reveal(input("enter the picture name : "))
  print("the data is : "+pic)
