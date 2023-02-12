# import imp
import random
import base64
from tkinter import *
import tkinter as tk
import os
import webbrowser
import pyautogui
import smtplib
import time
import pywhatkit as kit
import wikipedia
import pyjokes
from GoogleNews import GoogleNews
from commandtaker import cmndtkr
from wlanpass import getwifipass
from playsound import playsound
import datetime
import time 
from pathlib import Path
from pytbangla import computer as cp
import serial
from platform import python_branch
import subprocess
import re
from unicodedata import name
import pyautogui
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#Wish Function
def wish():
    greetings = ("hello sir", "welcome back, sir")
    greet = random.sample(greetings, 1)
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 4:
        cp.bolo(greet)
    elif hour >= 4 and hour < 6:
        cp.bolo("good morning, sir")
    elif hour >= 6 and hour < 12:
        playsound("wish.wav")
    elif hour >= 12 and hour < 18:
        cp.bolo("good afternoon, sir")
    else:
        cp.bolo("welcome back, sir")


#This Function tells latest news
def news(googlenews):
    googlenews = GoogleNews(lan='en', region='bd')
    # print(googlenews);

#This is The GUI Part Of this projext
def main():
    # wish()
    root = tk.Tk()
    root.title("Brixpy")
    root.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='logo.png'))
    root.geometry("500x400+450+200");
    root.loadimage = tk.PhotoImage(file="logo.png")
    root.roundedbutton = tk.Button(root, image=root.loadimage, command=Ai)
    root.roundedbutton["bg"] = "white"
    root.roundedbutton["border"] = "0"
    root.roundedbutton.place(x=850, y=850)
    root.roundedbutton.pack(side="top")
    root.mainloop()




def Light_on():
    serialcomm = serial.Serial('COM3', 9600)
    serialcomm.timeout = 1
    cp.bolo("are you sure?")
    i = cp.shuno().strip()
    if i == "yes":
        serialcomm.write(i.encode())
        time.sleep(0.5)
        cp.bolo("Ligh is on")
    else:
        cp.bolo("ok , as you wish")
        pass
def Light_off():
    serialcomm = serial.Serial("COM3",9600)
    serialcomm.timeout = 1
    cp.bolo("light turned off")
    i = cp.shuno().strip();
    serialcomm.write(i.encode())
    time.sleep(0.5)


#This Function can convert text to handwritting
def text_to_hand(var):
    kit.text_to_handwriting(var, rgb=[0,0,0])
    
#This Function can generate random credit card numbers
def cards():
    Digits = "01234567891"
    Card_Length = 11
    VBIN = "4677"
    MBIN = "5448"
    cmndtkr.speak("what should be the card holder name")
    Name = cmndtkr.takecommand().lower()
    # Name = input(">",)
    cn = "".join(random.sample(Digits, Card_Length))
    cmndtkr.speak("which card do you wnat to generate, visa or mastercard")
    options = cmndtkr.takecommand().lower()
    # options = input(">",)
    if "visa" in options:
        card_number = VBIN + cn
    elif "mastercard" in options:
        card_number = MBIN + cn
    else:
        cmndtkr.speak("please choose between visa and mastercard")
    cvv_length = 3
    CVV = "".join(random.sample(Digits, cvv_length))
    days = ("01","02","03","04","05","06","07",
            "08","09","10","11","12","13","14",
            "15","16","17","18","19","20","21",
            "22","23","24","25","26","27","28",
            "29","30","31")
    months = ("01","02","03","04","05","06","07",
              "08","09","10","11","12")
    years = ("2022", "2023", "2024", "2025", "2026",
             "2027", "2028", "2029", "2030")
    date_length = 1
    day = "".join(random.sample(days, date_length))
    month ="".join(random.sample(months, date_length))
    year = "".join(random.sample(years, date_length))
    divider = "/"
    expiry_date = day+divider+month+divider+year
    print("Name:", Name)
    print("Card Number:", card_number)
    print("C.V.V:", CVV)
    print("Expiry Date:", expiry_date)
    details = ['New Card Details:','Name:'+Name, 'Card Number:'+card_number,'CVV:'+CVV, 'Expiry Date:'+expiry_date]
    cmndtkr.speak("Your card has been generated")
    cmndtkr.speak("do you want to generate a text file of this card's details")
    answer = cmndtkr.takecommand().lower()
    # answer = input(">", )
    if 'yes' in answer:
        dir_path = Path('D:\Python Projects\Virtual AI\Brixpy\Cards')
        file_name = 'generated_cards.txt'
        # check if directory exists
        if dir_path.is_dir():
            with open (dir_path.joinpath(file_name),'a') as f:
                for item in details:
                    f.write(item +'\n')
                cmndtkr.speak("file updated")
        else:
            cmndtkr.speak("I could not generate the file as there is a directory issue")
    else:
        return 0


