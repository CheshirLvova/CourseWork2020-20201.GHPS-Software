## підключення внутрішніх бібліотек
from window import *
from random import randint

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open('hptemperature\\selected.txt', "w") as result_file:
        result_file.write(f'{filepath}')
    page8()
    
def open_site():
    webbrowser.open("https://github.com/CheshirLvova/CourseWork2020-2021.GHPS-Software")

def temp_inside():
    frame=Frame(root,bg=main_color)
    frame.place(relx=0.33,rely=0.15,relheight=0.19,relwidth=0.16)
    frame.columnconfigure(0, minsize=30)
    frame.columnconfigure(1, minsize=30)
    frame.columnconfigure(2, minsize=20)
    frame.rowconfigure(0, minsize=1)
    frame.rowconfigure(1, minsize=10)
    frame.rowconfigure(2, minsize=3)
    frame.rowconfigure(3, minsize=3)
    lbl01 = Label(frame, text="Встановити",bg=main_color).grid(row=0, column=0, padx = 8, pady = 5)
    spin0 = Spinbox(frame, from_=0, to=35, width=5)  
    spin0.grid(row = 1, column = 0, padx = 4, pady = 5)
    spin1 = Spinbox(frame, from_=0, to=99, width=5)  
    spin1.grid(row = 1, column = 1, padx = 4, pady = 5)
    lbl02 = Label(frame, text="°C",bg=main_color).grid(row=1, column=2, padx = 10, pady = 5, sticky='nsew')
    def clicked():
        with open('hptemperature\\temp_in.txt', 'a') as result_file:
            if int(spin1.get()) < 10: 
                result_file.write(f'\n{int(spin0.get())}.0{int(spin1.get())}')
            else:
                result_file.write(f'\n{int(spin0.get())}.{int(spin1.get())}')
        main_page()
    btnOK = Button(frame, height=1, width=1, text="OK", command=clicked).grid(row=2, column=0, columnspan=3, padx = 10, pady = 5, sticky='nsew')
    btnCancel = Button(frame, height=1, width=1, text="Повернутись", command=main_page).grid(row=3, column=0, columnspan=3, padx = 10, pady = 5, sticky='nsew')

def temp_boiler():
    frame=Frame(root,bg=main_color)
    frame.place(relx=0.39,rely=0.15,relheight=0.19,relwidth=0.16)
    frame.columnconfigure(0, minsize=30)
    frame.columnconfigure(1, minsize=30)
    frame.columnconfigure(2, minsize=20)
    frame.rowconfigure(0, minsize=1)
    frame.rowconfigure(1, minsize=10)
    frame.rowconfigure(2, minsize=3)
    frame.rowconfigure(3, minsize=3)
    lbl01 = Label(frame, text="Встановити",bg=main_color).grid(row=0, column=0, padx = 8, pady = 5)
    spin0 = Spinbox(frame, from_=0, to=89, width=5)  
    spin0.grid(row = 1, column = 0, padx = 4, pady = 5)
    spin1 = Spinbox(frame, from_=0, to=99, width=5)  
    spin1.grid(row = 1, column = 1, padx = 4, pady = 5)
    lbl02 = Label(frame, text="°C",bg=main_color).grid(row=1, column=2, padx = 10, pady = 5, sticky='nsew')
    def clicked():
        with open('hptemperature\\temp_boiler.txt', 'a') as result_file:
            if int(spin1.get()) < 10: 
                result_file.write(f'\n{int(spin0.get())}.0{int(spin1.get())}')
            else:
                result_file.write(f'\n{int(spin0.get())}.{int(spin1.get())}')
        main_page()
    btnOK = Button(frame, height=1, width=1, text="OK", command=clicked).grid(row=2, column=0, columnspan=3, padx = 10, pady = 5, sticky='nsew')
    btnCancel = Button(frame, height=1, width=1, text="Повернутись", command=main_page).grid(row=3, column=0, columnspan=3, padx = 10, pady = 5, sticky='nsew')
        
