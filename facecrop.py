import cv2
import os
directory="D:/FAMILY"
f_directory="D:/INNOVATIVE"

        
def facecrop(image):
    facedata="haarcascade_frontalface_default.xml"
    cascade=cv2.cv2.CascadeClassifier(facedata)
    img=cv2.cv2.imread(image)
    print(image)
    
    try:
    
        minisize=(img.shape[1],img.shape[0])
        miniframe=cv2.cv2.resize(img,minisize)
        faces=cascade.detectMultiScale(miniframe)


        for f in faces:
            x,y,w,h=[v for v in f]
            cv2.cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            sub_face=img[y:y+h,x:x+h]
            f_name=image.split('/')
            f_name=f_name[-1]
            cv2.cv2.imwrite(f_directory+f_name,sub_face)
            print("writing "+image)
        
    except :
        pass


   





if __name__=='__main__':
    images=os.listdir(directory)
    i=0
    for img in images:
        file=directory+'/'+img
   #     print(i)
        facecrop(file)
    #    print(file)
        i=i+1

