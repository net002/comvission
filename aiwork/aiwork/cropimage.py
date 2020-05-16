from PIL import Image 
import cv2



def crop(alter_image,x1,y1,x4,y4):
    image_part= "static/images/"
    alter_image = cv2.imread(image_part+alter_image)
    im1 = alter_image.crop((x1, y1, x4, y4))

    return im1