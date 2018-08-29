l####################################      2.0 Image Segmentation     #########################################

import cv2                             
import numpy as np

image = cv2.imread('C:\Users\SONY\Desktop\Butterfly.jpg') 
height,width,length = image.shape


hw=height*width
a=0
flag=0
h = 60
Iter = 20
array_comb = np.zeros((hw,5))
new_image_array=np.zeros((height,width,length))

for i in range (0,height):
    for j in range (0,width):
        array_comb[a][0]=image[i][j][0]
        array_comb[a][1]=image[i][j][1]
        array_comb[a][2]=image[i][j][2]
        array_comb[a][3]=i
        array_comb[a][4]=j    
        a=a+1    
 

while array_comb.shape[0]!=0:
    if flag == 0:
        row = np.random.choice(len(array_comb))
        mean_0 = array_comb[row][0]
        mean_1 = array_comb[row][1]
        mean_2 = array_comb[row][2]
        mean_3 = array_comb[row][3]
        mean_4 = array_comb[row][4]
        
    avg1,avg2,avg3,avg4,avg5 = 0,0,0,0,0
    
    array_thres=[]
    array_index=[]        
   
        
    for i in range (0,array_comb.shape[0]):
        e1=mean_0-array_comb[i][0]
        e2=mean_1-array_comb[i][1]
        e3=mean_2-array_comb[i][2]
        e4=mean_3-array_comb[i][3]
        e5=mean_4-array_comb[i][4]

        eucl = (e1*e1+e2*e2+e3*e3+e4*e4+e5*e5)**0.5
        if eucl<=h: 
            array_thres.append(array_comb[i])
            array_index.append(i)                    

    l=len(array_thres)
    if(l>0):
        for i in range(0,l):
            avg1=(array_thres[i])[0]+avg1
            avg2=(array_thres[i])[1]+avg2
            avg3=(array_thres[i])[2]+avg3
            avg4=(array_thres[i])[3]+avg4
            avg5=(array_thres[i])[4]+avg5
        
        Avg1 = avg1/l
        Avg2 = avg2/l
        Avg3 = avg3/l
        Avg4 = avg4/l
        Avg5 = avg5/l     
        new_eucl = ((Avg1-mean_0)**2+
                    (Avg2-mean_1)**2+
                    (Avg3-mean_2)**2+
                    (Avg4-mean_3)**2+
                    (Avg5-mean_4))**0.5 
                            
    if new_eucl<=iter:
        for i in range(len(array_index)):
            row_new = int((array_thres[i])[3])
            col_new = int((array_thres[i])[4])
            new_image_array[row_new][col_new][0]  = Avg1
            new_image_array[row_new][col_new][1]  = Avg2
            new_image_array[row_new][col_new][2]  = Avg3
        array_comb=np.delete(array_comb,array_index,0) 
        flag = 0            

    else:
        flag=1
        mean_0 = Avg1
        mean_1 = Avg2
        mean_2 = Avg3
        mean_3 = Avg4
        mean_4 = Avg5
        
    
cv2.imwrite('image.jpg',new_image_array)        #######    image after segmentation  ########
           
            
     
                 
                          
                                   
                                            
                                                              
                             
    