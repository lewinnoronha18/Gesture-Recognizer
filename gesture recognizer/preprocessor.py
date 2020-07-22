import cv2
import numpy as np
import os
from zipfile import ZipFile

lst=os.listdir('gest output')
for r in lst:
	
	j=0

	path='leapGestRecog/'+'0'+r+'/01_palm'
	for i in os.listdir(path):
		img=cv2.imread(path+'/'+i)
		new=cv2.resize(img,(400,400))
		ret,thresh1 = cv2.threshold(new,127,255,cv2.THRESH_BINARY)
		newpath='gest output/palm'
		filename=newpath+'/'+'0'+r+'_'+str(j)+'new.png'
		cv2.imwrite(filename,thresh1)
		j+=1
	'''	
	print(r,' done')

print('inshallah all done')




