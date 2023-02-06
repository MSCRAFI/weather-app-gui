# making weather program using weatherapi and requests module
import requests as rq
from tkinter import Tk, Text, Button, Label, Frame, END
root = Tk()
root.title("Weather App")
root.geometry("600x200+400+200")


class weather:
    def __init__(self):
        # Base URL
        self.BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
        self.API_KEY = open("API.txt", "r").read()  # getting the API

    def get_weather(self):  # getting data as DICT
        self.URL = self.BASE_URL + self.API_KEY + "&q=" + self.location + "\
&aqi=yes"
        self.response_list = rq.get(self.URL).json()
        return self.response_list

    def print_info(self):
        self.response = self.get_weather()
        # getting the info from DICT and printing it using fstring
        self.print_weather = f"The location you selected is \
{self.response['location']['name']}, {self.response['location']['country']}\n\
and current temperature of your location is \
{self.response['current']['temp_c']}°C or {self.response['current']['temp_f']}\
°F.\nBut people in this location feeling like \
{self.response['current']['feelslike_c']}°C or \
{self.response['current']['feelslike_f']}°F."
        return self.print_weather

    def on_search_click(self):
        # getting the location from Text Box
        self.location = text_box.get(1.0, END)
        # adding print_weather on the label
        show_label.config(text=self.print_info())


wtr = weather()  # calling the class
# getting the actual location

# Text Box and Button
text_Frame = Frame(root)
text_Frame.grid(column=1, row=1, padx=50, pady=10)
text_box = Text(text_Frame, height=1, width=30, font="Times-New-Roman 18")
text_box.grid(column=1, row=1)
button = Button(text_Frame, text="Go", width=10, background="black", fg="\
white", font="Times-New-Roman 12 bold", command=wtr.on_search_click)
button.grid(column=2, row=1)

# Label
label_frame = Frame(root)
label_frame.grid(column=1, row=2)
show_label = Label(label_frame, text="", font="Times-New-Roman 11", justify="\
left")
show_label.grid(column=1, row=1)


root.mainloop()
