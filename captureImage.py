import cv2;
import datetime;

cap=cv2.VideoCapture(0)
img_count=1
while True:
    ret, frame1=cap.read()
    if not ret:
        print('Failed!')
        break
    cv2.imshow('img',frame1)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key%265==32:
        img_name="myImage_{}.png".format(img_count)
        cv2.imwrite(img_name,frame1)
        print("SS taken")
        
        break
cap.release()