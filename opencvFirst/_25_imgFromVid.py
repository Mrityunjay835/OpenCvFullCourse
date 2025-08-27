import cv2
import os
cam = cv2.VideoCapture("./vid/output.mp4")
frameno = 0
while(True):
    ret,frame = cam.read()
    if ret:
    # if video is still left continue creating images
        name = "./vid/imgFromVid/videoFrame"+str(frameno) + '.jpg'
        print ('new frame captured...' + name)
        cv2.imwrite(name, frame)
        frameno += 1
    else:
        break
cam.release()
cv2.destroyAllWindows()

# python _25_imgFromVid.py