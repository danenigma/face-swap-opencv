import cv2
import sys
import turtle
import httplib
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

capture  = cv2.VideoCapture(0)

#conn = httplib.HTTPConnection("192.168.1.33:81")
while True:
    ret,image  = capture.read()

    if image is None:
        continue
    gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    faces  = face_cascade.detectMultiScale(
              gray,
              scaleFactor = 1.1,
              minNeighbors = 5,
              minSize  = (30,30),
              flags  = cv2.cv.CV_HAAR_SCALE_IMAGE
              )
    print len(faces)
    if len(faces)==1:
	cord1,cord2 = faces[0],faces[1]
        face1  = image[cord1[0]:cord1[0]+cord1[2],cord1[1]:cord1[1]+cord1[3]]
        face2  = image[cord2[0]:cord2[0]+cord2[2],cord2[1]:cord2[1]+cord2[3]]
	print face2.shape[0]        
	face1 = cv2.resize(face1,(face2.shape[0],face2.shape[1]),interpolation = cv2.INTER_CUBIC)
	face2 = cv2.resize(face2,(face1.shape[0],face1.shape[1]),interpolation = cv2.INTER_CUBIC)
	image[cord2[0]:cord2[0]+cord2[2],cord2[1]:cord2[1]+cord2[3]] = face1
	image[cord1[0]:cord1[0]+cord1[2],cord1[1]:cord1[1]+cord1[3]] = face2
	
	cv2.imshow("face one",face1)
	cv2.imshow("face two",face2)	         	
    cv2.imshow("face tracking ...........",image)
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
