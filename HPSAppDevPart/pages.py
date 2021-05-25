## підключення сторінок
from window import *
from page2_main_menu_page import *
from login_page_commands import *
from login_Internet_finding_controllers import *

def login_page():
    frame=Frame(root,bg=background_color)
    frame.place(relx=0,rely=0.035,relheight=1,relwidth=1)
    recommendation = Label(frame, text="           Перед початком роботи з ПЗ пропонуємо переглянути Довідку!            ",bg=background_color).place(relx=0.302,rely=0.1)
    style=ttk.Style()
    style.configure("TNotebook", activeBackground="#ffffff")
    nb = ttk.Notebook(frame, style="TNotebook")
    nb.place(relx=0.3,rely=0.15,relheight=0.4, relwidth=0.4)#grid(row=0, column=0, columnspan=3)

    # Add first tab
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)
    tab3 = ttk.Frame(nb)
    #tab1.grid(row=0, column=0)
    nb.add(tab1, text='Інтернет')
    nb.add(tab2, text='Локальна мережа')
    nb.add(tab3, text='Налаштувати...')
    # Change the sizes of the columns equally
    tab1.columnconfigure(0, minsize=43.2)#0.1
    tab1.columnconfigure(1, minsize=82.08)#0.38
    tab1.columnconfigure(2, minsize=17.28)#0.04
    tab1.columnconfigure(3, minsize=82.08)#0.19
    tab1.columnconfigure(4, minsize=164.16)
    tab1.columnconfigure(5, minsize=43.2)#0.1
    tab1.rowconfigure(0, minsize=36)#0.1 = 20.844
    tab1.rowconfigure(1, minsize=42)#0.2
    tab1.rowconfigure(2, minsize=6)
    tab1.rowconfigure(3, minsize=42)
    tab1.rowconfigure(4, minsize=6)
    tab1.rowconfigure(5, minsize=42)
    tab1.rowconfigure(6, minsize=36)
    tab1.rowconfigure(7, minsize=36)
    
    lbl0 = Label(tab1, text=" ").grid(row=0, column=0, padx = 0, pady = 0, sticky='W')
    lbl1 = Label(tab1, text="Пристрій#:").grid(row=1, column=3, padx = 0, pady = 0, sticky='W')
    lbl2 = Label(tab1, text="Логін:").grid(row=3, column=1, padx = 0, pady = 0, sticky='E')
    lbl3 = Label(tab1, text="Пароль:").grid(row=5, column=1, padx = 0, pady = 0, sticky='E')
    deviceInternetTab = Spinbox(tab1, from_=0, to=10000000000, width=10)
    deviceInternetTab.grid(row=1, column=3, columnspan=2, padx = 80, pady = 0, sticky='W')
    loginInternetTab = Text(tab1, height=1, width=23, wrap = "word")
    loginInternetTab.grid(row=3, column=3, padx = 0, pady = 0, sticky='W')
    password = StringVar() #Password variable
    passwordInternetTab = Entry(tab1, textvariable=password, show='*', width=31)
    passwordInternetTab.grid(row=5, column=3, columnspan=2, padx = 0, pady = 0, sticky='W')
    ip = '-'
    device = deviceInternetTab.get()
    log = loginInternetTab.get("1.0",END)
    pas = password.get()
    def OKInternetTab():
        with open('hptemperature\\user_information.txt', 'w') as result_file:
            result_file.write(f'{str(ip)}')# IP-адреса:
            result_file.write(f'\n{str(device)}')# Пристрій
            result_file.write(f'\n{str(log)}')# Логін
            result_file.write(f'\n{str(pas)}')# Пароль
        main_page()
    btnOKInternetTab = Button(tab1, height=1, width=1, text="Підключити", command= OKInternetTab).grid(row=7, column=2, columnspan=2, padx = 0, pady = 0, sticky='nsew')

    tab2.columnconfigure(0, minsize=43.2)#0.1
    tab2.columnconfigure(1, minsize=82.08)#0.38
    tab2.columnconfigure(2, minsize=17.28)#0.04
    tab2.columnconfigure(3, minsize=82.08)#0.19
    tab2.columnconfigure(4, minsize=164.16)
    tab2.columnconfigure(5, minsize=43.2)#0.1
    tab2.rowconfigure(0, minsize=36)#0.1 = 20.844
    tab2.rowconfigure(1, minsize=42)#0.2
    tab2.rowconfigure(2, minsize=6)
    tab2.rowconfigure(3, minsize=42)
    tab2.rowconfigure(4, minsize=6)
    tab2.rowconfigure(5, minsize=42)
    tab2.rowconfigure(6, minsize=36)
    tab2.rowconfigure(7, minsize=36)
    
    lbl00 = Label(tab2, text=" ").grid(row=0, column=0, padx = 0, pady = 0, sticky='W')
    lbl10 = Label(tab2, text="IP-адреса:").grid(row=1, column=1, padx = 0, pady = 0, sticky='E')
    lbl20 = Label(tab2, text="Підключені пристрої:").grid(row=3, column=1, padx = 0, pady = 0, sticky='E')
    deviceLocalTab = Text(tab2, height=1, width=17, wrap = "word")
    deviceLocalTab.grid(row=1, column=3, padx = 0, pady = 0, sticky='W')
    comboLocal = Combobox(tab2)  
    comboLocal['values'] = ('None')  
    comboLocal.grid(row=3, column=3, padx = 0, pady = 0, sticky='W')
    ip1 = deviceLocalTab.get("1.0",END)
    device1 = '-'
    log1 = '-'
    pas1 = '-'
    def OKLocalTab():
        with open('hptemperature\\user_information.txt', 'w') as result_file:
            result_file.write(f'{str(ip1)}')# IP-адреса:
            result_file.write(f'\n{str(device1)}')# Пристрій
            result_file.write(f'\n{str(log1)}')# Логін
            result_file.write(f'\n{str(pas1)}')# Пароль
        main_page()
    btnOKLocalTab = Button(tab2, height=1, width=1, text="Підключити", command=OKLocalTab).grid(row=7, column=2, columnspan=2, padx = 0, pady = 0, sticky='nsew')

    tab3.columnconfigure(0, minsize=43.2)#0.1
    tab3.columnconfigure(1, minsize=82.08)#0.38
    tab3.columnconfigure(2, minsize=17.28)#0.04
    tab3.columnconfigure(3, minsize=82.08)#0.19
    tab3.columnconfigure(4, minsize=164.16)
    tab3.columnconfigure(5, minsize=43.2)#0.1
    tab3.rowconfigure(0, minsize=36)#0.1 = 20.844
    tab3.rowconfigure(1, minsize=42)#0.2
    tab3.rowconfigure(2, minsize=6)
    tab3.rowconfigure(3, minsize=42)
    tab3.rowconfigure(4, minsize=6)
    tab3.rowconfigure(5, minsize=42)
    tab3.rowconfigure(6, minsize=36)
    tab3.rowconfigure(7, minsize=36)
    
    lbl01 = Label(tab3, text=" ").grid(row=0, column=0, padx = 0, pady = 0, sticky='W')
    lbl11 = Label(tab3, text="IP-адреса:").grid(row=1, column=1, padx = 0, pady = 0, sticky='E')
    lbl21 = Label(tab3, text="Логін:").grid(row=3, column=1, padx = 0, pady = 0, sticky='E')
    lbl31 = Label(tab3, text="Пароль:").grid(row=5, column=1, padx = 0, pady = 0, sticky='E')
    deviceCustomTab = Text(tab3, height=1, width=23, wrap = "word")
    deviceCustomTab.grid(row=1, column=3, padx = 0, pady = 0, sticky='W')
    loginCustomTab = Text(tab3, height=1, width=23, wrap = "word")
    loginCustomTab.grid(row=3, column=3, padx = 0, pady = 0, sticky='W')
    passwordCustom = StringVar() #Password variable
    passwordCustomTab = Entry(tab3, textvariable=password, show='*', width=31)
    passwordCustomTab.grid(row=5, column=3, columnspan=2, padx = 0, pady = 0, sticky='W')
    ip2 = deviceCustomTab.get("1.0",END)
    device2 = '-'
    log2 = loginCustomTab.get("1.0",END)
    pas2 = passwordCustom.get()
    def OKCustomTab():
        with open('hptemperature\\user_information.txt', 'w') as result_file:
            result_file.write(f'{str(ip2)}')# IP-адреса:
            result_file.write(f'\n{str(device2)}')# Пристрій
            result_file.write(f'\n{str(log2)}')# Логін
            result_file.write(f'\n{str(pas2)}')# Пароль
        main_page()
    btnOKCustomTab = Button(tab3, height=1, width=1, text="Підключити", command=OKCustomTab).grid(row=7, column=2, columnspan=2, padx = 0, pady = 0, sticky='nsew')


    
