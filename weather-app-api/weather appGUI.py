import requests
from tkinter import *
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 450

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

canvas = Canvas(window,height = HEIGHT,width = WIDTH)
canvas.pack()
bg_image = ImageTk.PhotoImage(Image.open("C:\\Users\\ASUS-PC\\AppData\\Local\\Programs\\Python\\Python36\\app.jpg")) 
bg_image_label = Label(canvas,image = bg_image)
bg_image_label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

#frame = Frame(window,bg='#5fa19e')
#frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

city_name_list=["Dhaka","Chittagong","Rajshahi","Barishal","Rangpur","Sylhet"]
city_listbox = StringVar(window)
city_listbox.set("Select the City")



output_frame = Frame(bg_image_label, bg='white', bd=10)
output_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')



weather_status_label = Label(output_frame,pady = 18,font=("times",14,"bold"),fg='#000')
weather_status_label.pack()

temprature_label = Label(output_frame,pady = 10,font=("times",14,"bold"),fg='#000')
temprature_label.pack()

humidity_label = Label(output_frame,pady = 12,font=("times",14,"bold"),fg='#000')
humidity_label.pack()

wind_speed_label = Label(output_frame,pady = 14,font=("times",14,"bold"),fg='#000')
wind_speed_label.pack()
    
option= OptionMenu(bg_image_label,city_listbox,*city_name_list)
option.pack()

button1= Button(bg_image_label,text="Check",width=15,command = weather)
button1.pack()

window.mainloop()

