#!/usr/bin/env python3
import cv2
#image read   1       0        -1
#            colored  b&w      transparent
path=input("Enter image path:")
picture=cv2.imread(path,1)
#print(ironman.shape)
#image show


while True:
	ch=input("Enter your choice:\n1.To crop image \n2.To draw circle\n3.To draw line\n4.To draw rectangle\n5.Quit")
	if (ch=='1'):
		width=int(input("Enter width:"))
		height=int(input("Enter height:"))
		i_crop=picture[0:height,0:width]
		cv2.imshow('cropped',i_crop)
	elif (ch=='2'):
		im_circle=cv2.circle(picture,(300,500),6,(0,0,255),2)
		cv2.imshow('Circled',im_circle)
	elif (ch=='4'):
		im_rect=cv2.rectangle(picture,(250,0),(450,270),(215,70,0),4)
		cv2.imshow('rectangled',im_rect)
	elif (ch=='2'):
		im_line=cv2.line(picture,(0,0),(320,490),(0,235,0),4)		
		cv2.imshow('lined',im_line)
	elif ch==5:
		break
#cv2.imshow(picture)
cv2.waitKey(0)
cv2.destroyAllWindows()
#to save image cv2.imwrite('newHero.jpg',ironman)