def information():
    longread = """Вас вітає ПЗ для користувацького контролю системи геотермальних теплових насосів HPSApp. 
Дякуємо, що скористалися ПЗ з метою ознайомлення з інтерфейсом програми за відсутності фізичних пристроїв.

З метою полегшення використання тестового ПЗ, пропонуємо Вам детальніше ознайомитись з можливими функціями для перегляду та використання:

1. Вхід у систему вимкнений з метою продемонструвати можливі варіанти входу та перейти до головної сторінки, натиснувши кнопку "Підключити".

2. Іконка користувача відображатиме введені клієнтом дані з метою перевірки таких даних, як IP-адреса чи ID контролера, логін та пароль.

3. Перейшовши на головну сторінку, Вам буде відображено меню та перелік підключених систем у вигляді внутрішніх вікон (для демонстрації 
    підключено лише одну систему та її назву з іконкою, що позначає відсутність підключених фізичних систем). У цьому вікні моделюються 
    робота системи ГТН, в якій відображено температурні режими у окремих ділянках системи, а також показано прапорці, які відповідають за 
    ті, чи інші компоненти системи. 
    До прикладу, значення прапорців:
	1 - Тепловий насос на обігрів приміщення
	2 - Альтернативний нагрівач
	4 – Тепловий насос на нагрів бойлера
	8 – Електронагрів бойлера
	16 – Режим охолодження (якщо такий є у системі)
    І тут ТН + нагрівач = 1 + 2 = 3 і т. д.

4. Меню складається з двох основних вкладок: «Головна» та «Сервіс».
  У вкладці «Головна» Вам пропонується до уваги три блоки основних команд, якими Ви може оперувати, а саме:
    1. Блок «Головна» містить дві функції:
	a. «Відключити» - (НАВЕДІТЬ МИШКОЮ НА ФУНКЦІЮ ТА ОТРИМАЄТЕ ІНФОРМАЦІЮ ПРО ФУНКЦІЮ)
	b. «Відкрити базу» - (НАВЕДІТЬ МИШКОЮ НА ФУНКЦІЮ ТА ОТРИМАЄТЕ ІНФОРМАЦІЮ ПРО ФУНКЦІЮ)
    2. Блок «Тепловий насос» містить наступний функціонал:
	a. «Увімк./Вимк.» - (НАВЕДІТЬ МИШКОЮ НА ФУНКЦІЮ ТА ОТРИМАЄТЕ ІНФОРМАЦІЮ ПРО ФУНКЦІЮ)
	b. Температурний блок містить:
		i. Меню індикації температури поза приміщенням (НАВЕДІТЬ МИШКОЮ НА ФУНКЦІЮ ТА ОТРИМАЄТЕ ІНФОРМАЦІЮ ПРО ФУНКЦІЮ);
		ii. Меню індикації температури повітря у приміщенні (КЛАЦНІТЬ ЛКМ ДЛЯ НАЛАШТУВАННЯ ТЕМПЕРАТУРИ З ТОЧНІСТЮ ДО СОТИХ, НАВЕДІТЬ ДЛЯ ПІДКАЗКИ);
		iii. Меню індикації температури бойлера (КЛАЦНІТЬ ЛКМ ДЛЯ НАЛАШТУВАННЯ ТЕМПЕРАТУРИ З ТОЧНІСТЮ ДО СОТИХ, НАВЕДІТЬ ДЛЯ ПІДКАЗКИ);
		iv. Управлінню температурою системи ГТН та відображення поточного стану;
	c. «Режим» - функція, яка відображає увесь перелік режимів та їх рівні, які є залученими на даний момент часу.
    3. Блок «Вигляд» дозволяє:
	a. Налаштувати параметри системи ГТН, перевірити роботу сенсорів,
	   встановити графік роботи системи протягом наступного тижня та
	   налаштувати режими роботи у відповідних пунктах;
	b. Переглянути графіки зміни температурних режимів за обраний період часу у відповідному пункті;
	c. «Завантажити» - функція, що дозволяє створити бекап обраних даних за певний період часу, визначений користувачем.
  Вкладка «Сервіс» містить лише дві функції:
    1. «Оновити» - дозволяє завантажити та запустити нову версію ПЗ без повторного входу в систему (КЛАЦНІТЬ ЛКМ ДЛЯ ПЕРЕХОДУ ДО РЕПОЗИТОРІЮ З НОВОЮ ВЕРСІЄЮ);
    2. «Скинути налаштування» - повернути налаштування контролерів до встановлених за замовчуванням."""
    frame=Frame(root,bg=active_color)
    frame.place(relx=0,rely=0.035,relheight=1,relwidth=1)
    frame.columnconfigure(0, minsize=40)
    frame.columnconfigure(1, minsize=45)
    frame.columnconfigure(2, minsize=330)
    frame.columnconfigure(3, minsize=45)
    frame.columnconfigure(4, minsize=330)

    label=Label(frame,text=longread, justify=LEFT)
    label.grid(row=0, column=0, columnspan=5, padx = 10, pady = 0, sticky="w")
    btntomain = Button(frame, height=1, width=1, text="На головну сторінку", command= main_page).grid(row=1, column=1, columnspan=2, padx = 40, pady = 5, sticky='nsew')
    btntolog = Button(frame, height=1, width=1, text="До сторінки авторизації", command=login_page).grid(row=1, column=3, columnspan=2, padx = 40, pady = 5, sticky='nsew')
