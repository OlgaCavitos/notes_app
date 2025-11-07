# import tkinter as t
# import datetime
# import requests
#
#
# class WeatherApp:
#     def __init__(self,master):
#         self.master = master
#         self.master.title("Weather App")
#         self.master.geometry("300x300")
#
#         self.label=t.Label(master,text="Enter the city name", font=("Arial",14))
#         self.label.pack(padx=10,pady=10)
#
#         self.entry=t.Entry(master,font=("Arial",12))
#         self.entry.pack(padx=10,pady=10)
#         self.entry.bind("<Return>", self.search_data)
#
#         self.button=t.Button(master,text="Search Weather", command=self.search_data,font=("Arial",14))
#         self.button.pack(padx=10,pady=10)
#
#         self.result_label=t.Label(master,text="Result",font=("Arial",14), justify="center")
#         self.result_label.pack(padx=10,pady=10)
#
#     def get_weather(self, city:str):
#         try:
#             url_weather=f"https://openweathermap.org/"
#             weather=requests.get(url_weather, timeout=5).json()
#             if "results" not in weather or not weather["weather"]:
#                 return f"No weather data for {city}"
#
#
#             latitude=weather["results"][0]["latitude"]
#             longitude=weather["results"][0]["longitude"]
#             city_name=weather["weather"][0]["name"]
#
#             url=f"https://openweathermap.org/"
#             data=requests.get(url,timeout=10).json()
#             current=data["current_weather"]
#
#             return (
#                 f"{city_name}\n\n"
#                 f" Temperature: {current[ 'temperature']}C\n"
#                 f" Wind Speed: {current[ 'wind']['speed']} km/h\n"
#                 f" Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#             )
#         except Exception as er:
#             return f"Error: {er}"
#
#     def save_to_file(self,text:str):
#         with open("weather.txt","a", encoding="utf-8") as f:
#             f.write(text + "\n" + "-"*40 + "\n")
#
#
#
#     def search_data(self, event=None):
#         city=self.entry.get().strip()
#         if not city:
#             self.result_label.config(text="Enter the city name")
#             return
#
#         result=self.get_weather(city)
#         self.result_label.config(text=result)
#
#         if not result.startswith("No weather data for ") and "not found" not in result:
#             self.save_to_file(result)
#
# if __name__ == "__main__":
#     root=t.Tk()
#     app=WeatherApp(root)
#     root.mainloop()



import datetime
import requests
import json


class WeatherApp:
    def __init__(self):
        self.output_file = "weather.txt"
        self.base_url = "https://wttr.in"

    def get_weather(self, city: str) -> str:
        try:
            url = f"{self.base_url}/{city}?format=j1"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                return f"[ERROR] Unable to fetch data for '{city}' (HTTP {response.status_code})"

            data = response.json()

            real_city = data["nearest_area"][0]["areaName"][0]["value"]

            if real_city.lower() != city.lower():
                return f"[WARNING] No exact match found for '{city}'. Closest location: {real_city}"


            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            weather_desc = current["weatherDesc"][0]["value"]
            humidity = current["humidity"]
            wind_speed = current["windspeedKmph"]

            result = (
                f"City: {real_city}\n"
                f"Weather: {weather_desc}\n"
                f"Temperature: {temp_c} °C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} km/h\n"
                f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            return result

        except requests.RequestException as err:
            return f"[ERROR] Network issue: {err}"
        except Exception as err:
            return f"[ERROR] Unexpected issue: {err}"

    def save_to_file(self, text: str):
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write(text + "\n" + "-" * 40 + "\n")

    def run(self):
        print("Weather App")
        print("Type a city name to get current weather data.")
        print("Type 'exit' to quit.\n")

        while True:
            city = input("Enter city name: ").strip()
            if city.lower() in ("exit", "quit"):
                break

            if not city:
                print("Please enter a city name.\n")
                continue

            result = self.get_weather(city)
            print("\n" + result + "\n")


            if not result.startswith(("[ERROR]", "[WARNING]")):
                self.save_to_file(result)
                print(f"Weather data saved to '{self.output_file}'\n")

if __name__ == "__main__":
    WeatherApp().run()



