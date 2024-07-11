# pip install pyautogui
# thư viện giúp thực hiện việc auto
import pyautogui as pg
# time thư viện có sãn quản lý về ngày giờ
import time
# io thư viện có sẵn 
import io
# pip install pyperclip
# thư viện giúp copy and paste và ...
import pyperclip

# delay 10s
time.sleep(10)
# open file text.txt, mode r == đọc , set tiếng việt utf-8
txt = io.open("text.txt", mode="r", encoding="utf-8")

# for txt lấy ra các giá trị trong file đó
for item in txt:
    # copy các item
    pyperclip.copy(item)
    # dán các item đã sao chép được từ file txt
    pg.hotkey("ctrl", "v")
    # định nghĩa là nhấn nút enter
    pg.press("Enter")
    # delay mỗi 1 tin nhắn
    # time.sleep(3)