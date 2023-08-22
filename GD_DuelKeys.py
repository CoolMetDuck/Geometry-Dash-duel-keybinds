import keyboard
import mouse
import pyautogui
def key_event(e):
    if e.event_type == "down" and keyboard.is_pressed("h"):
        pyautogui.moveTo(1442,540)
        mouse.click("left")

   








keyboard.hook(key_event)

keyboard.wait()