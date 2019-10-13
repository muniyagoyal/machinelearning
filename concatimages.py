#!usr/bin/env python3
import cv2
import numpy as np
picture=cv2.imread('iron.jpeg',1)
#gray_pic=cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)

i1=cv2.resize(picture,(600,450))
i2=cv2.resize(picture,(600,450))
print(i2.shape,i1.shape)

    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arange(N))
        colors = cmap[::-1,:].tolist()
    if isinstance(colors, list): 
        if len(colors) == N:
            colors = colors[::-1]
        else: 
            raise Exception("\n\nnumber of colors {} not equal \
            to number of categories{}\n".format(len(colors), N))

nhorizontal=np.hstack((i1,i2))
cv2.imshow("combined",nhorizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

