#importing the Time libraries for the timer
import tkinter as tk
from tkinter import ttk, messagebox
import time
import winsound
import threading



    #main script information
    while True:
        t_now = dt.datetime.now()
    
        if t_now < t_fut:
            # Pomodoro in progress - block websites
            add_websites(host_path)
            print(f"Pomodoro in progress... {t_fut - t_now} remaining")
        
        elif t_fut <= t_now <= t_fin:
            # Break time - unblock websites
            remove_websites(host_path)
            print('Break time!')
        
        else:
            # Pomodoro finished
            remove_websites(host_path)
            print('\a')
            
            for i in range(10):
                winsound.Beep((i+100), 500)
                
            total_pomodoros += 1
            usr_ans = messagebox.askyesno("Pomodoro finished!", 
                                        f"Completed {total_pomodoros} pomodoros.\nDo you want to start another Pomodoro?")
            
            if usr_ans:
                # Reset timer for another pomodoro
                t_now = dt.datetime.now()
                t_fut = t_now + dt.timedelta(0, t_pom)
                t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)
                messagebox.showinfo("Pomodoro started!", 
                                f"It is now {t_now.strftime('%H:%M')} hrs. \nTimer is set for 25 minutes")
                continue
            else:
                print(f"Total pomodoros completed: {total_pomodoros}")
                break
            
    time.sleep(20)
t_now = dt.datetime.now()
timenow = t_now.strftime("%H:%M")
print('\n\nMade it to the end!\n\n')
    