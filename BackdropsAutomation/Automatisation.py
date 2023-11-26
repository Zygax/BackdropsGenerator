import subprocess
import time
import pyautogui
import tkinter as tk
from tkinter import simpledialog
import pyperclip
import TypePromptDiscord
import Config
from tkinter import messagebox

# Function to simulate typing with a delay
def slow_typewrite(text, delay=0.02):
    for char in text:
        pyautogui.typewrite(char, interval=delay)
    
def show_popup_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Download Images", "Please download all pictures manually.")
    root.destroy()

# Activate the Chrome window
chrome_window_title = "Random - Google Chrome"
pyautogui.getWindowsWithTitle(chrome_window_title)[0].activate()

# Wait for a few seconds to allow Chrome to open
time.sleep(5)
pyautogui.hotkey('shift', 'esc')

# Create a pop-up window for user input
root = tk.Tk()
root.withdraw()  # Hide the main window

user_input = simpledialog.askstring("User Input", "Enter a theme for the backdrop:")

# Destroy the pop-up window
root.destroy()

# Define the multiline text using triple quotes
background_prompt = f"I'll be creating backdrops for photography by midjourney. Theme will be {user_input} world, but without people. Please give me different ideas for background I could create. Don't write anything else just Give me 20 prompts like: 1. {user_input} ..., no people, ground view. ultra realistic, backdrop, 8k. 2. {user_input} ..., no people, ground view. ultra realistic, backdrop, 8k. 3. {user_input}..., no people, ground view. ultra realistic, backdrop, 8k. etc. Write your location instead of three dots."

# Simulate typing the background_prompt slowly
slow_typewrite(background_prompt)

# Simulate pressing Enter to send the text
pyautogui.press('enter')

# Wait for ChatGPT to write answer
time.sleep(90)

# Copies last ChatGPT response
pyautogui.hotkey('ctrl', 'shift', 'c')

# Copy the answer from the clipboard to the 'all_prompts' variable
all_prompts = pyperclip.paste()

# Extract and store each prompt in separate variables
prompts = []
for line in all_prompts.split('\n'):
    line = line.strip()
    if line:
        prompts.append(line)

# Now, 'prompts' is a list where each element is one of the 20 prompts
# You can access them using prompts[0], prompts[1], etc.

# Example usage:
for i, prompt in enumerate(prompts):
    Config.prompt = prompt  # Store the current prompt in Config.prompt
    TypePromptDiscord.type_prompt()  # Call the type_prompt function from TypePromptDiscord
    
#Pop-up to wait for pictures to be downloaded
show_popup_message()
