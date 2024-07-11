import cv2
# numpy xử lý mảng
import numpy as np 

cap = cv2.VideoCapture(0) # dùng webcam
# cap = cv2.VideoCapture("video.mp4") # dùng video
while True:
    # ret trả về trả về giá trị true false
    #   -> trả về false nếu k chụp được
    #cap.read() đọc ảnh trong khung hình
    ret, frame = cap.read() 
    width= int(cap.get(3))
    height= int(cap.get(4))
    print(ret)
    # chèn text
    font=cv2.FONT_HERSHEY_TRIPLEX
    img=cv2.putText(frame, "Tuanflute", (0,height-50), font,3,5)
    cv2.imshow("Cua so cam", frame) # hiện lên
    if cv2.waitKey(1) == ord("q"):
        break
cap.release() # giải phóng cam
cv2.destroyAllWindows() # đóng tất cả cửa sổ windows