def main_page():
    frame=Frame(root)
    frame.place(relx=0,rely=0.035,relheight=1,relwidth=1)
    nb = ttk.Notebook(frame)
    nb.grid(row=0, column=0, columnspan=3)

    # Add first tab
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)

    #tab1.grid(row=0, column=0)
    nb.add(tab1, text='Головна')
    nb.add(tab2, text='Сервіс')

    # Change the sizes of the columns equally
    tab1.columnconfigure(0, minsize=70)
    tab1.columnconfigure(1, minsize=5)
    tab1.columnconfigure(2, minsize=70)
    tab1.columnconfigure(3, minsize=5)
    tab1.columnconfigure(4, minsize=70)
    tab1.columnconfigure(5, minsize=5)
    tab1.columnconfigure(6, minsize=70)
    tab1.columnconfigure(7, minsize=70)
    tab1.columnconfigure(8, minsize=70)
    tab1.columnconfigure(9, minsize=70)
    tab1.columnconfigure(10, minsize=5)
    tab1.columnconfigure(11, minsize=70)
    tab1.columnconfigure(12, minsize=5)
    tab1.columnconfigure(13, minsize=100)
    tab1.columnconfigure(14, minsize=100)
    tab1.columnconfigure(15, minsize=5)
    tab1.columnconfigure(16, minsize=90)
    tab1.columnconfigure(17, minsize=5)
    tab1.columnconfigure(18, minsize=990)

    tab2.columnconfigure(0, minsize=70)
    tab2.columnconfigure(1, minsize=5)
    tab2.columnconfigure(2, minsize=70)
    tab2.columnconfigure(3, minsize=5)
    tab2.columnconfigure(4, minsize=1770)

    #tab1
    bt1=Button(tab1,text='Відключити', image = icon1, compound = TOP, borderwidth = 0, command=None)
    bthint1 = Hovertip(bt1,'дозволяє відключити ПЗ від системи ГТН, \nякщо користувач підключений \n(повернення на сторінку входу)')
    bt1.grid(row=0, column=0, rowspan=3, padx = 5, pady = 5)
    
    separator0 = ttk.Separator(tab1, orient='vertical')
    separator0.grid(column=1, row=0, rowspan=3, sticky='ns')
    
    lbl1 = Label(tab1, text="Головна").grid(row=3, column=0, columnspan=3, padx = 0, pady = 1)

    bt2=Button(tab1,text='Відкрити базу', image = icon2, compound = TOP, borderwidth = 0, command=open_file)
    bthint2 = Hovertip(bt2,'дозволяє відкрити бекапи, \nщо містяться на пристрої для \nвідображення статистики за обраний користувачем \nперіод \n\n(для відображення функціоналу спробуйте запустити файл \n\"temp_plot.txt\", який міститься у папці ПЗ).')
    bt2.grid(row=0, column=2, rowspan=3, padx = 5, pady = 5)

    separator1 = ttk.Separator(tab1, orient='vertical')
    separator1.grid(column=3, row=0, rowspan=4, sticky='ns')
    
    bt3=Button(tab1,text='Увімк./Вимк.', image = icon3, compound = TOP, borderwidth = 0, command=None)
    bthint3 = Hovertip(bt3,'дозволяє вмикати/вимикати систему \nГТН на певний період без її \nповного відключення від контролерів')
    bt3.grid(row=0, column=4, rowspan=3, padx = 5, pady = 1)

    separator2 = ttk.Separator(tab1, orient='vertical')
    separator2.grid(column=5, row=0, rowspan=3, sticky='ns')
    
    bt4=Button(tab1,text = '{}°'.format(temp_outside), image = icon4, compound = TOP, borderwidth = 0)
    bthint4 = Hovertip(bt4,'меню індикації температури поза приміщенням \n(за наявності відповідних датчиків) \n\n(Для демонстрації функціоналу дані \nпро температуру сайту обираються \nз сайту погоди у Львові)')
    bt4.grid(row=0, column=6, rowspan=3, padx = 3, pady = 5)
    fileHandle = open ( 'hptemperature\\temp_in.txt',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    bt5=Button(tab1,text='{}°'.format(lineList[-1]), image = icon5, compound = TOP, borderwidth = 0, command=temp_inside)
    bthint5 = Hovertip(bt5,'меню індикації температури повітря у приміщеннi \n\n(клацніть ЛКМ для налаштування комфортної температури у \nприміщенні в межах від 0.00° до 35.99°)')
    bt5.grid(row=0, column=7, rowspan=3, padx = 3, pady = 5)
    fileHandle1 = open ( 'hptemperature\\temp_boiler.txt',"r" )
    lineList1 = fileHandle1.readlines()
    fileHandle1.close()
    bt6=Button(tab1,text='{}°'.format(lineList1[-1]), image = icon6, compound = TOP, borderwidth = 0, command=temp_boiler)
    bthint6 = Hovertip(bt6,'меню індикації температури бойлера \n\n(клацніть ЛКМ для налаштування температури води у \nбойлерi в межах від 0.00° до 89.99°)')
    bt6.grid(row=0, column=8, rowspan=3, padx = 3, pady = 5)
    bt7=Button(tab1,text='{}°'.format(00.00), image = icon7, compound = TOP, borderwidth = 0, command=None)
    bthint7 = Hovertip(bt7,'перегляд управління температурою системи ГТН та \nвідображення поточного стану \n\n(при підключенні контролера можна моніторити температуру ГТН))')
    bt7.grid(row=0, column=9, rowspan=3, padx = 3, pady = 5)

    separator3 = ttk.Separator(tab1, orient='vertical')
    separator3.grid(column=10, row=0, rowspan=3, sticky='ns')

    lbl2 = Label(tab1, text="Тепловий насос").grid(row=3, column=3, columnspan=10, padx = 0, pady = 1)

    bt8=Button(tab1,text='Режим', image = icon8, compound = TOP, borderwidth = 0, command=None)
    bthint8 = Hovertip(bt8, 'відображає увесь перелік режимів та їх рівні, які \nє залученими на даний момент часу \n(при підключенні контролера)')
    bt8.grid(row=0, column=11, rowspan=3, padx = 5, pady = 5)

    separator4 = ttk.Separator(tab1, orient='vertical')
    separator4.grid(column=12, row=0, rowspan=4, sticky='ns')
    

    bt9=Button(tab1,text='Графік', image = icon9, compound = LEFT, borderwidth = 0, command=page8)
    bthint9 = Hovertip(bt9, 'При виконанні перенаправляє на сторінку з відображенням \nдоступних температурних графіків')
    bt9.grid(row=0, column=13, sticky=W, padx = 5, pady = 0)
    bt10=Button(tab1,text='Параметри', image = icon10, compound = LEFT, borderwidth = 0, command=parameters_page)
    bthint10 = Hovertip(bt10, 'При виконанні перенаправляє на сторінку з відображенням загальних датчиків, \nякі розміщуються у будь-якій системі ГТН')
    bt10.grid(row=1, column=13, sticky=W, padx = 5, pady = 0)
    bt11=Button(tab1,text='Сенсори', image = icon11, compound = LEFT, borderwidth = 0, command=None)
    bthint11 = Hovertip(bt11, 'При виконанні перенаправляє на сторінку з відображенням сенсорів підключеного контролера \n(Зчитує сенсори з контролера та виводить список станів кожного зі сенсорів) \n\n(у демонстраційному зразку неактивна)')  
    bt11.grid(row=2, column=13, sticky=W, padx = 5, pady = 0)
    bt12=Button(tab1,text='Розклад', image = icon12, compound = LEFT, borderwidth = 0, command=page8)
    bthint12 = Hovertip(bt12, 'При виконанні перенаправляє на сторінку з можливістю \nналаштування режимів роботи ГТН у конкретний період')
    bt12.grid(row=0, column=14, sticky=W, padx = 5, pady = 0)
    bt13=Button(tab1,text='Режими', image = icon13, compound = LEFT, borderwidth = 0, command=page8)
    bthint13 = Hovertip(bt13, 'При виконанні перенаправляє на сторінку з можливістю \nналаштування режимів роботи ГТН у даний момент')
    bt13.grid(row=1, column=14, sticky=W, padx = 5, pady = 0)


    separator5 = ttk.Separator(tab1, orient='vertical')
    separator5.grid(column=15, row=0, rowspan=3, sticky='ns')

    bt14=Button(tab1,text='Завантажити', image = icon14, compound = TOP, borderwidth = 0, command=None)
    bthint14 = Hovertip(bt14, 'дозволяє створити бекап обраних даних за \nпевний період часу, визначений користувачем \n\n (недоступна без підключення фізичних пристроїв)')
    bt14.grid(row=0, column=16, rowspan=3, padx = 5, pady = 5)

    lbl3 = Label(tab1, text="Вигляд").grid(row=3, column=12, columnspan=6, padx = 0, pady = 1)

    separator6 = ttk.Separator(tab1, orient='vertical')
    separator6.grid(column=17, row=0, rowspan=4, sticky='ns')

    #tab2
    bt01=Button(tab2,text='Оновити', image = icon15, compound = TOP, borderwidth = 0, command=open_site)
    bthint15 = Hovertip(bt01, 'при виконанні перенаправляє на сайт розробника для перегляду нових версій ПЗ')
    bt01.grid(row=0, column=0, rowspan=4, padx = 15, pady = 5)
    
    separator0 = ttk.Separator(tab2, orient='vertical')
    separator0.grid(column=1, row=0, rowspan=4, sticky='ns')
    
    bt2=Button(tab2,text='Скинути налаштування', image = icon16, compound = TOP, borderwidth = 0, command=None)
    bt2.grid(row=0, column=2, rowspan=4, padx = 15, pady = 5)

    separator1 = ttk.Separator(tab2, orient='vertical')
    separator1.grid(column=3, row=0, rowspan=6, sticky='ns')

    #main_page
    
    nb1 = ttk.Notebook(frame)
    nb1.grid(row=1, column=0)

    # Add first tab
    heat_pump_1 = ttk.Frame(nb1)
    nb1.add(heat_pump_1, text='Тепловий насос:0000000 X', image=image2, compound=LEFT)
    
    heat_pump_1.columnconfigure(0, minsize=40)#for tab
    heat_pump_1.columnconfigure(1, minsize=120)
    heat_pump_1.columnconfigure(2, minsize=48)
    heat_pump_1.columnconfigure(3, minsize=24)
    heat_pump_1.columnconfigure(4, minsize=108)
    heat_pump_1.columnconfigure(5, minsize=12)
    heat_pump_1.columnconfigure(6, minsize=60)
    heat_pump_1.columnconfigure(7, minsize=84)
    heat_pump_1.columnconfigure(8, minsize=24)
    heat_pump_1.columnconfigure(9, minsize=48)
    heat_pump_1.columnconfigure(10, minsize=90)
    heat_pump_1.columnconfigure(11, minsize=30)
    heat_pump_1.columnconfigure(12, minsize=60)
    heat_pump_1.columnconfigure(13, minsize=130)
    heat_pump_1.columnconfigure(14, minsize=20)
    heat_pump_1.columnconfigure(15, minsize=54)
    heat_pump_1.columnconfigure(16, minsize=24)
    heat_pump_1.columnconfigure(17, minsize=60)
    heat_pump_1.columnconfigure(18, minsize=94)
    heat_pump_1.columnconfigure(19, minsize=900)
    
    
    label1 = Label(heat_pump_1, text = "Пристроїв не знайдено...", bg=active_color)
    label1.grid(row=0, column=0, columnspan = 19, sticky="w")
    hpsystembackground=Label(heat_pump_1, image = image1)
    hpsystembackground.grid(row=1, column=1, rowspan= 18, columnspan=18, padx = 5, pady = 0, sticky="w")

    pump1 = Label(heat_pump_1, text = "1").grid(row=5, column=15, sticky="w", padx = 0, pady = 10)
    pump2 = Label(heat_pump_1, text = "2").grid(row=6, column=3, sticky="sw", padx = 0, pady = 10)
    pump3 = Label(heat_pump_1, text = "3").grid(row=1, column=3, sticky="w")
    pump4 = Label(heat_pump_1, text = "4").grid(row=1, column=5, sticky="w")
    pump5 = Label(heat_pump_1, text = "5").grid(row=6, column=11, sticky="sw", padx = 0, pady = 10)
    pump6 = Label(heat_pump_1, text = "6").grid(row=1, column=11, sticky="w")
    pump7 = Label(heat_pump_1, text = "7").grid(row=7, column=14, sticky="nw", padx = 0, pady = 5.49)
    pump8 = Label(heat_pump_1, text = "8").grid(row=1, column=9, sticky="w")

##    temp3 = Label(heat_pump_1, text = "00.00°").grid(row=2, column=3, sticky="e")
##    temp4 = Label(heat_pump_1, text = "00.00°").grid(row=2, column=5, sticky="w")
##    pump6 = Label(heat_pump_1, text = "00.00°").grid(row=2, column=11, sticky="w")
##    pump7 = Label(heat_pump_1, text = "00.00°").grid(row=8, column=14, sticky="nw", padx = 0, pady = 5.49)
##    pump8 = Label(heat_pump_1, text = "00.00°").grid(row=2, column=9, sticky="w")
    p1 = Label(heat_pump_1, text = "0.00 кВт").place(relx=0.085,rely=0.8065)
    p2 = Label(heat_pump_1, text = "0.00 кВт").place(relx=0.22,rely=0.8065)
    p3 = Label(heat_pump_1, text = "0.00 кВт").place(relx=0.322,rely=0.8065)
   
def page8():
    frame=Frame(root,bg=active_color)
    frame.place(relx=0,rely=0.035,relheight=1,relwidth=1)
    nb = ttk.Notebook(frame)
    nb.grid(row=0, column=0, columnspan=8)

    # Add first tab
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)

    #tab1.grid(row=0, column=0)
    nb.add(tab1, text='Головна')
    nb.add(tab2, text='Сервіс')

    # Change the sizes of the columns equally
    tab1.columnconfigure(0, minsize=70)
    tab1.columnconfigure(1, minsize=5)
    tab1.columnconfigure(2, minsize=70)
    tab1.columnconfigure(3, minsize=5)
    tab1.columnconfigure(4, minsize=70)
    tab1.columnconfigure(5, minsize=5)
    tab1.columnconfigure(6, minsize=70)
    tab1.columnconfigure(7, minsize=70)
    tab1.columnconfigure(8, minsize=70)
    tab1.columnconfigure(9, minsize=70)
    tab1.columnconfigure(10, minsize=5)
    tab1.columnconfigure(11, minsize=70)
    tab1.columnconfigure(12, minsize=5)
    tab1.columnconfigure(13, minsize=100)
    tab1.columnconfigure(14, minsize=100)
    tab1.columnconfigure(15, minsize=5)
    tab1.columnconfigure(16, minsize=90)
    tab1.columnconfigure(17, minsize=5)
    tab1.columnconfigure(18, minsize=90)
    tab1.columnconfigure(19, minsize=5)
    tab1.columnconfigure(20, minsize=900)

    tab2.columnconfigure(0, minsize=70)
    tab2.columnconfigure(1, minsize=5)
    tab2.columnconfigure(2, minsize=70)
    tab2.columnconfigure(3, minsize=5)
    tab2.columnconfigure(4, minsize=1770)

    #tab1
    bt1=Button(tab1,text='Відключити', image = icon1, compound = TOP, borderwidth = 0, command=None)
    bthint1 = Hovertip(bt1,'дозволяє відключити ПЗ від системи ГТН, \nякщо користувач підключений \n(повернення на сторінку входу)')
    bt1.grid(row=0, column=0, rowspan=3, padx = 5, pady = 5)
    
    separator0 = ttk.Separator(tab1, orient='vertical')
    separator0.grid(column=1, row=0, rowspan=3, sticky='ns')
    
    lbl1 = Label(tab1, text="Головна").grid(row=3, column=0, columnspan=3, padx = 0, pady = 1)

    bt2=Button(tab1,text='Відкрити базу', image = icon2, compound = TOP, borderwidth = 0, command=open_file)
    bthint2 = Hovertip(bt2,'дозволяє відкрити бекапи, \nщо містяться на пристрої для \nвідображення статистики за обраний користувачем \nперіод \n\n(для відображення функціоналу спробуйте запустити файл \n\"temp_plot.txt\", який міститься у папці ПЗ).')
    bt2.grid(row=0, column=2, rowspan=3, padx = 5, pady = 5)

    separator1 = ttk.Separator(tab1, orient='vertical')
    separator1.grid(column=3, row=0, rowspan=4, sticky='ns')
    
    bt3=Button(tab1,text='Увімк./Вимк.', image = icon3, compound = TOP, borderwidth = 0, command=None)
    bthint3 = Hovertip(bt3,'дозволяє вмикати/вимикати систему \nГТН на певний період без її \nповного відключення від контролерів')
    bt3.grid(row=0, column=4, rowspan=3, padx = 5, pady = 1)

    separator2 = ttk.Separator(tab1, orient='vertical')
    separator2.grid(column=5, row=0, rowspan=3, sticky='ns')
    
    bt4=Button(tab1,text = '{}°'.format(temp_outside), image = icon4, compound = TOP, borderwidth = 0)
    bthint4 = Hovertip(bt4,'меню індикації температури поза приміщенням \n(за наявності відповідних датчиків) \n\n(Для демонстрації функціоналу дані \nпро температуру сайту обираються \nз сайту погоди у Львові)')
    bt4.grid(row=0, column=6, rowspan=3, padx = 3, pady = 5)
    fileHandle = open ( 'hptemperature\\temp_in.txt',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    bt5=Button(tab1,text='{}°'.format(lineList[-1]), image = icon5, compound = TOP, borderwidth = 0, command=temp_inside)
    bthint5 = Hovertip(bt5,'меню індикації температури повітря у приміщеннi \n\n(клацніть ЛКМ для налаштування комфортної температури у \nприміщенні в межах від 0.00° до 35.99°)')
    bt5.grid(row=0, column=7, rowspan=3, padx = 3, pady = 5)
    fileHandle1 = open ( 'hptemperature\\temp_boiler.txt',"r" )
    lineList1 = fileHandle1.readlines()
    fileHandle1.close()
    bt6=Button(tab1,text='{}°'.format(lineList1[-1]), image = icon6, compound = TOP, borderwidth = 0, command=temp_boiler)
    bthint6 = Hovertip(bt6,'меню індикації температури бойлера \n\n(клацніть ЛКМ для налаштування температури води у \nбойлерi в межах від 0.00° до 89.99°)')
    bt6.grid(row=0, column=8, rowspan=3, padx = 3, pady = 5)
    bt7=Button(tab1,text='{}°'.format(00.00), image = icon7, compound = TOP, borderwidth = 0, command=None)
    bthint7 = Hovertip(bt7,'перегляд управління температурою системи ГТН та \nвідображення поточного стану \n\n(при підключенні контролера можна моніторити температуру ГТН))')
    bt7.grid(row=0, column=9, rowspan=3, padx = 3, pady = 5)

    separator3 = ttk.Separator(tab1, orient='vertical')
    separator3.grid(column=10, row=0, rowspan=3, sticky='ns')

    lbl2 = Label(tab1, text="Тепловий насос").grid(row=3, column=3, columnspan=10, padx = 0, pady = 1)

    bt8=Button(tab1,text='Режим', image = icon8, compound = TOP, borderwidth = 0, command=None)
    bthint8 = Hovertip(bt8, 'відображає увесь перелік режимів та їх рівні, які \nє залученими на даний момент часу \n(при підключенні контролера)')
    bt8.grid(row=0, column=11, rowspan=3, padx = 5, pady = 5)

    separator4 = ttk.Separator(tab1, orient='vertical')
    separator4.grid(column=12, row=0, rowspan=4, sticky='ns')
    
    bt9=Button(tab1,text='Графік', image = icon9, compound = LEFT, borderwidth = 0, command=page8)
    bthint9 = Hovertip(bt9, 'При виконанні перенаправляє на сторінку з відображенням \nдоступних температурних графіків')
    bt9.grid(row=0, column=13, sticky=W, padx = 5, pady = 0)
    bt10=Button(tab1,text='Параметри', image = icon10, compound = LEFT, borderwidth = 0, command=parameters_page)
    bthint10 = Hovertip(bt10, 'При виконанні перенаправляє на сторінку з відображенням загальних датчиків, \nякі розміщуються у будь-якій системі ГТН')
    bt10.grid(row=1, column=13, sticky=W, padx = 5, pady = 0)
    bt11=Button(tab1,text='Сенсори', image = icon11, compound = LEFT, borderwidth = 0, command=None)
    bthint11 = Hovertip(bt11, 'При виконанні перенаправляє на сторінку з відображенням сенсорів підключеного контролера \n(Зчитує сенсори з контролера та виводить список станів кожного зі сенсорів) \n\n(у демонстраційному зразку неактивна)')  
    bt11.grid(row=2, column=13, sticky=W, padx = 5, pady = 0)
    bt12=Button(tab1,text='Розклад', image = icon12, compound = LEFT, borderwidth = 0, command=page8)
    bthint12 = Hovertip(bt12, 'При виконанні перенаправляє на сторінку з можливістю \nналаштування режимів роботи ГТН у конкретний період')
    bt12.grid(row=0, column=14, sticky=W, padx = 5, pady = 0)
    bt13=Button(tab1,text='Режими', image = icon13, compound = LEFT, borderwidth = 0, command=page8)
    bthint13 = Hovertip(bt13, 'При виконанні перенаправляє на сторінку з можливістю \nналаштування режимів роботи ГТН у даний момент')
    bt13.grid(row=1, column=14, sticky=W, padx = 5, pady = 0)

    separator5 = ttk.Separator(tab1, orient='vertical')
    separator5.grid(column=15, row=0, rowspan=3, sticky='ns')

    bt14=Button(tab1,text='Завантажити', image = icon14, compound = TOP, borderwidth = 0, command=None)
    bthint14 = Hovertip(bt14, 'дозволяє створити бекап обраних даних за \nпевний період часу, визначений користувачем \n\n (недоступна без підключення фізичних пристроїв)')
    bt14.grid(row=0, column=16, rowspan=3, padx = 5, pady = 5)

    lbl3 = Label(tab1, text="Вигляд").grid(row=3, column=12, columnspan=6, padx = 0, pady = 1)
    
    separator6 = ttk.Separator(tab1, orient='vertical')
    separator6.grid(column=17, row=0, rowspan=4, sticky='ns')

    bt15=Button(tab1,text='Повернутись', image = icon17, compound = TOP, borderwidth = 0, command = main_page)
    bt15.grid(row=0, column=18, rowspan=3, padx = 5, pady = 5)

    separator7 = ttk.Separator(tab1, orient='vertical')
    separator7.grid(column=19, row=0, rowspan=4, sticky='ns')
    
    #tab2
    bt01=Button(tab2,text='Оновити', image = icon15, compound = TOP, borderwidth = 0, command=open_site)
    bthint15 = Hovertip(bt01, 'при виконанні перенаправляє на сайт розробника для перегляду нових версій ПЗ')
    bt01.grid(row=0, column=0, rowspan=4, padx = 15, pady = 5)
    
    separator0 = ttk.Separator(tab2, orient='vertical')
    separator0.grid(column=1, row=0, rowspan=4, sticky='ns')
    
    bt2=Button(tab2,text='Скинути налаштування', image = icon16, compound = TOP, borderwidth = 0, command=None)
    bt2.grid(row=0, column=2, rowspan=4, padx = 15, pady = 5)

    separator1 = ttk.Separator(tab2, orient='vertical')
    separator1.grid(column=3, row=0, rowspan=6, sticky='ns')

    #frame
    heading = ["№", "Назва", "Температура", "Нагрів", "Альт.Нагрів", "Бойлер", "Альт.Бойлер", "Охолодження"]
    modes = ["Черговий режим", "Еко-режим", "Стандартний режим", "Режим 3", "Режим 4", "Режим 5", "Режим 6"]
    for row in range(1,9):
        for col in range(8):
            if row == 1:
                label = Label(frame, text = heading[col], bg=main_color, padx=3, pady = 3)    
                label.grid(row = row, column = col, sticky="nsew")
            else:
                if col == 0:
                    label = Label(frame, text = row-1, bg=active_color, padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="nsew")
                elif col == 1:
                    label = Label(frame, text = modes[row-2], bg=active_color, padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="w")
                elif col == 2:
                    spin = Spinbox(frame, from_=1, to=3, width=5) #режими 1-3   
                    spin.grid(row = row, column = col)
                else:
                    chkValue = BooleanVar() 
                    chkValue.set(False)
                    check = Checkbutton(frame, variable = chkValue, onvalue = True, offvalue = False)
                    chkValue.set(True)
                    check.grid(row=row, column = col)
                    
##                    chk.state(['selected'])  # check the checkbox
##                    chk.state(['!selected']) # clear the checkbox
##                    chk.state(['disabled'])  # disable the checkbox
##                    chk.state(['!disabled','selected']) # enable the checkbox and put a check in it!
                if col == 1:
                    frame.grid_columnconfigure(col, weight=14)
                else:
                    frame.grid_columnconfigure(col, weight=1)

    # the figure that will contain the plot
    fig = Figure(figsize = (16, 5.5), dpi = 100)
    fig.patch.set_facecolor(active_color)
    with open('hptemperature\\selected.txt', "r") as input_backup:
        dataset = input_backup.read()
    y = loadtxt( dataset,dtype=object )

    y0 = [float(y[0][i]) for i in range(len(y[0]))]
    y1 = [float(y[1][i]) for i in range(len(y[1]))]
    y2 = [float(y[2][i]) for i in range(len(y[2]))]
    # adding the subplot
    plot1 = fig.add_subplot(211)# nrows, ncols, index

    # plotting the graph
    plot1.plot(y0, color='blue')
    plot1.plot(y1, color='magenta')
    plot1.plot(y2, color='yellow')
    plot1.legend(['температура у приміщенні', 'темература ззовні', 'температура бойлера'], fontsize=6, facecolor=active_color)
    plot1.set_facecolor(active_color)
    plot1.set_xlim([int(y[3][0]), int(y[3][-2])])
    plot1.set_ylim([0, 110])
    plot1.set_ylabel('Температура t°')
    plot1.set_xlabel('Графік зміни температури з {0}-{1}-{2} по {3}-{4}-{5}\n    '.format(str(y[3][0]), str(y[4][0]), str(y[5][0]), str(y[3][-1]), str(y[4][0]), str(y[5][0])))
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = frame)  
    canvas.draw()
    canvas.get_tk_widget().configure(bg=active_color)
  
    # placing the canvas on the Tkinter window
    #canvas.get_tk_widget().grid(row = 10, column = 0, columnspan = 8)
  
    # creating the Matplotlib toolbar
    #toolbar = NavigationToolbar2Tk(canvas, frame)
    #toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row = 9, column = 0, columnspan = 8, rowspan=2)

    todayday = date.today().strftime('%d')
    todaymonth = date.today().strftime('%m')
    todayyear = date.today().strftime('%Y')
    cal = Calendar(frame, selectmode = 'day',  year = int(todayyear), month = int(todaymonth), day = int(todayday))
    cal.grid(row = 2, column = 1, rowspan=7, padx = 50, sticky="e")
    #cal.place(relx = 0.2, rely = 0.19, relheight=0.25)
    def take_date(): 
        #date.config(text = "Дата вибору: " + cal.get_date())
        data = cal.get_date()

