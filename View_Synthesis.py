##############################          1.4  View Synthesis         ##################################

import cv2                             
import numpy as np

left_img = cv2.imread('C:\Users\SONY\Desktop\sview1.png')                        
right_img = cv2.imread('C:\Users\SONY\Desktop\sview5.png')
disp1_img = cv2.imread('C:\Users\SONY\Desktop\disp1.png',0)
disp5_img = cv2.imread('C:\Users\SONY\Desktop\disp5.png',0)

height, width,length=left_img.shape
array_view3_l = np.zeros((height,width,length),dtype = np.uint8)
array_view3_r = np.zeros((height,width,length),dtype = np.uint8)


for i in range (0,height):                                      
    for j in range (0,width):
        for k in range(0,length):
            n = (j-disp1_img[i][j]/2)
            m = (j+disp5_img[i][j]/2)
            array_view3_l[i][n][k] = left_img[i][j][k]
            
            if m<463:
                array_view3_r[i][m][k] = right_img[i][j][k]



for i in range (0,height):                                      
    for j in range (0,width):
        if (int(array_view3_l[i][j][0])==0 and int(array_view3_l[i][j][1])==0 and int(array_view3_l[i][j][2])==0):
            array_view3_l[i][j][0]=array_view3_r[i][j][0]
            array_view3_l[i][j][1]=array_view3_r[i][j][1]
            array_view3_l[i][j][2]=array_view3_r[i][j][2]
            
                                               
 
print (array_view3_l)                                               
cv2.imshow('view3',array_view3_l)             #######      view 3     ######## 