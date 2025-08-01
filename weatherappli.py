import requests
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return {
            "weather": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

def show_weather():
    api_key = "ff02e1cefe13e59d5e0aa6665cfc2feb"
    city = city_entry.get()
    try:
        weather_data = get_weather(api_key, city)
        result_text.set(
            f"Weather in {city}:\n"
            f"Condition: {weather_data['weather'].title()}\n"
            f"Temperature: {weather_data['temperature']} °C\n"
            f"Humidity: {weather_data['humidity']} %\n"
            f"Wind Speed: {weather_data['wind_speed']} m/s\n"
            f"Time: {weather_data['time']}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Weather App")
root.geometry("420x360")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", font=("Segoe UI", 11))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)

ttk.Label(main_frame, text="Enter City Name:").pack(pady=5)
city_entry = ttk.Entry(main_frame, width=30)
city_entry.pack(pady=5)

ttk.Button(main_frame, text="Get Weather", command=show_weather).pack(pady=15)

result_text = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_text, justify="left", anchor="center", background="white", relief="solid", padding=10)
result_label.pack(fill="both", expand=True, pady=10)

root.mainloop()
