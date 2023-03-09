import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests

window = tk.Tk()
window.geometry("640x800")
window.title("Voice Speech Project")
window.resizable(False, False)

label_voice =tk.Label(window, text="Voice Text")
label_voice.grid(columnspan=5, row=1, padx=5, pady=5)

voiceText = tk.StringVar()
voice = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=6)
voice.grid(column=2, row=2, padx=5, pady=5)

def GenerateVoice():
    response = requests.get('https://api.elevenlabs.io/openapi.json')
    print(response.status_code)
    print(response.json())

button = tk.Button(window, text="Generate voice", command=GenerateVoice)
button.grid(column=0, row=2, padx=5, pady=5)

logo = Image.open('ganyu.gif')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image_names = logo

logo_label.grid(columnspan=5, row=0)

canvas = tk.Canvas(window, width=600, height=600)
canvas.grid(columnspan=5, rowspan=4)





if __name__ == "__main__":
    window.mainloop()
