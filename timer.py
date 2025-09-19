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

  