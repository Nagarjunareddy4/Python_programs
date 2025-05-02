# Digital Clock with Location Display
# This script creates a digital clock GUI using Tkinter that displays the current time, date, and user location based on IP address.
import tkinter as tk
import time
import requests

# Function to get user location using IP
def get_location():
    try:
        response = requests.get("http://ip-api.com/json")
        data = response.json()
        city = data.get("city", "Unknown")
        country = data.get("country", "")
        return f"{city}, {country}"
    except:
        return "Location Unavailable"

# Function to update time and date
def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    current_date = time.strftime("%A, %d %B %Y")  # Full weekday, day, month, year
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_time)

# GUI Setup
window = tk.Tk()
window.title("Digital Clock with Location")
window.geometry("420x250")
window.configure(bg="#1e1e1e")

# Location Label
location = get_location()
location_label = tk.Label(window, text=location, font=("Arial", 14), fg="white", bg="#1e1e1e")
location_label.pack(pady=5)

# Clock Label
clock_label = tk.Label(window, font=("Arial", 50), fg="#00FFCC", bg="#1e1e1e")
clock_label.pack(pady=10)

# Date Label
date_label = tk.Label(window, font=("Arial", 18), fg="#FFA500", bg="#1e1e1e")
date_label.pack()

# Start Clock
update_time()

# Run the App
window.mainloop()
