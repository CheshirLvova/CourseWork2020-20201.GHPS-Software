## підключення внутрішніх бібліотек
from libs import *

## підключення сторінок
from window import *
from page2_main_menu_page import *



def user_info():
        fileHandle = open ( 'hptemperature\\user_information.txt',"r" )
        lineList = fileHandle.readlines()
        fileHandle.close()
        messagebox.showinfo("Інформація про користувача", """IP-адреса:\t\t{0}
Контролер:\t\t{1}
Логін:\t\t{2}
Пароль:\t\t{3}""".format(lineList[0], lineList[1], lineList[2], lineList[3]))
        
