import tkinter as tk
from tkinter import ttk, messagebox
import time
import winsound
import threading

class MyMelodyPomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Melody Pomodoro Timer ♡")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg='#FFEBF3')  # Light pink background
        
        # My Melody color scheme
        self.colors = {
            'bg': '#FFEBF3',        # Light pink background
            'primary': '#FF9ECB',    # Medium pink
            'secondary': '#FF66A3',  # Dark pink
            'accent': '#FFFFFF',     # White
            'text': '#8A4F6B',       # Dark pink text
            'work': '#FF6B93',       # Work timer color
            'break': '#9ED8FF'       # Break timer color (light blue like My Melody's hood)
        }
        
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
        # Header with My Melody theme
        header_frame = tk.Frame(self.root, bg=self.colors['bg'])
        header_frame.pack(pady=10)
        
        title_label = tk.Label(header_frame, text="♡ My Melody Pomodoro Timer ♡", 
                              font=("Comic Sans MS", 18, "bold"), 
                              fg=self.colors['text'], bg=self.colors['bg'])
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame, text="Stay focused with My Melody! ✨", 
                                 font=("Comic Sans MS", 10), 
                                 fg=self.colors['secondary'], bg=self.colors['bg'])
        subtitle_label.pack()
        
        # Timer display with cute frame
        timer_frame = tk.Frame(self.root, bg=self.colors['primary'], relief='raised', bd=3)
        timer_frame.pack(pady=15, padx=20, fill='x')
        
        self.timer_label = tk.Label(timer_frame, text="25:00", 
                                   font=("Arial Rounded MT Bold", 48), 
                                   fg=self.colors['accent'], bg=self.colors['primary'])
        self.timer_label.pack(pady=15)
        
        # Status label with cute styling
        self.status_label = tk.Label(self.root, text="Work Time - Let's focus! 💖", 
                                    font=("Comic Sans MS", 14, "bold"), 
                                    fg=self.colors['work'], bg=self.colors['bg'])
        self.status_label.pack(pady=5)
        
        # Pomodoro counter with flower decoration
        counter_frame = tk.Frame(self.root, bg=self.colors['bg'])
        counter_frame.pack(pady=5)
        
        self.counter_label = tk.Label(counter_frame, text="🌸 Pomodoros Completed: 0 🌸", 
                                     font=("Comic Sans MS", 12), 
                                     fg=self.colors['text'], bg=self.colors['bg'])
        self.counter_label.pack()
        
        # Button frame with cute rounded buttons
        button_frame = tk.Frame(self.root, bg=self.colors['bg'])
        button_frame.pack(pady=20)
        
        # Start button
        self.start_button = self.create_cute_button(button_frame, "Start ✨", self.start_timer, 0, 0)
        
        # Pause button
        self.pause_button = self.create_cute_button(button_frame, "Pause 🌸", self.pause_timer, 0, 1)
        self.pause_button.config(state="disabled")
        
        # Reset button
        self.reset_button = self.create_cute_button(button_frame, "Reset 🔄", self.reset_timer, 0, 2)
        
        # Skip button
        self.skip_button = self.create_cute_button(button_frame, "Skip ⏩", self.skip_session, 0, 3)
        
        # Footer with My Melody signature
        footer_label = tk.Label(self.root, text="💕 Keep smiling with My Melody! 💕", 
                               font=("Comic Sans MS", 9), 
                               fg=self.colors['secondary'], bg=self.colors['bg'])
        footer_label.pack(side='bottom', pady=10)
    
    def create_cute_button(self, parent, text, command, row, column):
        button = tk.Button(parent, text=text, command=command, 
                          font=("Comic Sans MS", 10, "bold"),
                          bg=self.colors['secondary'], fg=self.colors['accent'],
                          activebackground=self.colors['primary'], 
                          activeforeground=self.colors['accent'],
                          relief='raised', bd=3, padx=15, pady=8,
                          cursor='heart')
        button.grid(row=row, column=column, padx=8)
        return button
    
    def update_timer(self):
        if self.is_running:
            self.current_time -= 1
            
            # Format time as minutes:seconds
            minutes = self.current_time // 60
            seconds = self.current_time % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            
            # Update progress color (gets darker as time decreases)
            progress = self.current_time / (self.work_time if not self.is_break else self.break_time)
            if self.is_break:
                r = int(158 * progress)  # Blue component for breaks
                g = int(216 * progress)
                b = int(255)
                color = f'#{r:02x}{g:02x}{b:02x}'
            else:
                r = 255
                g = int(107 + (148 * (1 - progress)))  # Pink to red gradient
                b = int(147 + (108 * (1 - progress)))
                color = f'#{r:02x}{g:02x}{b:02x}'
            
            self.timer_label.config(bg=color)
            
            # Check if timer reached zero
            if self.current_time <= 0:
                self.timer_complete()
        
        # Schedule the next update
        self.root.after(1000, self.update_timer)
    
    def start_timer(self):
        self.is_running = True
        self.start_button.config(state="disabled", bg='#CCCCCC')
        self.pause_button.config(state="normal", bg=self.colors['secondary'])
        self.status_label.config(text="⏰ Timer running... Stay focused! 💖")
    
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state="normal", bg=self.colors['secondary'])
        self.pause_button.config(state="disabled", bg='#CCCCCC')
        self.status_label.config(text="⏸️ Timer paused - Ready when you are! 🌸")
    
    def reset_timer(self):
        self.is_running = False
        self.is_break = False
        self.current_time = self.work_time
        self.timer_label.config(text="25:00", bg=self.colors['primary'])
        self.status_label.config(text="Work Time - Let's focus! 💖", fg=self.colors['work'])
        self.start_button.config(state="normal", bg=self.colors['secondary'])
        self.pause_button.config(state="disabled", bg='#CCCCCC')
    
    def skip_session(self):
        self.timer_complete()
    
    def timer_complete(self):
        self.is_running = False
        
        # Play cute alarm sound
        threading.Thread(target=self.play_cute_alarm).start()
        
        if not self.is_break:
            # Work session completed
            self.pomodoro_count += 1
            self.counter_label.config(text=f"🌸 Pomodoros Completed: {self.pomodoro_count} 🌸")
            
            # Determine break type
            if self.pomodoro_count % 4 == 0:
                self.current_time = self.long_break_time
                break_type = "Long Break"
                emoji = "🎉"
            else:
                self.current_time = self.break_time
                break_type = "Short Break"
                emoji = "☕"
            
            self.is_break = True
            minutes = self.current_time // 60
            self.timer_label.config(text=f"{minutes:02d}:00", bg=self.colors['break'])
            self.status_label.config(text=f"{break_type} - Time to relax! {emoji}", fg=self.colors['break'])
            
            messagebox.showinfo("Yay! Work Complete! 🎀", 
                              f"Great job! You finished a work session! 💖\n\nTime for a {break_type.lower()}! {emoji}\n\nMy Melody is proud of you! 🌸")
        else:
            # Break completed
            self.current_time = self.work_time
            self.is_break = False
            self.timer_label.config(text="25:00", bg=self.colors['primary'])
            self.status_label.config(text="Work Time - Let's focus! 💖", fg=self.colors['work'])
            
            messagebox.showinfo("Break Time Over! ⏰", 
                              "Break time is over! 🌸\n\nLet's get back to work with My Melody! 💕\n\nYou can do it! ✨")
        
        self.start_button.config(state="normal", bg=self.colors['secondary'])
        self.pause_button.config(state="disabled", bg='#CCCCCC')
    
    def play_cute_alarm(self):
        # Play cute alarm sound (higher pitch for My Melody theme)
        for i in range(3):
            winsound.Beep(1200 + i*100, 400)  # Cute high-pitched beeps
            time.sleep(0.3)

# Run the application
if __name__ == "__main__":
    app = MyMelodyPomodoroTimer()