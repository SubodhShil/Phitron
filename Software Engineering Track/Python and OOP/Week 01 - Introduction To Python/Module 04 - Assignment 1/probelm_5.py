import pyautogui

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        pyautogui.write('#', interval=0.2)
    pyautogui.write('\n')
