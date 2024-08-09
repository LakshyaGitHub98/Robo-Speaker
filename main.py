import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
while 1:
    print("Welcome to Robospeaker ! Created by Lakshya.")
    x=input("Enter something you wana me to pronounce : ")
    speaker.speak(x)