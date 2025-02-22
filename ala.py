import cv2
import numpy as np

image_path = "Images/MCQQ.png"
image = cv2.imread(image_path)
if image is None:
     raise FileNotFoundError("image is not found")

re = cv2.resize(image,(700,700))
gray = cv2.cvtColor(re, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 1)
edged = cv2.Canny(blurred, 75, 200)
#image, gray, edged,re


countors, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(countors))
cv2.drawContours(edged,countors,-1,(255,255,255),2)
#cv2.imshow("draw countors",edged)

countors = sorted(countors,key=cv2.contourArea,reverse=True)
if len(countors) < 4:
    print("not enogh counots detected")
contor1 = countors[0]
contor2 = countors[1]
contor3 = countors[2]
contor4 = countors[3]
contor5 = countors[4]

x1, y1, w1, h1 = cv2.boundingRect(contor1)
x4, y4, w4, h4 = cv2.boundingRect(contor2)
x5, y5, w5, h5 = cv2.boundingRect(contor3)


answer_section1 = edged[y1:y1+h1, x1:x1+w1]
answer_section2= re[y4:y4+h4, x4:x4+w4]
registration_number =edged[y5:y5+h5, x5:x5+w5]
cv2.imshow("answer section",answer_section1)
cv2.imshow("answer section 2",answer_section2)
cv2.imshow("reg no section",registration_number)

def rectcountor(countors):
    mylist = []
    for i in countors:
        area = cv2.contourArea(i)
        #print("area is"area)
        if area > 50:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            #print("corner point:",len(approx))
            if len(approx) == 4:
                mylist.append(i)
    mylist = sorted(mylist,key=cv2.contourArea,reverse=True)            
    #print(mylist)
    return  mylist 

def get_cornerpoint(cont):
    peri = cv2.arcLength(cont,True)
    approx = cv2.approxPolyDP(cont,0.02*peri,True)
    return approx
 
   
a = rectcountor(countors=countors)
my_answer = a[0]
print(len(my_answer))

b= get_cornerpoint(my_answer) 
print(b)

gradepoint1= get_cornerpoint(my_answer[1])
gradepoint2= get_cornerpoint(my_answer[2])
gradepoint3= get_cornerpoint(my_answer[0])
gradepoint4= get_cornerpoint(my_answer[3])
print(gradepoint2.shape)
print(gradepoint4.shape)
# if  !=0:
#     cv2.drawContours(edged,my_answer,-1(0,255,0),10)
#     cv2.drawContours(edged,my_answer,-1,(0,255,0),20)

if gradepoint1.size != 0 and gradepoint2.size != 0:
    cv2.drawContours(re,gradepoint1,-1,(0,255,0),10)
    cv2.drawContours(re ,gradepoint2,-1,(0,255,0),10)

#my_answer = a[3]    
#my_answer = a[0]
#cv2.imshow("Processed Image", image)
#cv2.imshow("gray",gray)
#cv2.imshow("edge",edged)
#cv2.imshow("bubbles",bubble
cv2.imshow("resize image",re)
cv2.waitKey(0)
cv2.destroyAllWindows()








