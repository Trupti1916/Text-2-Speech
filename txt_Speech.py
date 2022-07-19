#google text to speech
from gtts import gTTS
import os

my_sentence = input('Enter your sentence you want to convert into audio :- ')

print(os.getcwd())

audio = gTTS(text=my_sentence, lang='en', slow=False)

audio.save('english.mp3')


