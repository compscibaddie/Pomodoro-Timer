#importing the Time libraries for the timer
import tkinter as tk
from tkinter import ttk, messagebox
import time
import winsound
import threading

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 14))
        
        # Variables
        self.work_time = 25 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        self.long_break_time = 15 * 60  # 15 minutes in seconds
        self.current_time = self.work_time
        self.is_running = False
        self.is_break = False
        self.pomodoro_count = 0
        
        # Create UI
        self.create_widgets()
        
        # Start the timer update
        self.update_timer()
        
        self.root.mainloop()

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
    