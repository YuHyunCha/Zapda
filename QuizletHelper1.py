import pyautogui
import keyboard


pyautogui.click(100,100)
while 1:
    if keyboard.is_pressed('j'):
        pyautogui.typewrite("1") # j -> 1
    if keyboard.is_pressed('i'):
        pyautogui.typewrite("2") # i -> 2
    if keyboard.is_pressed('o'):
        pyautogui.typewrite("3") # o -> 3
    if keyboard.is_pressed('p'):
        pyautogui.typewrite("4") # p -> 4
    if keyboard.is_pressed('q'): 
        break                    # q -> exit