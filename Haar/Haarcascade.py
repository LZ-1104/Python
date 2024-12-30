import numpy as np
import cv2 as cv


while(True):
    # Capture frame-by-frame
    pic=cv.imread("Test/pic2/4.jpg")
    # Our operations on the frame come here
    gray = cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
    cv.namedWindow('img',cv.WINDOW_NORMAL)
    # Display the resulting frame
    cv.imshow('img',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv.destroyAllWindows()