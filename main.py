from operator import pos
import time
import pyautogui
import pytesseract
from PIL import Image

def main():
    咖啡廳()
    課程表()
    社交()
    信箱()

def 咖啡廳():
    x, y = pyautogui.center(pyautogui.locateOnScreen("rksr.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(5)
    x, y = pyautogui.center(pyautogui.locateOnScreen("rksr_vlok.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(1)
    x, y = pyautogui.center(pyautogui.locateOnScreen("oimbc.png", confidence=0.95))
    pyautogui.click(x, y)
    x, y = pyautogui.center(pyautogui.locateOnScreen("close.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(1)
    x, y = pyautogui.center(pyautogui.locateOnScreen("back.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(5)
    return(None)


def 課程表():
    x, y = pyautogui.center(pyautogui.locateOnScreen("yrwd.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(5)
    x, y = pyautogui.center(pyautogui.locateOnScreen("muhe.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(1)
    region = (259, 140, 28, 30)
    screenshot = pyautogui.screenshot(region=region)
    remain = int(pytesseract.image_to_string(
    screenshot,
    config=r"--psm 10 -c tessedit_char_whitelist=0123456789",
    lang="eng",))
    while remain != 0:
        heart = pyautogui.locateOnScreen("heart.png", confidence=0.95)
        try: 
            if heart is not None:
                hx, hy, hw, hh = heart
                try:
                    pyautogui.locateOnScreen("tick.png", region=(max(0, hx - 80), max(0, hy - 80), hw + 160, hh + 160), confidence=0.95)
                    continue
                except pyautogui.ImageNotFoundException:
                    x, y = pyautogui.center(heart)
                    pyautogui.click(x, y)
                    x, y = pyautogui.center(pyautogui.locateOnScreen("yrwd_start.png", confidence=0.95))
                    pyautogui.click(x, y)
                    time.sleep(5)
                    x, y = pyautogui.center(pyautogui.locateOnScreen("confirm.png", confidence=0.95))
                    pyautogui.click(x, y)
                    time.sleep(1)
                    remain -= 1
        except pyautogui.ImageNotFoundException:
            pass
        pyautogui.click(1865, 544)

def 社交():
    x, y = pyautogui.center(pyautogui.locateOnScreen("ifg.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(1)
    x, y = pyautogui.center(pyautogui.locateOnScreen("ifg_ifg.png", confidence=0.95))
    pyautogui.click(x, y)
    pyautogui.press("space")
    x, y = pyautogui.center(pyautogui.locateOnScreen("back.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(5)
    return(None)

def 信箱():
    x, y = pyautogui.center(pyautogui.locateOnScreen("oymr.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(5)
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press("space")
    x, y = pyautogui.center(pyautogui.locateOnScreen("back.png", confidence=0.95))
    pyautogui.click(x, y)
    time.sleep(5)
    return(None)

while True:
    time.sleep(10)
    try:
        if pyautogui.locateOnScreen("rksr.png", confidence=0.95) is not None:
            咖啡廳()
    except pyautogui.ImageNotFoundException:
        pass
#    try:
#        if pyautogui.locateOnScreen("yrwd.png", confidence=0.95) is not None:
#            課程表()
#    except pyautogui.ImageNotFoundException:
#        pass
    try:
        if pyautogui.locateOnScreen("ifg.png", confidence=0.95) is not None:
            社交()
    except pyautogui.ImageNotFoundException:
        pass
    try:
        if pyautogui.locateOnScreen("oymr.png", confidence=0.95) is not None:
            信箱()
    except pyautogui.ImageNotFoundException:
        pass
    break