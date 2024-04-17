import tkinter as tk
import datetime
import wikipedia
import speech_recognition as sr
import os
import webbrowser
import pyttsx3

from LoopRunner import LoopRunner
from LoopRunner2 import LoopRunner2
from LoopRunner3 import LoopRunner3
from LoopRunner4 import LoopRunner4
from LoopRunner5 import LoopRunner5
from ManageAttendance import ManageAttendance
from ManageLab import ManageLab
from ManageLab2 import ManageLab2
from ManageLab3 import ManageLab3
from viewexcel import ViewExcel

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("AMS AI on this side! How may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Please Say Again")
        return "None"


def open_manage_attendance():
    speak("Opening Attendance for AIML")
    manage_attendance = ManageAttendance()
    manage_attendance.mainloop()


def open_em3():
    speak("Opening em3 attendance")
    em3_attendance = LoopRunner()
    em3_attendance.mainloop()


def open_dsgt():
    speak("Opening dsgt attendance")
    dsgt_attendance = LoopRunner2()
    dsgt_attendance.mainloop()


def open_cg():
    speak("Opening cg attendance")
    cg_attendance = LoopRunner3()
    cg_attendance.mainloop()


def open_ds():
    speak("Opening ds attendance")
    ds_attendance = LoopRunner4()
    ds_attendance.mainloop()


def open_dlcoa():
    speak("Opening dlcoa attendance")
    dlcoa_attendance = LoopRunner5()
    dlcoa_attendance.mainloop()


def open_second_year():
    codepath2 = "C:\\Users\paras\Downloads\DSE-AIML 2023.xlsx"
    os.startfile(codepath2)


def open_manage_lab():
    speak("Opening Lab Attendance")
    lab_attendance = ManageLab()
    lab_attendance.mainloop()


def open_manage_lab2():
    speak("Opening Lab Attendance For B2 Batch")
    lab_attendance2 = ManageLab2()
    lab_attendance2.mainloop()


def open_manage_lab3():
    speak("Opening Lab Attendance For B3 Batch")
    lab_attendance3 = ManageLab3()
    lab_attendance3.mainloop()


def view_excel():
    speak("Opening Excel Records")
    root = tk.Tk()  # Create a Tkinter root window
    excel_viewer = ViewExcel(root)  # Pass the root window as the master argument
    root.mainloop()



if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()

        # task execution logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'thank you' in query:
            speak("Your Welcome! Any More Info you would like to have?")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'instagram' in query:
            webbrowser.open("instagram.com")

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {str_time}")

        elif 'code' in query:
            codepath = "C:\\Users\paras\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'good' in query:
            speak("Thank you! Up For More!")

        elif 'music' in query:
            webbrowser.open("spotify.com")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif 'aiml' in query:
            open_manage_attendance()

        elif 'manage lab' in query:
            open_manage_lab()

        elif 'manage lab 2' in query:
            open_manage_lab2()

        elif 'manage lab 3' in query:
            open_manage_lab3()

        elif 'em3' in query:
            open_em3()

        elif 'dsgt' in query:
            open_dsgt()

        elif 'cg' in query:
            open_cg()

        elif 'ds' in query:
            open_ds()

        elif 'dlc' in query:
            open_dlcoa()

        elif "direct second year" in query:
            open_second_year()

        elif "kaisan ba" in query:
            speak("Thik Ba")

        elif 'excel' in query:
            view_excel()

    root = tk.Tk()
    root.title("AMS AI")
    root.geometry("400x300")

    em3_button = tk.Button(root, text="Open EM3 Attendance", command=open_em3)
    em3_button.pack()

    dsgt_button = tk.Button(root, text="Open DSGT Attendance", command=open_dsgt)
    dsgt_button.pack()

    cg_button = tk.Button(root, text="Open CG Attendance", command=open_cg)
    cg_button.pack()

    ds_button = tk.Button(root, text="Open DS Attendance", command=open_ds)
    ds_button.pack()

    dlcoa_button = tk.Button(root, text="Open DLCOA Attendance", command=open_dlcoa)
    dlcoa_button.pack()

    root.mainloop()
