from tkinter import *
import tkinter as tk
from geopy.geocoders import nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image
from tkinter import Tk

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

Search_image = PhotoImage(file="PNG File (.png)")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)
Search_image = PhotoImage(file="C://Users//Rehan//Downloads//your_image.png")


root.mainloop()



