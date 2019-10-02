import tkinter as tk
import requests
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Weather 2.0")
HEIGHT = 500
WIDTH = 600

def format_response(output):
    try:
        city = output['name']
        weather_status = output['weather'][0]['description']
        temprature = output['main']['temp']
        humidity = output['main']['humidity']
        wind_speed=output['wind']['speed']
        final_str = (f"\tCity: {city} \n\tConditions: {weather_status} \n\tTemperature (°C):{temprature} \n\tHumidity:{humidity}\n\tWind Speed: {wind_speed}")
    except:
        final_str = 'There was a problem retrieving that information'
    
    return final_str


def weather(city):
    url = (f"https://openweathermap.org/data/2.5/weather?q={city}&appid=b6907d289e10d714a6e88b30761fae22")
    response = requests.get(url)
    print(response.json())
    output = response.json()

    results['text'] = format_response(output)

C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background_image= ImageTk.PhotoImage(Image.open("C:\\Users\\ASUS-PC\\AppData\\Local\\Programs\\Python\\Python36\\app.jpg"))
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

frame = tk.Frame(app,  bg='#0d3d57', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Load Data', font=40, command=lambda: weather(textbox.get()))
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#0d3d57', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)






app.mainloop()
