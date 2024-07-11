# pip install opencv-python 
# nhận diện khuôn mặt, cử chỉ
import cv2

# đọc ảnh
img=cv2.imread("img/1.jpeg", 1)

# resize image
img=cv2.resize(img,(400, 200)) #rộng , dài

# xoay ảnh
# img=cv2.rotate(img, cv2.ROTATE_180)

# xuất ảnh
cv2.imshow("Hinh anh cua toi ", img)
k=cv2.waitKey()

# lưu ảnh mới nếu nhắn phím s
# ord("kitu") trả ra số trong bảng mã ascII
if k == ord("s"):
    cv2.imwrite("anhmoi.jpg", img)

