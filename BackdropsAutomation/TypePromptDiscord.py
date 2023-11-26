import Config
import pyautogui
import time

def type_prompt():
    # Activate the Discord window by title
    discord_window_title = "@Midjourney Bot - Discord"
    pyautogui.getWindowsWithTitle(discord_window_title)[0].activate()

    # Wait for a moment before typing to ensure the Discord input field is ready
    time.sleep(15)

    # Type the prompt in Discord only if prompt is not empty
    if Config.prompt:
        pyautogui.write(f"/imagine {Config.prompt}")
        pyautogui.press('enter')
