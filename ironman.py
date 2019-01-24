#!/usr/bin/env python3
import cv2
#image read   1       0        -1
#            colored  b&w      transparent
ironman=cv2.imread('iron.jpeg',1)
#image show 
cv2.imshow('hero',ironman)
cv2.waitKey(0)
cv2.destroyAllwindows()
#to save image cv2.imwrite('newHero.jpg',ironman)



