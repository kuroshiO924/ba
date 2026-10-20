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
    remain = pytesseract.image_to_string(
    screenshot,
    config=r"--psm 10 -c tessedit_char_whitelist=0123456789",
    lang="eng",)
    while remain != "0":
        while pyautogui.locateOnScreen("heart.png", confidence=0.95) is not None:
            x, y = pyautogui.center(pyautogui.locateOnScreen("heart.png", confidence=0.95))
            pyautogui.click(x, y)
            x, y = pyautogui.center(pyautogui.locateOnScreen("yrwd_start.png", confidence=0.95))
            pyautogui.click(x, y)
            time.sleep(5)
            x, y = pyautogui.center(pyautogui.locateOnScreen("confirm.png", confidence=0.95))
            pyautogui.click(x, y)
            time.sleep(1)
            remain -= 1
        pyautogui.click(1865, 544)

def 社交():
    x, y = pyautogui.center(pyautogui.locateOnScreen("ifg.png", confidence=0.95))
    pyautogui.click(x, y)

def 信箱():
    x, y = pyautogui.center(pyautogui.locateOnScreen("oymr.png", confidence=0.95))
    pyautogui.click(x, y)

while True:
    time.sleep(10)
    if pyautogui.locateOnScreen("rksr.png", confidence=0.95) is not None:
        咖啡廳()
    if pyautogui.locateOnScreen("yrwd.png", confidence=0.95) is not None:
        課程表()
    #if pyautogui.locateOnScreen("ifg.png", confidence=0.95) is not None:
    #    社交()
    #if pyautogui.locateOnScreen("oymr.png", confidence=0.95) is not None:
    #    信箱()
