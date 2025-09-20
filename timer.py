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