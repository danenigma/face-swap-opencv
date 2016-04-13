import cv2
import sys
import turtle
import httplib
FACE_CASCADE = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

def get_faces(image):	
    gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#convert to gray scale
    
    faces  = FACE_CASCADE.detectMultiScale(#get faces
              gray,
              scaleFactor = 1.1,
              minNeighbors = 5,
              minSize  = (30,30),
              flags  = cv2.cv.CV_HAAR_SCALE_IMAGE
              )
    return faces	

capture  = cv2.VideoCapture(0)#create capture object 
while True:
    ret,image  = capture.read()

    if image is None:
        continue
    faces = get_faces(image)
    print len(faces)
    if len(faces)==2:#if two faces are detected
	cord1,cord2 = faces[0],faces[1]
	x,y,w,h = cord1
	x2,y2,w2,h2 = cord2
	cv2.rectangle(image ,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)#uncomment this line to draw rectangles over the faces
        face1  = image[y:y+h,x:x+w]
        face2  = image[y2:y2+h2,x2:x2+w2]   
	face1 = cv2.resize(face1,(w2,h2),interpolation = cv2.INTER_CUBIC)
	face2 = cv2.resize(face2,(w,h),interpolation = cv2.INTER_CUBIC)
	image[cord2[1]:cord2[1]+cord2[3],cord2[0]:cord2[0]+cord2[2]] = face1
	image[cord1[1]:cord1[1]+cord1[3],cord1[0]:cord1[0]+cord1[2]] = face2
	cv2.imshow("face one",face1)
	cv2.imshow("face two",face2)	         	
    cv2.imshow("face tracking ...........",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