#This Function can send emails to anyone (working function)
def SendEmail(to, compose):
    msg = MIMEMultipart()
    msg['Subject'] = 'New Message From Brixpy Assistant'
    msg['From'] = "brixpyassistant@gmail.com"
    msg.attach(compose)
    UserName = "brixpyassistant@gmail.com"
    UserPassword = "F411EDE86A2AFC0EF8C011346E8DC2366E34"
    Server = "smtp.elasticemail.com"
    Port = "2525"
    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(UserName, UserPassword)
    s.sendmail(UserName, to, msg.as_string())
    s.quit()
    

        
#This Function can access the stored passwords of Wi-Fi profiles
def crackpass():
    getwifipass.wifipass()
    
#This is the Artificial Intelligence part of this project
def Ai():
    while True:
        query = cmndtkr.takecommand().lower()
        # query = input("enter the command: ", )
        if 'open notepad' in query:
            cmndtkr.speak("opening notepad")
            npath = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
        elif 'close notepad' in query:
            cmndtkr.speak('closing notepad')
            os.system('taskkill /f /im notepad.exe')
        elif 'cracker' in query:
            cmndtkr.speak("Opening password cracker")
            os.startfile('D:\\Python Projects\\Password_Cracker\\cracker.py')
        elif 'wi-fi password' in query:
            cmndtkr.speak('cracking into your home network')
            crackpass();
        elif 'wikipedia' in query:
            cmndtkr.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            cmndtkr.speak("According to Wikipedia")
            cmndtkr.speak(results)
        elif "convert text to hand writing" in query:
            cp.bolo("what text would you like to convert to hand writing")
            text = cp.shuno()
            text_to_hand(text)
        elif "calculate" in query:
            cmndtkr.speak("You did not build the calculator module")
        elif 'open youtube' in query:
            cmndtkr.speak('opening youtube')
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            cmndtkr.speak('opening google')
            webbrowser.open("www.google.com")
        elif 'open facebook' in query or 'open FB' in query or 'open friends book' in query:
            webbrowser.open('www.facebook.com')
        elif 'send an email' in query:
            cmndtkr.speak("whom do you want to send email")
            # contact = cmndtkr.takecommand().lower();
            contact = input(":>")
            if "huzaifa" in contact:
                try:
                    #cmndtkr.speak('what is the subject?')
                    #subject = cmndtkr.takecommand().lower()
                    cmndtkr.speak('what should i write?')
                    compose = MIMEText(cmndtkr.takecommand().lower())
                    to = "hamadahiro430@gmail.com"
                    SendEmail(to, compose)
                    cmndtkr.speak("email has been sent")
                except Exception as e:
                    cmndtkr.speak("sorry sir i was not able to send this email.")
                    print(e)
            elif "abbu" in contact:
                try:
                    #cmndtkr.speak("what is the subject?")
                    #subject = cmndtkr.takecommand().lower()
                    cmndtkr.speak('what should i write?')
                    compose = MIMEText(cmndtkr.takecommand().lower())
                    to = "kaowserhossain89@gmail.com"
                    SendEmail(to, compose)
                    cmndtkr.speak("email has been sent")
                except Exception as e:
                    cmndtkr.speak(
                        "sorry sir i was not able to send this email.")
                    print(e)
            elif "myself" in contact:
                try:
                    #cmndtkr.speak("what is the subject?")
                    #subject = cmndtkr.takecommand().lower()
                    cmndtkr.speak('what should i write?')
                    # content = cmndtkr.takecommand().lower()
                    compose = MIMEText(input("enter the content: "))
                    to = "mahfuzrahman038@gmail.com"
                    SendEmail(to, compose)
                    cmndtkr.speak("email has been sent")
                except Exception as e:
                    cmndtkr.speak(
                        "sorry sir i was not able to send this email.")
                    print(e)
        elif 'play a song' in query:
            cmndtkr.speak("which song do you want me to play?")
            song_name = cmndtkr.takecommand().lower()
            cmndtkr.speak(f"playing: {song_name}")
            kit.playonyt(song_name)
        elif 'tell me a joke' in query:
            joke = pyjokes.get_jokes();
            cmndtkr.speak(joke)
        elif 'switch window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        elif "tell me news" in query:
            cmndtkr.speak("fetching latest news")
            news()
        elif "generate credit card" in query:
            cards()
        elif  "quite" or "sleep" in query:
            cmndtkr.speak("okay sir")
            quit()
        else:
            cmndtkr.speak("Please say that again")
        break
    
if __name__ == '__main__':
    main()