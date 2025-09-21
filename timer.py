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

#creating the widgets for the timer
def create_widgets(self):
    self.timer_label = tkk.label(self.root, text="45:00", font=("Arial", 40))
    self.timer_label.pack(pady=20)

    #timer status label
    self.status_label = ttk.Label(self.root, text="Work Time - Focus", foreground="red") 
    self.status_label.pack(pady=5)

    #Timer Counter
    self.counter_label = ttk.Label(self.root, text="Pomodoros Completed: 0") 
    self.counter_label.pack(pady=5)

    #Button Frame
    button_frame = ttk.Frame(self.root)
    button_frame.pack(pady=20)

    #functional buttons
    #Start Button
    self.start_button = ttk.Button(button_frame, text="Start", command=self.start_timer)
    self.start_button.grid(row=0, column=0, padx=10)

    #Pause Button
    self.pause_button = ttk.Button(button_frame, text="Pause", command=self.pause_timer, state="disabled")
    self.pause_button.grid(row=0, column=1, padx=10)

    #Reset Button
    self.timer_button = tkk.button(button_frame, text="Reset", command=self.reset_timer)
    self.reset_button.grid(row=0, column=3, padx=10)

    #Skip Button
    self.skip_button = tkk.button(button_frame, text="Skip", command=self.skip_timer)
    self.skip_button.grid(row=0, column=3, padx=10)

#Creating the methods
    def update_timer(self):
            if self.is_running:
                self.current_time -= 1
                
                # Format time as minutes:seconds
                minutes = self.current_time // 60
                seconds = self.current_time % 60
                self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                
                # Check if timer reached zero
                if self.current_time <= 0:
                    self.timer_complete()
            
            # Schedule the next update
            self.root.after(1000, self.update_timer)
    
    def start_timer(self):
        self.is_running = True
        self.start_button.config(state="disabled")
        self.pause_button.config(state="enabled")
    
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state="enabled")
        self.pause_button.config(state="disabled")
    
    def reset_timer(self):
        self.is_running = False
        self.is_break = False
        self.current_time = self.work_time
        self.timer_label.config(text="25:00")
        self.status_label.config(text="Work Time - Focus!", foreground="red")
        self.start_button.config(state="enabled")
        self.pause_button.config(state="disabled")
    
    def skip_session(self):
        self.timer_complete()
    
    def timer_complete(self):
        self.is_running = False
        
        # Play alert sound
        threading.Thread(target=self.play_alarm).start()
        
        if not self.is_break:
            # Work session completed
            self.pomodoro_count += 1
            self.counter_label.config(text=f"Pomodoros: {self.pomodoro_count}")
            
            # Determine break type
            if self.pomodoro_count % 4 == 0:
                self.current_time = self.long_break_time
                break_type = "Long Break"
            else:
                self.current_time = self.break_time
                break_type = "Short Break"
            
            self.is_break = True
            minutes = self.current_time // 60
            self.timer_label.config(text=f"{minutes:02d}:00")
            self.status_label.config(text=f"{break_type} - Relax!", foreground="green")
            
            messagebox.showinfo("Time's up!", f"Work session completed!\nTime for a {break_type.lower()}.")
        else:
            # Break completed
            self.current_time = self.work_time
            self.is_break = False
            self.timer_label.config(text="25:00")
            self.status_label.config(text="Work Time - Focus!", foreground="red")
            
            messagebox.showinfo("Break over!", "Break time is over!\nTime to get back to work.")
        
        self.start_button.config(state="enabled")
        self.pause_button.config(state="disabled")
    
    def play_alarm(self):
        # Play alarm sound
        for i in range(3):
            winsound.Beep(1000, 500)
            time.sleep(0.5)