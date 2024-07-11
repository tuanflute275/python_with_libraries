import pyautogui as pg
import time

time.sleep(10)
# tìm tọa độ
# print(pg.position())

pg.leftClick(245, 132, 1, 1)
pg.typewrite("www.facebook.com")
pg.press("Enter")