import pyautogui
import time
# 2 seconds for switching to LumberJack Tab
time.sleep(2)

# clicking on the start button
pyautogui.moveTo(684,611,duration=2)
pyautogui.click()


#From now on every commented command works with mouse
#which for higher speed I replaced with keyboard commands


while True:
    if pyautogui.locateOnScreen(r"c:\users\kian\desktop\lumberjack\leftorright\left.png",region=(597,326,25,27)) != None:
        # pyautogui.moveTo(766,603)
        # pyautogui.click()
        pyautogui.press("right")

    elif pyautogui.locateOnScreen(r"c:\users\kian\desktop\lumberjack\leftorright\right.png",region =(743,308,29,36)) != None:
        # pyautogui.moveTo(600,606)
        # pyautogui.click()
        # pyautogui.click()
        pyautogui.press("left")

    elif pyautogui.locateOnScreen(r"c:\users\kian\desktop\lumberjack\leftorright\tworights.png",region =(725,247,34,130)) != None:
        # pyautogui.moveTo(766,603)
        # pyautogui.click()
        # pyautogui.click()
        pyautogui.press("right")
        pyautogui.press("right")


    elif pyautogui.locateOnScreen(r"c:\users\kian\desktop\lumberjack\leftorright\twolefts.png",region =(605,276,38,93)) != None:
        # pyautogui.moveTo(600,606)
        # pyautogui.click()
        # pyautogui.click()
        pyautogui.press("left")
        pyautogui.press("left")



    elif pyautogui.locateOnScreen(r"c:\users\kian\desktop\lumberjack\leftorright\oneleftthenright.png",region =(598,277,48,67)) != None:
        # pyautogui.moveTo(600,606)
        # pyautogui.click()
        pyautogui.press("left")
        # pyautogui.moveTo(766,603)
        # pyautogui.click()
        pyautogui.press("right")


    elif pyautogui.locateOnScreen(r"c:\users\kian\desktop\lumberjack\leftorright\onerightthenleft.png",region =(714,275,41,72)) != None:
        # pyautogui.moveTo(766,603)
        # pyautogui.click()
        pyautogui.press("right")
        # pyautogui.moveTo(600,606)
        # pyautogui.click()
        pyautogui.press("left")
