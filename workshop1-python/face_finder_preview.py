import numpy as np
import cv2 as cv
rectangles = False
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
smile_cascade = cv.CascadeClassifier("haarcascade_smile.xml")
nose_cascade = cv.CascadeClassifier("haarcascade_mcs_nose.xml")
#smiley = cv.imread("smiley.jpg")
catnose = cv.imread("catnose.jpg")
print catnose.shape, catnose.shape[0], catnose.shape[1]
img = cv.imread(raw_input("Picture: "))
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey, 1.3, 5)
for (x,y,w,h) in faces:
    if rectangles:
        cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    roi_gray = grey[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        if rectangles:
            cv.rectangle(roi_color, (ex-10,ey-10), (ex-10+ew,ey-10), (0,0,0), 2)
            cv.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    smiles = smile_cascade.detectMultiScale(roi_gray)
    for (sx,sy,sw,sh) in smiles:
        if rectangles:
            cv.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (0,0,255), 2)
        #cv.addWeighted(smiley, 1, roi_color, 0, 0, roi_color)
        #ss = smiley.shape
        #`img[sy:sy+ss[0], sx:sx+ss[0]] = cv.addWeighted(smiley, 1, img[sy:sy+ss[0], sx:sx+ss[0]], 1, 0)
        break # Only one smile per face.
    noses = nose_cascade.detectMultiScale(roi_gray)
    for (nx,ny,nw,nh) in noses:
        print nx,ny,nw,nh
        if rectangles:
            cv.rectangle(roi_color, (nx,ny), (nx+nw,ny+nh), (255,255,0), 2)
        # Move the nose a little so that it is centered onto the nose.
        cn = catnose.shape
        print cn
        fx = y+ny-(cn[0]/2)#-(w/2)-(cn[0]/2)
        fx2 = y+ny+nw+(cn[0]/2)#-(w/2)+(cn[0]/2)
        fy = x+nx-(cn[0]/2)#-(h/2)-(cn[1]/2)
        fy2 = x+nx+nh+(cn[0]/2)#-(h/2)+(cn[1]/2)
        fx = max([0,fx])
        fx2 = max([0,fx2])
        fy = max([0,fy])
        fy2 = max([0,fy2])
        sl = img[fx:fx2, fy:fy2]
        #cv.imshow("img", sl)
        #cv.waitKey(0)
        print sl.shape
        # Slice out 
        nn = cv.resize(catnose, (sl.shape[1], sl.shape[0]))
        print nn.shape
        #cv.imshow("img", nn)
        #cv.waitKey(0)
        img[fx:fx2, fy:fy2] = cv.addWeighted(nn, 1, sl, 1, 0)
        break # Only one nose per face.
#nsm = cv.resize(smiley, img.shape[:-1])
#img = cv.addWeighted(img, 0., nsm, 1., 0.)
cv.imshow("img", img)
cv.waitKey(0)

cv.destroyAllWindows()
