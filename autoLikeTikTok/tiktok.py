import pyautogui as pg
import time

# delay 5s
time.sleep(5)
# auto click
for _ in range(10):
    pos=pg.position(600, 500)
    pg.doubleClick(pos)
    time.sleep(3)
    pos2=pg.position(1197, 613)
    pg.click(pos2)
    time.sleep(30)