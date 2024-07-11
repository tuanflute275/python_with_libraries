import cv2
import time
import os


cap = cv2.VideoCapture(0)

FolderPath="img/finger"
lst=os.listdir(FolderPath)
#print(lst)
lst_2=[]  # khai báo list chứa các mảng giá trị của các hình ảnh/
for i in lst:
    # print(i)
    image=cv2.imread(f"{FolderPath}/{i}")  # Fingers/1.jpg , Fingers/2.jpg ...
    # print(f"{FolderPath}/{i}")
    lst_2.append(image)
# print(len(lst_2))
pTime=0

# detector =htm.handDetector(detectionCon=0.55)
#0.75 độ chính xác 75%

while True:
    ret, frame = cap.read()
    # frame = detector.findHands(frame)
    # lmList = detector.findPosition(frame, draw=False) # phát hiện vị trí
    
    
    h, w, c = lst_2[0].shape
    frame[0:h,0:w] = lst_2[0]  # nếu số ngón tay =0 thì lst_2[-1] đẩy về phần tử cuối cùng của list là ảnh 6
    
    
    # viết ra fps
    cTime=time.time()  # trả về số giây, tính từ 0:0:00 ngày 1/1/1970 theo giờ  utc , gọi là(thời điểm bắt đầu thời gian)
    fps=1/(cTime-pTime) # tính fps Frames per second - đây là  chỉ số khung hình trên mỗi giây
    pTime=cTime
    # show fps lên màn hình, fps hiện đang là kiểu float , ktra print(type(fps))
    cv2.putText(frame, f"FPS: {int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)


    
    cv2.imshow("Tuanflute", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release() # giải phóng cam
cv2.destroyAllWindows() # đóng tất cả cửa sổ windows