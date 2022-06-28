# Import Necessary Libraries
import speech_recognition as sr
from translate import Translator
import webbrowser as wb
from gtts import gTTS
import os

def main():
    textt=input(' enter translate for translation \n enter search for searching \n')

    if 'translate' in textt:
        # Create Recognizer() class objects called r1
        r1 = sr.Recognizer()
        sound2 = "english.wav"

        # google languages display with their codes
        import googletrans
        print(googletrans.LANGUAGES)

        # with sr.Microphone() as source2:
        with sr.AudioFile(sound2) as source2:
            r1.adjust_for_ambient_noise(source2)
            print("now speak")
            print("translating...")
            audio2 = r1.listen(source2)
            try:
                # converting audio to text
                get_sentence2 = r1.recognize_google(audio2)
                print('Phrase to be Translated: ' + get_sentence2)
                tl=input('enter designation language code : ')
                translator = Translator(from_lang='en', to_lang=tl)
                text_to_translate= translator.translate(get_sentence2)
                print(text_to_translate)
                text = str(text_to_translate)
                speak = gTTS(text=text, lang=tl, slow=False)
                speak.save("rc1.mp3")
                os.system("start rc1.mp3")

            except sr.UnknownValueError:
                print("Unable to understand the input")
            except sr.RequestError as e:
                print("Unable to provide required output".format(e))

    else:
        url = 'https://www.google.co.in/search?q='
        r3 = sr.Recognizer()
        sound3 = "manit.wav"
        with sr.AudioFile(sound3) as source3:
            r3.adjust_for_ambient_noise(source3)
            print("converting to text")
            audio3 = r3.listen(source3)
            try:
                print("converted audio is... \n " + r3.recognize_google(audio3))
                print('Phrase to be searched: ' + r3.recognize_google(audio3))
                wb.get().open_new(url + r3.recognize_google(audio3))

            except sr.UnknownValueError:
                print("Unable to understand the input")
            except sr.RequestError as e:
                print("Unable to provide required output".format(e))


if __name__=="__main__" :
    main()