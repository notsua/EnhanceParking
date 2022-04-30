import cv2
import numpy as np
import pickle
import cvzone
import mongodb
w ,h= 55 ,65
spcount = 0
ccount = 0
#video feed
cap = cv2.VideoCapture('parking_lot_1.mp4')

def carpakingspaces(im):
    for pos in poslist:
        global spcount , ccount
        x , y = pos
        imgcrop = im[y:y+h,x:x+w]
        cv2.imshow(str(x+y),imgcrop)
        count = cv2.countNonZero(imgcrop)
        cvzone.putTextRect(img,str(count),(x,y+h-3),scale = 1,thickness=1,offset=0)
        if count < 200:
            color  = (0,255,0)
            spcount += 1
        else:
            color = (0,0,255)

        cv2.rectangle(img , pos , (pos[0]+w,pos[1]+h),color , 2)
    cvzone.putTextRect(img,str('freespace'+str(spcount)),(100,50),scale = 3,thickness=5,offset=20 , colorR=(0,255,0))
    if ccount == 50:
        mongodb.update_values('13.139268348118557,77.6261566464334',spcount)
        ccount = 0
    spcount = 0

with open('carpositions' , 'rb') as f:
    poslist = pickle.load(f)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES , 1)
    sucess , img = cap.read()
    imggrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggrey,(3,3),4)
    imgthreshold = cv2.adaptiveThreshold(imgblur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25 , 16)
    imgmeadian = cv2.medianBlur(imgthreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgdialate = cv2.dilate(imgmeadian,kernel, iterations=1)
    carpakingspaces(imgdialate)
    cv2.imshow('Image',img)
    ccount +=1
    if ccount == 50:
        mongodb.update_values('13.139268348118557,77.6261566464334',str(spcount))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('new3',imgblur)
    cv2.imshow('new',imgmeadian)
    cv2.waitKey(15)