def parameters_page():
    frame=Frame(root,bg=active_color)
    frame.place(relx=0,rely=0.035,relheight=1,relwidth=1)
    nb = ttk.Notebook(frame)
    nb.grid(row=0, column=0, columnspan=8)

    # Add first tab
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)

    #tab1.grid(row=0, column=0)
    nb.add(tab1, text='Головна')
    nb.add(tab2, text='Сервіс')

    # Change the sizes of the columns equally
    tab1.columnconfigure(0, minsize=70)
    tab1.columnconfigure(1, minsize=5)
    tab1.columnconfigure(2, minsize=70)
    tab1.columnconfigure(3, minsize=5)
    tab1.columnconfigure(4, minsize=70)
    tab1.columnconfigure(5, minsize=5)
    tab1.columnconfigure(6, minsize=70)
    tab1.columnconfigure(7, minsize=70)
    tab1.columnconfigure(8, minsize=70)
    tab1.columnconfigure(9, minsize=70)
    tab1.columnconfigure(10, minsize=5)
    tab1.columnconfigure(11, minsize=70)
    tab1.columnconfigure(12, minsize=5)
    tab1.columnconfigure(13, minsize=100)
    tab1.columnconfigure(14, minsize=100)
    tab1.columnconfigure(15, minsize=5)
    tab1.columnconfigure(16, minsize=90)
    tab1.columnconfigure(17, minsize=5)
    tab1.columnconfigure(18, minsize=90)
    tab1.columnconfigure(19, minsize=5)
    tab1.columnconfigure(20, minsize=900)

    tab2.columnconfigure(0, minsize=70)
    tab2.columnconfigure(1, minsize=5)
    tab2.columnconfigure(2, minsize=70)
    tab2.columnconfigure(3, minsize=5)
    tab2.columnconfigure(4, minsize=1770)

    #tab1
    bt1=Button(tab1,text='Відключити', image = icon1, compound = TOP, borderwidth = 0, command=None)
    bthint1 = Hovertip(bt1,'дозволяє відключити ПЗ від системи ГТН, \nякщо користувач підключений \n(повернення на сторінку входу)')
    bt1.grid(row=0, column=0, rowspan=3, padx = 5, pady = 5)
    
    separator0 = ttk.Separator(tab1, orient='vertical')
    separator0.grid(column=1, row=0, rowspan=3, sticky='ns')
    
    lbl1 = Label(tab1, text="Головна").grid(row=3, column=0, columnspan=3, padx = 0, pady = 1)

    bt2=Button(tab1,text='Відкрити базу', image = icon2, compound = TOP, borderwidth = 0, command=open_file)
    bthint2 = Hovertip(bt2,'дозволяє відкрити бекапи, \nщо містяться на пристрої для \nвідображення статистики за обраний користувачем \nперіод \n\n(для відображення функціоналу спробуйте запустити файл \n\"temp_plot.txt\", який міститься у папці ПЗ).')
    bt2.grid(row=0, column=2, rowspan=3, padx = 5, pady = 5)

    separator1 = ttk.Separator(tab1, orient='vertical')
    separator1.grid(column=3, row=0, rowspan=4, sticky='ns')
    
    bt3=Button(tab1,text='Увімк./Вимк.', image = icon3, compound = TOP, borderwidth = 0, command=None)
    bthint3 = Hovertip(bt3,'дозволяє вмикати/вимикати систему \nГТН на певний період без її \nповного відключення від контролерів')
    bt3.grid(row=0, column=4, rowspan=3, padx = 5, pady = 1)

    separator2 = ttk.Separator(tab1, orient='vertical')
    separator2.grid(column=5, row=0, rowspan=3, sticky='ns')
    
    bt4=Button(tab1,text = '{}°'.format(temp_outside), image = icon4, compound = TOP, borderwidth = 0)
    bthint4 = Hovertip(bt4,'меню індикації температури поза приміщенням \n(за наявності відповідних датчиків) \n\n(Для демонстрації функціоналу дані \nпро температуру сайту обираються \nз сайту погоди у Львові)')
    bt4.grid(row=0, column=6, rowspan=3, padx = 3, pady = 5)
    fileHandle = open ( 'hptemperature\\temp_in.txt',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    bt5=Button(tab1,text='{}°'.format(lineList[-1]), image = icon5, compound = TOP, borderwidth = 0, command=temp_inside)
    bthint5 = Hovertip(bt5,'меню індикації температури повітря у приміщеннi \n\n(клацніть ЛКМ для налаштування комфортної температури у \nприміщенні в межах від 0.00° до 35.99°)')
    bt5.grid(row=0, column=7, rowspan=3, padx = 3, pady = 5)
    fileHandle1 = open ( 'hptemperature\\temp_boiler.txt',"r" )
    lineList1 = fileHandle1.readlines()
    fileHandle1.close()
    bt6=Button(tab1,text='{}°'.format(lineList1[-1]), image = icon6, compound = TOP, borderwidth = 0, command=temp_boiler)
    bthint6 = Hovertip(bt6,'меню індикації температури бойлера \n\n(клацніть ЛКМ для налаштування температури води у \nбойлерi в межах від 0.00° до 89.99°)')
    bt6.grid(row=0, column=8, rowspan=3, padx = 3, pady = 5)
    bt7=Button(tab1,text='{}°'.format(00.00), image = icon7, compound = TOP, borderwidth = 0, command=None)
    bthint7 = Hovertip(bt7,'перегляд управління температурою системи ГТН та \nвідображення поточного стану \n\n(при підключенні контролера можна моніторити температуру ГТН))')
    bt7.grid(row=0, column=9, rowspan=3, padx = 3, pady = 5)

    separator3 = ttk.Separator(tab1, orient='vertical')
    separator3.grid(column=10, row=0, rowspan=3, sticky='ns')

    lbl2 = Label(tab1, text="Тепловий насос").grid(row=3, column=3, columnspan=10, padx = 0, pady = 1)

    bt8=Button(tab1,text='Режим', image = icon8, compound = TOP, borderwidth = 0, command=None)
    bthint8 = Hovertip(bt8, 'відображає увесь перелік режимів та їх рівні, які \nє залученими на даний момент часу \n(при підключенні контролера)')
    bt8.grid(row=0, column=11, rowspan=3, padx = 5, pady = 5)

    separator4 = ttk.Separator(tab1, orient='vertical')
    separator4.grid(column=12, row=0, rowspan=4, sticky='ns')
    
    bt9=Button(tab1,text='Графік', image = icon9, compound = LEFT, borderwidth = 0, command=page8)
    bthint9 = Hovertip(bt9, 'При виконанні перенаправляє на сторінку з відображенням \nдоступних температурних графіків')
    bt9.grid(row=0, column=13, sticky=W, padx = 5, pady = 0)
    bt10=Button(tab1,text='Параметри', image = icon10, compound = LEFT, borderwidth = 0, command=parameters_page)
    bthint10 = Hovertip(bt10, 'При виконанні перенаправляє на сторінку з відображенням загальних датчиків, \nякі розміщуються у будь-якій системі ГТН')
    bt10.grid(row=1, column=13, sticky=W, padx = 5, pady = 0)
    bt11=Button(tab1,text='Сенсори', image = icon11, compound = LEFT, borderwidth = 0, command=None)
    bthint11 = Hovertip(bt11, 'При виконанні перенаправляє на сторінку з відображенням сенсорів підключеного контролера \n(Зчитує сенсори з контролера та виводить список станів кожного зі сенсорів) \n\n(у демонстраційному зразку неактивна)')  
    bt11.grid(row=2, column=13, sticky=W, padx = 5, pady = 0)
    bt12=Button(tab1,text='Розклад', image = icon12, compound = LEFT, borderwidth = 0, command=page8)
    bthint12 = Hovertip(bt12, 'При виконанні перенаправляє на сторінку з можливістю \nналаштування режимів роботи ГТН у конкретний період')
    bt12.grid(row=0, column=14, sticky=W, padx = 5, pady = 0)
    bt13=Button(tab1,text='Режими', image = icon13, compound = LEFT, borderwidth = 0, command=page8)
    bthint13 = Hovertip(bt13, 'При виконанні перенаправляє на сторінку з можливістю \nналаштування режимів роботи ГТН у даний момент')
    bt13.grid(row=1, column=14, sticky=W, padx = 5, pady = 0)

    separator5 = ttk.Separator(tab1, orient='vertical')
    separator5.grid(column=15, row=0, rowspan=3, sticky='ns')

    bt14=Button(tab1,text='Завантажити', image = icon14, compound = TOP, borderwidth = 0, command=None)
    bthint14 = Hovertip(bt14, 'дозволяє створити бекап обраних даних за \nпевний період часу, визначений користувачем \n\n (недоступна без підключення фізичних пристроїв)')
    bt14.grid(row=0, column=16, rowspan=3, padx = 5, pady = 5)

    lbl3 = Label(tab1, text="Вигляд").grid(row=3, column=12, columnspan=6, padx = 0, pady = 1)
    
    separator6 = ttk.Separator(tab1, orient='vertical')
    separator6.grid(column=17, row=0, rowspan=4, sticky='ns')

    bt15=Button(tab1,text='Повернутись', image = icon17, compound = TOP, borderwidth = 0, command = main_page)
    bt15.grid(row=0, column=18, rowspan=3, padx = 5, pady = 5)

    separator7 = ttk.Separator(tab1, orient='vertical')
    separator7.grid(column=19, row=0, rowspan=4, sticky='ns')
    
    #tab2
    bt01=Button(tab2,text='Оновити', image = icon15, compound = TOP, borderwidth = 0, command=open_site)
    bthint15 = Hovertip(bt01, 'при виконанні перенаправляє на сайт розробника для перегляду нових версій ПЗ')
    bt01.grid(row=0, column=0, rowspan=4, padx = 15, pady = 5)
    
    separator0 = ttk.Separator(tab2, orient='vertical')
    separator0.grid(column=1, row=0, rowspan=4, sticky='ns')
    
    bt2=Button(tab2,text='Скинути налаштування', image = icon16, compound = TOP, borderwidth = 0, command=None)
    bt2.grid(row=0, column=2, rowspan=4, padx = 15, pady = 5)

    separator1 = ttk.Separator(tab2, orient='vertical')
    separator1.grid(column=3, row=0, rowspan=6, sticky='ns')

    #frame
    heading = ["№", "Датчик", "Значення"]
    params = ["(T0) T0: t° вулиці", "(T1) T1: t° помешени", "(T2) T2: t° на выходе в гео-контур", "(T3) T3: t° на входе из гео-контура",
              "(T4) T4: t° на выходе испарител", "(T5) T5: t° на выходе из системы отопления", "(T6) T6: t° на входе в систему отопления",
              "(T7) T7: t° бойлера", "(T8) T8: t° нагріву", "(T12) TE: t° кипіння", "(T16) SH: t° перегріву", "(P0) PL: Тиск випаровування",
              "(P1) PH: Тиск конденсації", "(P16) Пресостат низького тиску", "(P17) Пресостат високого тиску", "(F0) Протік в гео-контурі",
              "(F1) Протік в системі опалення", "(F2) Лічильник електроенергії (миттєвий)", "(O1) Потужність компресора",
              "(O2) Потужність гео-контурного насоса", "(O3) Потужність контурного насоса",  "(O5) DC.RPM", "(O16) Потужність гео-контура",
              "(O17) Потужність системи опалення", "(O18) Коефіцієнт перетворення", "(X5) Мотогодинник", "(X6) Годинник бойлера",
              "(X7) Теплолічильник гарячого контура", "(X8) Електролічильник (накопичувальний)", "(R2) Параметр 2", "(R49) П49.Перегрів",
              "Компресор HI", "Компресор ON", "Помпа гео HI", "Помпа гео ON", "Помпа опалення HI", "Помпа опалення ON", "Додатковий Нагрів",
              "---", "Бойлер", " Клапан EVI", "Реверс", "Додатковий нагрівач бойлера", "---"]
    modes = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0"]
    for row in range(1,24):
        for col in range(3):
            if row == 1:
                label = Label(frame, text = heading[col], bg=background_color, padx=3, pady = 3)    
                label.grid(row = row, column = col, sticky="nsew")
            else:
                if col == 0:
                    label = Label(frame, text = row-1, bg=main_color, padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="nsew")
                elif col == 1:
                    label = Label(frame, text = params[row-2], bg=active_color, padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="w")
                elif col == 2:
                    label = Label(frame, text = modes[row-2], bg="white", padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="nsew")

                if col == 1:
                    frame.grid_columnconfigure(col, weight=2)
                else:
                    frame.grid_columnconfigure(col, weight=1)
    for row in range(1,24):
        for col in range(3, 6):
            if row == 1:
                label = Label(frame, text = heading[col-3], bg=background_color, padx=3, pady = 3)    
                label.grid(row = row, column = col, sticky="nsew")
            else:
                if col == 3:
                    label = Label(frame, text = row+21, bg=main_color, padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="nsew")
                elif col == 4:
                    label = Label(frame, text = params[row+20], bg=active_color, padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="w")
                elif col == 5:
                    label = Label(frame, text = modes[row+20], bg="white", padx=3, pady = 3)    
                    label.grid(row = row, column = col, sticky="nsew")

                if col == 1:
                    frame.grid_columnconfigure(col, weight=3)
                else:
                    frame.grid_columnconfigure(col, weight=1)
    #scrollbar = Scrollbar(frame, orient="vertical", command=frame.yview).grid(row = 1, column = 3, rowspan=44,  sticky="nse")

            
