import os
import sys
import subprocess
import threading

from tkinter import *
import customtkinter

from gpt import GPT
from speaker import Speaker
from blinker import Blinker


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

commands = {
    "telegram": "C:\\Windows.old\\Users\\ReerGlobal\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vs": "C:\\Users\\ReerGlobal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe",
    "youtube":"C:\\Users\\ReerGlobal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome apps\\Youtube.exe",
    "movies": "C:\\Users\\ReerGlobal\\Downloads\\Telegram Desktop"
}

def adjust_height(text_widget):
    num_lines = int(text_widget.index('end-1c').split('.')[0])
    text_widget.configure(height= num_lines * 35, border_color="light blue", border_width=1)

def listen_respond(chat_box, root, active_blinker):
    global isListening
    speaker = Speaker()
    response = GPT()
    isListening = False
    active_blinker.configure("orange")

    def activate_deactivate(event=None):
        global isListening
        if isListening:
            speaker.deactivation_sound()
            isListening = False
            active_blinker.configure("orange") 

        else:
            speaker.activation_sound()
            isListening = True
            active_blinker.configure("green") 
    
    root.bind("<F7>", activate_deactivate)
    root.bind("<space>", activate_deactivate)
      

    while True:
        if isListening:
            print("Listening...")
            text = speaker.recognize_speech(1, 30, 10)
            resp = ''
            if text == ' ':
                continue
            if "go to sleep" in text or text == '':
                print("Goodbye")
                activate_deactivate()
                continue

            textbox = customtkinter.CTkTextbox (chat_box,
                                            width=600,
                                            height=10,
                                            text_color='white',
                                            fg_color='black',
                                            activate_scrollbars=False,
                                            wrap="word",
                                            font=('Microsoft YaHei UI', 16)
                                            )
            textbox.pack(pady=5, padx=10, fill="y", expand=True)
            textbox.insert('end', "You \n")
            textbox.insert('end', text + "\n")
            textbox.insert('end'," \n")
            adjust_height(textbox)
        
            if 'bye' in text or 'goodbye' in text:
                resp = response.get_response(text, "close_command")
                speaker.speak_text(resp)
                root.destroy()
            elif 'open' in text:
                if 'telegram' in text:
                    subprocess.Popen(resource_path(commands['telegram']))
                elif 'chrome' in text or 'google' in text:
                    subprocess.Popen(resource_path(commands['chrome']))
                elif 'visual studio' in text or 'vs code' in text:
                    subprocess.Popen(resource_path(commands['vs']))
                elif 'youtube' in text or 'you tube' in text or 'Youtube' in text:
                    pass
                elif 'movies' in text:
                    subprocess.Popen(resource_path(commands['movies'])) 
                
                resp = response.get_response(text, "open_command")

            else:
                resp = response.get_response(text, "normal")

            resp_box = customtkinter.CTkTextbox (chat_box,
                                            width=600,
                                            height=10,
                                            text_color='white',
                                            fg_color='black',
                                            activate_scrollbars=False,
                                            wrap="word",
                                            font=('Microsoft YaHei UI', 16)
                                        )
            resp_box.pack(pady=5, padx=10, fill="y", expand=True)
            resp_box.insert('end', "Browne \n")
            resp_box.insert('end', resp + "\n")
            resp_box.insert('end'," \n")
        
            adjust_height(resp_box)
            speaker.speak_text(resp)
        
        
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root = customtkinter.CTk()
root.title("AI")
root.geometry("300x300")
root.iconbitmap(resource_path("assets\\robot_icon.ico"))

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", toggle_fullscreen) 

label=customtkinter.CTkLabel(master=root,
                                text="   BROWNE",
                                font=('Microsoft YaHei UI',24),
                                text_color='white',
                                fg_color='light blue',
                                anchor="w",
                                justify="left",
                                width=1500,
                                height=40
                            )
label.pack()
blink = Blinker(root, width=20, height=20, bg="black", highlightthickness=0)
blink.configure("red")
blink.pack(pady=5)

chat_box = customtkinter.CTkScrollableFrame(master=root,
                                    width=1000,
                                    height=700,
                                    fg_color="transparent",
                                )
chat_box.pack(padx=30)

loop_thread = threading.Thread(target=listen_respond, args=(chat_box, root, blink), daemon=True)
loop_thread.start()

root.mainloop()