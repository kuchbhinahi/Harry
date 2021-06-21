import cv2
#webcam
cap = cv2.VideoCapture(0)


while cap.isOpened(): #webcam is opem then
    ret, back = cap.read() #reading webcam
    if ret == True:
        cv2.imshow("image", back)
        if cv2.waitKey(100) == ord('z'):
            cv2.imwrite('image.jpg', back)
            break
cap.release()
cv2.distroyAllWindows()

