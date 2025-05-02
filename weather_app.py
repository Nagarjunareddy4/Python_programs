import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import urllib.request
import io

# --- API Settings ---
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# --- Global Variables ---
recent_searches = []
use_celsius = True

# --- Functions ---
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    units = "metric" if use_celsius else "imperial"
    unit_symbol = "°C" if use_celsius else "°F"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": units
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            raise ValueError(data.get("message", "Error fetching weather"))

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        icon_code = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        city_name = data["name"]

        # Fetch icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        image_byt = urllib.request.urlopen(icon_url).read()
        image_buf = io.BytesIO(image_byt)
        image = Image.open(image_buf)
        photo = ImageTk.PhotoImage(image)
        weather_icon.config(image=photo)
        weather_icon.image = photo

        # Display data
        result = f"📍 {city_name}\n" \
                 f"🌡 Temperature: {temp}{unit_symbol}\n" \
                 f"☁ Weather: {weather}\n" \
                 f"💧 Humidity: {humidity}%\n" \
                 f"💨 Wind Speed: {wind} m/s"
        weather_output.config(text=result)

        update_recent(city_name)

    except Exception as e:
        weather_output.config(text="")
        weather_icon.config(image="")
        messagebox.showerror("Error", f"Could not fetch weather:\n{e}")

def update_recent(city):
    if city not in recent_searches:
        recent_searches.insert(0, city)
        if len(recent_searches) > 5:
            recent_searches.pop()
    recent_label.config(text="🕓 Recent: " + ", ".join(recent_searches))

def toggle_units():
    global use_celsius
    use_celsius = not use_celsius
    unit_button.config(text="Switch to °F" if use_celsius else "Switch to °C")
    if city_entry.get():
        get_weather()

# --- GUI Setup ---
window = tk.Tk()
window.title("Weather App")
window.geometry("400x500")
window.configure(bg="#e0f7fa")

# --- Entry ---
city_entry = tk.Entry(window, font=("Arial", 14), width=25, justify='center')
city_entry.pack(pady=20)

# --- Buttons ---
get_button = tk.Button(window, text="Get Weather", font=("Arial", 12),
                       command=get_weather, bg="#4db6ac", fg="white")
get_button.pack(pady=5)

unit_button = tk.Button(window, text="Switch to °F", font=("Arial", 10),
                        command=toggle_units, bg="#00796b", fg="white")
unit_button.pack(pady=5)

# --- Icon ---
weather_icon = tk.Label(window, bg="#e0f7fa")
weather_icon.pack()

# --- Output ---
weather_output = tk.Label(window, text="", font=("Arial", 12), justify="left", bg="#e0f7fa")
weather_output.pack(pady=15)

# --- Recent ---
recent_label = tk.Label(window, text="", font=("Arial", 10), fg="gray", bg="#e0f7fa")
recent_label.pack()

# --- Run App ---
window.mainloop()
