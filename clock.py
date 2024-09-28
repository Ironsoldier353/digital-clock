import tkinter as tk
import time

def update_time():

    current_time = time.strftime("%H:%M:%S")
  
    clock_label.config(text=current_time)

    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(pady=10, padx=10)


update_time()

root.mainloop()
