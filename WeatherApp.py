import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Units can be metric or imperial

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        result_text.set(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:\n"
                        f"Temperature: {weather_data['main']['temp']}°C\n"
                        f"Description: {weather_data['weather'][0]['description']}\n"
                        f"Humidity: {weather_data['main']['humidity']}%\n"
                        f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        result_text.set("Weather data not available.")

def get_weather_info():
    city = city_entry.get()
    if city:
        weather_data = get_weather(api_key_entry.get(), city)
        display_weather(weather_data)
    else:
        messagebox.showinfo("Input Error", "Please enter a city.")

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
api_key = "YOUR_API_KEY"

# GUI setup
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

# Entry for API key
api_key_label = tk.Label(app, text="Enter OpenWeatherMap API Key:")
api_key_label.pack(pady=10)
api_key_entry = tk.Entry(app, show="*", width=30)
api_key_entry.pack(pady=5)

# Entry for city name
city_label = tk.Label(app, text="Enter City Name:")
city_label.pack(pady=10)
city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

# Button to get weather information
get_weather_button = tk.Button(app, text="Get Weather Info", command=get_weather_info, bg="blue", fg="white")
get_weather_button.pack(pady=10)

# Display weather information
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Helvetica", 12), wraplength=300)
result_label.pack(pady=10)

app.mainloop()
