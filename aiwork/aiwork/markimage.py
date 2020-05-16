import cv2




def mark(images_o,images_m) :
    image_part= "static/images/"

    img = cv2.imread(image_part+images_o)
    mark_o = cv2.imread(image_part+images_m)
    test = cv2.imread(image_part+"0f9277755d2edfaea37f207af33e2782.jpg")
    mark_gray = cv2.cvtColor(mark_o,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(mark_gray, 50, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    img1_bg = cv2.bitwise_not(img,img,mask = mask)
    img1_bB = cv2.bitwise_or(img,img,mask = mask)

   
    
    cv2.imshow('image', img1_bB) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__=='__main__':
    mark("02.jpg","mark.jpg")