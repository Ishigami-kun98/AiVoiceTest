import requests
import bs4
import os

VoiceFolder = "VoiceToClone/"

response = requests.get('https://genshin-impact.fandom.com/wiki/Ganyu/Voice-Overs')
if response.ok:
    print('Connected succesfully')
    # print(response.headers)
    parseHTML = bs4.BeautifulSoup(response.text, 'html.parser')
    # print(parseHTML)
    div_audios = parseHTML.find_all('span', class_='audio-button custom-theme hidden')
    # print(div_audios)
    for a_audio in div_audios:
        link = a_audio.find('a').get('href')
        link = link.split('/')[0:-2]
        file_name = link[-1]
        link = "/".join(link)

        requestFile = requests.get(link)
        if os.path.exists(VoiceFolder + file_name):
            os.remove(VoiceFolder + file_name)

        if requestFile.ok:
            print("Successfully get sound")
            with open(VoiceFolder + file_name, 'bx') as f:
                f.write(requestFile.content)
        else:
            print("Access denied")
else:
    print('Connection failed')