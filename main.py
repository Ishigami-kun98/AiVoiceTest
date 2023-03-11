import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests
import os
import time
from pygame import mixer


mixer.init()


window = tk.Tk()
window.geometry("640x800")
window.title("Voice Speech Project")
window.resizable(False, False)

label_voice =tk.Label(window, text="Voice Text")
label_voice.grid(columnspan=5, row=1, padx=5, pady=5)

voiceText = tk.StringVar()
voice = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=6)
voice.grid(column=2, row=2, padx=5, pady=5)

#voice_id = 'q2hdaLxGtlbMLaQR1foF'
voice_id = 'nJIqabccGu6XcekSdjkK'
# voice_id = '21m00Tcm4TlvDq8ikWAM'
def GenerateVoice():
    t = voice.get('1.0', tk.END)

    post_header = {'accept': 'audio/mpeg', 
               'xi-api-key': '6a1e9174b98828f5eeb8ff828662fc3e', 
               'Content-Type': 'application/json',
                }
    post_datas = {
    "text": t,
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
        }
    }

    get_header = {'accept': 'application/json', 
               'xi-api-key': '6a1e9174b98828f5eeb8ff828662fc3e', 

            }
    response = requests.post(f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}',json=post_datas, headers= post_header)
    response_get = requests.get(f'https://api.elevenlabs.io/v1/voices', headers=get_header)
    # if response_get.status_code == 200:
    #     all = response_get.json()
    #     for voce in all['voices']:
    #         print(voce)
    # response_get = requests.get(f'https://api.elevenlabs.io/v1/voices/{voice_id}', headers=get_header)
    # print(response_get.content)
    if response.status_code == 200:

        data = response.content
        if os.path.exists("myfile.mp3"):
            os.remove("myfile.mp3")
        else:
            print("file doesnt exist")
        with open('myfile.mp3', mode='bx+') as f:
            f.write(data)
            f.close()
        mixer.music.load("myfile.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        mixer.music.unload()
 
    else:
        print(response)
        print(response.headers)
    
button = tk.Button(window, text="Generate voice", command=GenerateVoice)
button.grid(column=0, row=2, padx=5, pady=5)
currentDir = os.path.abspath("BackGround.gif")

logo = Image.open(currentDir).convert('RGB')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image_names = logo

logo_label.grid(columnspan=5, row=0)

canvas = tk.Canvas(window, width=600, height=600)
canvas.grid(columnspan=5, rowspan=4)





if __name__ == "__main__":
    window.mainloop()
