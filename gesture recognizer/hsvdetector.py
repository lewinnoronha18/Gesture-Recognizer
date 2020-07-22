import cv2 
import numpy as np

def nothing(x):
	pass
# define a video capture object 


vid = cv2.VideoCapture(0) 
cv2.namedWindow('Trackbars')

cv2.createTrackbar('l-h','Trackbars',0,179,nothing)
cv2.createTrackbar('l-s','Trackbars',0,179,nothing)
cv2.createTrackbar('l-v','Trackbars',0,179,nothing)
cv2.createTrackbar('u-h','Trackbars',0,255,nothing)
cv2.createTrackbar('u-s','Trackbars',0,255,nothing)
cv2.createTrackbar('u-v','Trackbars',0,255,nothing)
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    frame=cv2.flip(frame,1)
    frame=frame[0:400,0:400]
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos('l-h','Trackbars')
    l_s=cv2.getTrackbarPos('l-s','Trackbars')
    l_v=cv2.getTrackbarPos('l-v','Trackbars')
    u_h=cv2.getTrackbarPos('u-h','Trackbars')
    u_s=cv2.getTrackbarPos('u-s','Trackbars')
    u_v=cv2.getTrackbarPos('u-v','Trackbars')

    lower_skin=np.array([0,0,79])
    upper_skin=np.array([39,255,255])

    mask=cv2.inRange(hsv,lower_skin,upper_skin)
    blur = cv2.medianBlur(mask,5)
    
    kernel = np.ones((9,9),np.uint8)
    closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE,kernel)
    kernel2= np.ones((3,3),np.uint8)
    closing2 = cv2.morphologyEx(closing, cv2.MORPH_CLOSE,kernel2)
    
    gesture='peace'
    res=cv2.bitwise_and(frame,frame,mask=blur)
    '''
    cv2.imwrite(gesture+str(i)+'.jpg',closing)
    i=i+1
    '''
    #cv2.imshow('closing',frame)
    cv2.imshow('blur',closing2)
    cv2.imshow('result',res)

    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 