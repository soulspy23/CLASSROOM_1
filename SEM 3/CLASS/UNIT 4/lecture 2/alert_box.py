#alert box

import pyautogui
num = int(input("Enter a value :"))
x = 100/num

if num == 0:
    pyautogui.alert("Alert ! cannot be divided by 0")
else:
    print("The value is",x)