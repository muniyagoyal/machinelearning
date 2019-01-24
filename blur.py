#!/usr/bin/env python3
import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
	status,frame=cap.read()
	blur_img=cv2.blur(frame,(10,10))
	cv2.imshow('original',frame)
	cv2.imshow('blur_img',blur_img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		        break
		
cv2.destroyAllWindows()
cap.release()

