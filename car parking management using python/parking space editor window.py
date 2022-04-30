import cv2
import pickle

w ,h= 55 ,65
pos = []
try:
    with open('carpositions' , 'rb') as f:
        pos = pickle.load(f)
except:
    pos = []


#function for mouse click
def mcc(events, x, y, flag, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        pos.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i , p in enumerate(pos):
            x1 , y1 = p
            if x1 < x < x1 + w and y1 < y < y1 + h:
                pos.pop(i)
    with open('carpositions' , 'wb') as f:
        pickle.dump(pos,f)

# running the code for the marking positions
while True:
    img = cv2.imread('parking_lot_1.png')
    for pp in pos:
        cv2.rectangle(img , pp , (pp[0]+w,pp[1]+h),(250 , 0,0) , 2)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',mcc)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(pos)
cv2.destroyAllWindows()