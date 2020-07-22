import cv2 
import numpy as np

from tensorflow.keras.models import load_model

vid = cv2.VideoCapture(0) 
reverse_lookup={'0':'Fist','1':'L_shape','2':'Palm','3':'Peace'}
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    frame=cv2.flip(frame,1)
    og_frame=cv2.rectangle(frame, (0,0), (300,300),(255,0,0), 2) 
    frame=frame[0:300,0:300]
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_skin=np.array([0,0,79])
    upper_skin=np.array([39,255,255])

    mask=cv2.inRange(hsv,lower_skin,upper_skin)
    blur = cv2.medianBlur(mask,5)
    
    kernel = np.ones((9,9),np.uint8)
    closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE,kernel)
    kernel2= np.ones((3,3),np.uint8)
    closing2 = cv2.morphologyEx(closing, cv2.MORPH_CLOSE,kernel2)
    imge=cv2.resize(closing2,(150,150))
    
    '''
    gray_image = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)
    arr=np.array(gray_image)
    '''
    arr=np.array(imge)
    arr=arr.reshape(1,150,150)

    model=load_model('my_model2.h5')
    predictw=model.predict(arr)
    predictw=predictw.round()

    predictw=predictw.reshape(4)
    
    ind=0
    for r in range(0,4):
    	if predictw[r]==1:
    		ind=r
    	else:
    		continue

    og_frame=cv2.putText(og_frame,reverse_lookup[str(ind)] ,(300,300),cv2.FONT_HERSHEY_SIMPLEX ,2, (0,0,255),4,cv2.LINE_AA)
    cv2.imshow('output',closing2)
    cv2.imshow('input',og_frame)
    #print(ind)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 