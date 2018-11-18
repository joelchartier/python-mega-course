import cv2
import time

start_time = time.time()

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("faces.png")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=20)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow("Found faces", img)
cv2.waitKey(50000)
