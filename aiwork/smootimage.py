import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import unsharp_mask
from skimage import io



def smoot(img) :
    
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    unsharp(dst)

def unsharp(dst) :   
    filename = 'static/image/savedImage.jpg'
    result_1 = unsharp_mask(dst, radius=1, amount=1)
    result_2 = unsharp_mask(dst, radius=5, amount=1)
    result_3 = unsharp_mask(dst, radius=10, amount=1)
    result_4 = unsharp_mask(dst, radius=15, amount=1)
    result_5 = unsharp_mask(dst, radius=20, amount=1)  
    io.imsave(filename.replace('.jpg', '_1.jpg'), result_1) 
    io.imsave(filename.replace('.jpg', '_2.jpg'), result_2) 
    io.imsave(filename.replace('.jpg', '_3.jpg'), result_3) 
    io.imsave(filename.replace('.jpg', '_4.jpg'), result_4) 
    io.imsave(filename.replace('.jpg', '_5.jpg'), result_5) 
    




