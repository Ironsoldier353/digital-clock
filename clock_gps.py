import tkinter as tk
import requests
import time

def get_location_time():
    try:
        # Get time from World Time API based on IP
        response = requests.get('http://worldtimeapi.org/api/ip')
        if response.status_code == 200:
            data = response.json()
            # Extracting only the time part from the datetime string
            current_time = data['datetime'][11:19]  
            return current_time
        else:
            return "Error"
    except Exception as e:
        print(f"Error retrieving time: {e}")
        return "Error"

def update_time():
    # Fetch the current time from World Time API
    current_time = get_location_time()
    
    # Update the label with the fetched time
    clock_label.config(text=current_time)
    
    # Refresh the time every second (1000ms)
    clock_label.after(1000, update_time)

# Initialize Tkinter window
root = tk.Tk()
root.title("Digital Clock with Geo-based Time")

# Configure the clock label
clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(pady=10, padx=10)

# Start the clock update loop
update_time()

# Run the Tkinter event loop
root.mainloop()
