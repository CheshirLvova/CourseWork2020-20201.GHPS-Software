## підключення внутрішніх бібліотек
from libs import *
## підключення бібліотек для виконання основних функцій
from temperature_outside import *

# кольори
background_color = "#E3E2DE"
main_color = "#E5E4E1"
active_color = "#F2F1ED"
white_color="#ffffff"

## створення вікна та загальні налаштування
root = Tk()
root.title("ПЗ для користувацього контролю системи геотермальних теплових насосів")
root.iconbitmap('icons\program.ico')
root.wm_geometry("1080x720+0+0")# розмір = ширина х висота + початкова_точка_х + початкова_точка_у
root.configure(bg=background_color)

# іконки для панелі управління (sizex32)
icon1 = PhotoImage(file = r"icons\connect.png")
icon2 = PhotoImage(file = r"icons\openLog.png")
icon3 = PhotoImage(file = r"icons\house.png")
icon4 = PhotoImage(file = r"icons\mountain.png")
icon5 = PhotoImage(file = r"icons\house.png")
icon6 = PhotoImage(file = r"icons\shower.png")
icon7 = PhotoImage(file = r"icons\arrows.png")
icon8 = PhotoImage(file = r"icons\temperature.png")

icon9 = PhotoImage(file = r"icons\analytics.png")
icon10 = PhotoImage(file = r"icons\sliders.png")
icon11 = PhotoImage(file = r"icons\speed.png")
icon12 = PhotoImage(file = r"icons\calendar.png")
icon13 = PhotoImage(file = r"icons\choice.png")

icon14 = PhotoImage(file = r"icons\rewindTime.png")

icon15 = PhotoImage(file = r"icons\update.png")
icon16 = PhotoImage(file = r"icons\back.png")

icon17 = PhotoImage(file = r"icons\backtomain.png")
image1 = PhotoImage(file=r'heat_pump_elements\heatpumpsystem.png')
image2 = PhotoImage(file=r'icons\notFound.png')


