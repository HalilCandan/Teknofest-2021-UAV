import cv2 as cv
import numpy as np
import imutils
import csv




cap=cv.VideoCapture('redtargetvideo.mp4')

count_frame = 0

with open ('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["time", "x" , "y"])

    while True:

        ignored, frame = cap.read(0)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_range = np.array([150, 100, 100])
        upper_range = np.array([180, 255, 250])

        mask= cv.inRange(hsv, lower_range, upper_range)

        cnts = cv.findContours(mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE )
        cnts = imutils.grab_contours(cnts)

        for c in cnts:
            area = cv.contourArea(c)
            if area > 50:
                cv.drawContours(frame, [c], -1, (0,255,0), 3)

                M = cv.moments(c)


                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                cv.circle(frame, (cx,cy), 7, (255,255,255), -1)
                cv.putText(frame, "Center", (cx-20, cy-20), cv.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255),3)

                writer.writerow([timee , cx , cy])

        count_frame = count_frame + 1
        timee = round((count_frame/30), 2)


        cv.imshow("result", frame)

        k = cv.waitKey(30)



cap.release()
cv.destroyAllWindows()











