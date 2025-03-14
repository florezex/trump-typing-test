import tkinter as tk
from tkinter import messagebox, font
import random
import time

class TypingSpeedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Typing Speed Test")
        self.root.geometry("900x500")
        self.root.configure(bg='#E8F4F9')  # Light blue background
        
        self.sample_texts = [
            "Despite the negative press covfefe.",
            "I will build a great wall and nobody builds walls better than me.",
            "I think I am actually humble. I think I'm much more humble than you would understand.",
            "I have a very good brain and I've said a lot of things.",
            "I know words, I have the best words.",
            "Nobody knew health care could be so complicated.",
            "I'm really rich. I'll show you that in a second.",
            "All of the women on The Apprentice flirted with me - consciously or unconsciously. That's to be expected.",
            "My IQ is one of the highest - and you all know it.",
            "Sorry losers and haters, but my IQ is one of the highest - and you all know it!"
        ]
        
        self.current_text = ""
        self.start_time = None
        self.game_started = False
        
        # Create a modern style frame
        self.main_frame = tk.Frame(root, bg='#E8F4F9', padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')
        
        # Custom font configurations
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.text_font = font.Font(family="Helvetica", size=16)
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        
        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Modern Typing Speed Test",
            font=self.title_font,
            bg='#E8F4F9',
            fg='#2C3E50'
        )
        self.title_label.pack(pady=(0, 30))
        
        # Text display with better contrast
        self.text_display = tk.Label(
            self.main_frame,
            text="Click 'Start' to begin the typing test!",
            wraplength=800,
            font=self.text_font,
            bg='#FFFFFF',
            fg='#2C3E50',
            pady=20,
            padx=20
        )
        self.text_display.pack(fill='x', pady=(0, 20))
        
        # Modern entry field
        self.entry = tk.Entry(
            self.main_frame,
            font=self.text_font,
            state='disabled',
            width=50,
            bg='#FFFFFF',
            fg='#2C3E50',
            insertbackground='#2C3E50'
        )
        self.entry.pack(pady=20)
        
        # Stylish button
        self.start_button = tk.Button(
            self.main_frame,
            text="Start",
            command=self.start_game,
            font=self.button_font,
            bg='#3498DB',
            fg='white',
            activebackground='#2980B9',
            activeforeground='white',
            relief='flat',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        self.start_button.pack(pady=20)
        
        # Stats with modern styling
        self.stats_label = tk.Label(
            self.main_frame,
            text="WPM: 0 | Accuracy: 0%",
            font=self.text_font,
            bg='#E8F4F9',
            fg='#2C3E50'
        )
        self.stats_label.pack(pady=10)
        
        # Bind hover effects
        self.start_button.bind('<Enter>', lambda e: self.start_button.config(bg='#2980B9'))
        self.start_button.bind('<Leave>', lambda e: self.start_button.config(bg='#3498DB'))
        
    def start_game(self):
        self.current_text = random.choice(self.sample_texts)
        self.text_display.config(text=self.current_text)
        self.entry.delete(0, tk.END)
        self.entry.config(state='normal')
        self.entry.focus()
        self.start_time = time.time()
        self.game_started = True
        self.start_button.config(state='disabled')
        self.entry.bind('<Return>', self.end_game)
        
    def calculate_wpm(self, time_taken, typed_text):
        words = len(typed_text.split())
        minutes = time_taken / 60
        return int(words / minutes)
    
    def calculate_accuracy(self, original_text, typed_text):
        if len(typed_text) == 0:
            return 0
        
        correct_chars = sum(1 for a, b in zip(original_text, typed_text) if a == b)
        accuracy = (correct_chars / len(original_text)) * 100
        return round(accuracy, 1)
    
    def end_game(self, event=None):
        if not self.game_started:
            return
            
        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.entry.get()
        
        wpm = self.calculate_wpm(time_taken, typed_text)
        accuracy = self.calculate_accuracy(self.current_text, typed_text)
        
        self.stats_label.config(text=f"WPM: {wpm} | Accuracy: {accuracy}%")
        self.entry.config(state='disabled')
        self.start_button.config(state='normal')
        self.game_started = False
        
        # Modern styled message box
        self.root.after(100, lambda: messagebox.showinfo(
            "Results",
            f"Time: {time_taken:.1f} seconds\nWPM: {wpm}\nAccuracy: {accuracy}%"
        ))

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingSpeedGame(root)
    root.mainloop()
