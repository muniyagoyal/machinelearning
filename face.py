#!/usr/bin/env python3

import  cv2
import numpy as np
cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


#img=cv2.imread('banjovi.jpg')
while cap.isOpened():
	status,frame=cap.read()
	grayimg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg,1.15,5)  
	for  (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) 
		fo_gray=grayimg[y:y+h,x:x+w]
		fo_color=frame[y:y+h,x:x+w]
	cv2.imshow('Detect',frame)
	#cv2.imshow('Gray',fo_gray)
	#cv2.imshow('FaceOnly',fo_color)
	if cv2.waitKey(30) & 0xff ==ord('q'):
		break		

cv2.destroyAllWindows()
cap.release()
"""
cv2.imshow('gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
