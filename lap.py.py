import pyautogui, pyperclip, time
time.sleep(2)
for i  in range(100):
	pyperclip.copy("hello" + str(i+1))
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press("enter");
	time.sleep(2)