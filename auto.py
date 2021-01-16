from PIL import ImageGrab
import numpy as np
import pyautogui
import pyperclip
import datetime
import imutils
import random
import cv2
import time


def paste():
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)

    time.sleep(0.5)
    pyautogui.hotkey('enter')

def send_text(text):
    pyperclip.copy(text)
    pyautogui.moveTo(3000, 500)
    pyautogui.click(3000, 1350)
    paste()

    if "p!highlow" in text:
        pyperclip.copy(options[random.randint(0, 1)])
        paste()

    if "p!buy fishing rod" in text:
        pyperclip.copy("p!withdraw 150")
        pyautogui.moveTo(3000, 500)
        pyautogui.click(3000, 1350)
        paste()

        time.sleep(1)
        pyautogui.click(2965, 1300)

    if "p!trivia hard" in text:
        pyperclip.copy(random.randint(1, 4))
        time.sleep(1)
        paste()


options = ["lower", "higher"]

commands = {
    "p!highlow" : [0.5*60, datetime.datetime.now()],
    "p!fish" : [1*60, datetime.datetime.now()],
    "p!buy fishing rod" : [4*60, datetime.datetime.now()],
    "p!work" : [5*60, datetime.datetime.now()],
    "p!deposit all" : [5*60, datetime.datetime.now()],
    "p!trivia hard" : [10*60, datetime.datetime.now()],
    "p!daily" : [86400*60, datetime.datetime.now()]
}


index = 0
time.sleep(1)


while True:
    for x in commands:
        difference = datetime.datetime.now() - commands[x][1]
        if difference.total_seconds() >= commands[x][0]:
            print(x)
            send_text(x)
            commands[x][1] = datetime.datetime.now()


"""
while True:

    # Monitor 1 default
    #img = ImageGrab.grab()
    
    # Monitor 2 (5900, 2025, 6100, 2100)
    img = ImageGrab.grab(bbox=(3000, 1500, 4800, 1700), all_screens=True)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([85, 60, 0])
    upper = np.array([90, 255, 255])

    mask1 = cv2.inRange(hsv, lower, upper)

    cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    for c in cnts1:
        area1 = cv2.contourArea(c)
        if area1 > 1000:

            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Cyan", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

            print("I am detecting the color" + str(index))
            index += 1

            # Monitor 1 1315, 1375
            # Monitor 2 4875, 1375
            pyautogui.click(4875,1375)

    cv2.imshow("result", frame)

    k = cv2.waitKey(5)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""