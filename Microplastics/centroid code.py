#COnvert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#find threshold which determines the contours
_,thresh = cv2.threshold(gray,10, 255, cv2.THRESH_BINARY )
thresh = cv2.erode(thresh, np.ones((5,5)))

#find contours
cnts,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

for (j, c) in enumerate(cnts):
        if cv2.contourArea(c) > 1000:  
            mask = np.zeros_like(gray)
            #draw contours on a black image
            cv2.drawContours(mask,[c],-1, 255, -1)
            # find centroid
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #draw centroid
            cv2.circle(res, (cx, cy),6, (0, 0, 255), -1)
            cv2.putText(res, "centroid", (cx - 25, cy - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
