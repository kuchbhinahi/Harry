import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True: # how do we convert rgb to hsv?
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)
        green_1 = np.uint8([[[0,255,0]]])
        hsv_green = cv2.cvtColor(green_1, cv2.COLOR_BGR2HSV)
        #print(hsv_green)

        l_green = np.array([0, 100, 100])
        u_green = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_green, u_green)
        #cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        #cv2.imshow("part1", part1)
        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("cloak", part1 + part2)

    if cv2.waitKey(5) == ord('z'):
        break

cap.release()
cv2.distroyAllWindows()
        