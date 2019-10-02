import requests
from tkinter import *
from PIL import ImageTk, Image


def weather():
    city = city_listbox.get() #get the city selected by user
    api_url = (f"https://openweathermap.org/data/2.5/weather?q={city}&appid=b6907d289e10d714a6e88b30761fae22")
    response = requests.get(api_url)
    output = response.json()

    #p_key = output['weather'][0]['id']
    weather_status = output['weather'][0]['description']
    temprature = output['main']['temp']
    humidity = output['main']['humidity']
    wind_speed=output['wind']['speed']

    weather_status_label.configure(text="Weather Status: "+ weather_status)
    temprature_label.configure(text="Temprature: "+ str(temprature)+ "*C")
    humidity_label.configure(text="Humidity: "+ str(humidity))
    wind_speed_label.configure(text="Wind Speed: "+ str(wind_speed))

    #print(p_key)

window = Tk()
window.title("Weather App")
window.geometry = ("500x450")
bg_image = ImageTk.PhotoImage(Image.open("app.jpg")) 
bg_image_label = Label (image = bg_image)
bg_image_label.pack()
       

city_name_list=["Dhaka","Chittagong","Rajshahi","Barishal","Rangpur","Sylhet"]
city_listbox = StringVar(window)
city_listbox.set("Select the City")


option= OptionMenu(window,city_listbox,*city_name_list)
option.pack()

button1= Button(window,text="Check",width=15,command = weather,border=1)
button1.pack()

weather_status_label = Label(window,font=("times",10,"bold"))
weather_status_label.pack()

temprature_label = Label(window,font=("times",10,"bold"))
temprature_label.pack()

humidity_label = Label(window,font=("times",10,"bold"))
humidity_label.pack()

wind_speed_label = Label(window,font=("times",10,"bold"))
wind_speed_label.pack()
    

window.mainloop()

