import pyautogui
import time
import pandas
import openpyxl
import numpy

pyautogui.press("win")
time.sleep(4)
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://www.linkedin.com/feed/")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=854, y=98)

#achar a posição do mouse para clicar
print(pyautogui.position())
