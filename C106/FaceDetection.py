import cv2

img = cv2.imread('boy.jpg')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Boy Image', grey)
#cv2.waitKey(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(grey)
print(faces)

for (x,y,w,h) in faces :
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
