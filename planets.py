import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"mercurio",(110,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"venus",(170,90),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"terra",(210,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"marte",(250,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"jupiter",(310,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"saturno",(350,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"urano",(410,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"netuno",(450,80),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.imshow("resultado",img)
cv2.waitKey(0)













