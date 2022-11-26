import cv2

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while (True) :
    ret, frame = vid.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detect the faces
    faces = face_cascade.detectMultiScale(grey, 1.1, 4)
    
    #Draw the rectangle arond the face
    for (x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow('Webcam', frame)


    if cv2.waitKey(25) == 32 :
        break

vid.release()
cv2.destroyAllWindows()