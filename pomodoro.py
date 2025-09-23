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
        
        # Variables
        self.work_time = 25 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        self.long_break_time = 15 * 60  # 15 minutes in seconds
        self.current_time = self.work_time
        self.is_running = False
        self.is_break = False
        self.pomodoro_count = 0
        
        self.create_widgets()
        
        # Start the timer update
        self.update_timer()
        
        self.root.mainloop()
    
    def create_widgets(self):
        # Timer display
        self.timer_label = tk.Label(self.root, text="25:00", font=("Arial", 40))
        self.timer_label.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Work Time - Focus!", fg="red")
        self.status_label.pack(pady=5)
        
        # Pomodoro counter
        self.counter_label = tk.Label(self.root, text="Pomodoros: 0")
        self.counter_label.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Start button
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, width=8)
        self.start_button.grid(row=0, column=0, padx=5)
        
        # Pause button
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer, state="disabled", width=8)
        self.pause_button.grid(row=0, column=1, padx=5)
        
        # Reset button
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer, width=8)
        self.reset_button.grid(row=0, column=2, padx=5)
        
        # Skip button
        self.skip_button = tk.Button(button_frame, text="Skip", command=self.skip_session, width=8)
        self.skip_button.grid(row=0, column=3, padx=5)
    
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
        self.pause_button.config(state="normal")
    
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
    
    def reset_timer(self):
        self.is_running = False
        self.is_break = False
        self.current_time = self.work_time
        self.timer_label.config(text="25:00")
        self.status_label.config(text="Work Time - Focus!", fg="red")
        self.start_button.config(state="normal")
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
            self.status_label.config(text=f"{break_type} - Relax!", fg="green")
            
            messagebox.showinfo("Time's up!", f"Work session completed!\nTime for a {break_type.lower()}.")
        else:
            # Break completed
            self.current_time = self.work_time
            self.is_break = False
            self.timer_label.config(text="25:00")
            self.status_label.config(text="Work Time - Focus!", fg="red")
            
            messagebox.showinfo("Break over!", "Break time is over!\nTime to get back to work.")
        
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
    
    def play_alarm(self):
        # Play alarm sound
        for i in range(3):
            winsound.Beep(1000, 500)
            time.sleep(0.5)

# Run the application
if __name__ == "__main__":
    app = PomodoroTimer()