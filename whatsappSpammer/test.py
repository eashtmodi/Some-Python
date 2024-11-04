import time, pyautogui
time.sleep(5)
f= open("Bee Movie Script.txt","r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

