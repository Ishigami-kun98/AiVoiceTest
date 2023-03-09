import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests
import pygame

window = tk.Tk()
window.geometry("640x800")
window.title("Voice Speech Project")
window.resizable(False, False)

label_voice =tk.Label(window, text="Voice Text")
label_voice.grid(columnspan=5, row=1, padx=5, pady=5)

voiceText = tk.StringVar()
voice = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=6)
voice.grid(column=2, row=2, padx=5, pady=5)

pygame.mixer.init()

voice_id = 'q2hdaLxGtlbMLaQR1foF'
def GenerateVoice():
    t = voice.get('1.0', tk.END)

    header = {'accept': 'audio/mpeg', 
               'xi-api-key': '6a1e9174b98828f5eeb8ff828662fc3e', 
               'Content-Type': 'application/json',
                }
    datas = {
    "text": t,
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
        }
    }
    response = requests.post(f'https://api.elevenlabs.io/v1/text-to-speech/q2hdaLxGtlbMLaQR1foF',json=datas, headers= header)

    if response.status_code == 200:
        print(type(response.encoding))
        print(response)
        print(response._content)
    else:
        print(response)
        print(response.headers)
    
button = tk.Button(window, text="Generate voice", command=GenerateVoice)
button.grid(column=0, row=2, padx=5, pady=5)

logo = Image.open('BackGround.gif')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image_names = logo

logo_label.grid(columnspan=5, row=0)

canvas = tk.Canvas(window, width=600, height=600)
canvas.grid(columnspan=5, rowspan=4)





if __name__ == "__main__":
    window.mainloop()
