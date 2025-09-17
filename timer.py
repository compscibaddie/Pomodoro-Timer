#importing the Time libraries for the timer
import time
import datetime as dt

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import windsound

#hinding the main window functionality
root = tkinter.Tk()
root.withdraw()

host_path = r"C:\Windows\System32\drivers\etc"
redirect_path = "127.0.0.1"

print("-"*40+f"\nCurrent host path is: {host_path}\n"+"-"*40)

website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.twitter.com", "twitter.com"]

total_pomodoros = 0

#collecting Time information
t_now = dt.datetime.now()
t_pom = 25*60
t_delta = dt.timedelta(0, t_pom)

t_fut = t_now + t_delta
delta_sec = 1#60
t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)

#running main loop, to block all sites while the timer is running

def add_websites(filepath):
    with open(filepath+"\hosts", "r+") as dummy_file:
        content = dummy_file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                dummy_file.write(redirect_path+" "+website+"\n")
