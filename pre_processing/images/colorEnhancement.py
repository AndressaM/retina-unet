import cv2
import numpy as np

def proc(img):

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cannyEdge = cv2.Canny(gray, 23, 36)

	#cv2.imshow(cannyEdge)

	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
	morph = cv2.morphologyEx(cannyEdge, cv2.MORPH_DILATE, kernel)
	#opening = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)
	#closing = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
	redCanny = cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR)

	for row in range (0, redCanny.shape[0]):
		for col in range (0, redCanny.shape[1]):
		    pixel = redCanny[row][col]
		    if(pixel[0] or pixel[1] or pixel[2]):                        
		        redCanny[row][col][0] = 0
		        redCanny[row][col][1] = 0 
		        redCanny[row][col][2] = 255

	result = redCanny | img
	return result

# Generate the new color enhanced images
for i in range(21, 41):
    img_id = str(i) + '_training.tif'
    src = cv2.imread(img_id) # load images
    res = proc(src)
    cv2.imwrite('./enhanced/' + img_id, res)
