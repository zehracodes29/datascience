#basic program for cctv cameras
import cv2  #load opencv

WEB_CAM_IDX=0     #default webcam index
cam=cv2.VideoCapture(WEB_CAM_IDX)  #web cam as variable

while cam.isOpened():   #loop when webcam is open
    status, frame=cam.read() # readframe from webcam
    if not status:
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()