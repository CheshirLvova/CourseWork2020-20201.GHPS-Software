## підключення внутрішніх бібліотек
from libs import *

## - визначити джерела постачання даних для виконання задач проєкта; зафіксувати адреси
## серверів чи інші, звідки отримувати дані;
def GetServerAddress(apiKey):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Lviv&appid=$$apiKey$$'
    return url.replace('$$apiKey$$', apiKey)

def GetDataFromServer():
    ##  1) перевірити, чи є дані за сьогоднішній день  
    # print('Checking if file with data for this day already exist')

    dirPath = 'hptemperature\\'#hptemperature\\
    files = glob.glob(os.path.join(dirPath, '*.json'))

    today = date.today().strftime('%d-%m-%Y')
    filename = dirPath + f'{today}.json'
    ## 2) якщо даних немає – отримати від сервера   
    if filename in files:
        # print('File with data for this day already exist')
        return

    ## print('Connecting to server...')

    remoteaddr = GetServerAddress('1952efb4a7da640d955fd67682858a7f')
    remotefile = urllib.request.urlopen(remoteaddr)  
    ## 3) прийняти рішення на випадок відсутності даних
    # print('Get file')

    with open(filename, 'wb') as fsave:     
        fsave.write(remotefile.read())  
        # print('File was saved')

    remotefile.close()
    # print('Remote file closed')

    # print('\nPrint file to python window: ')
    with open(filename) as data_file:
        data = json.load(data_file)
    pprint(data)

    #print('\nPrinting finished')


## Завдання 1. Аналіз структури файлу json і показ прикладу даних
def GatherAllData(result_file):
    """ Read all data from result_file and analyze json structure """
    #result_file.write('Function to gather data from all .json files started')

    dirPath = 'hptemperature\\'#hptemperature\\
    files = glob.glob(os.path.join(dirPath, '*.json'))
    #result_file.write('\nAll data files have same structure:')
    with open(files[0]) as data_file:
        one_file_data = json.load(data_file)
        #result_file.write('\nMain info:')
        #result_file.write(f'\nType of entire document: {type(one_file_data).__name__}')
        #result_file.write(f'\nDocument has: {len(one_file_data)} elements')
        #result_file.write(f'\nType of every element: {[type(one_file_data[elem]).__name__ for elem in one_file_data.keys()]}:')
        #result_file.write(f"\nType of 'main' element: {type(one_file_data['main']).__name__}")
        #result_file.write(f"\nValue of 'main':\n{one_file_data['main']}")
        #result_file.write("\nSubelements of 'main':\n")
        #result_file.write('\n'.join([ str(subvalue) for subvalue in one_file_data['main'].items() ]))
        
    data = []

    for file in files:
        with open(file) as data_file:
            filename = os.path.split(file)[1]
            temp = json.load(data_file)
            data.append({os.path.splitext(filename)[0] : temp})     

    #result_file.write('\n\nAll data gathered')
    #result_file.write('\nFirst data entry printed for example:\n')   
    #json.dump(data[0], result_file, indent=4)
    
    return data

## Завдання 2. Виведення значень за певним ключем
def GetValuesByKey(data, key):
    """ Get values from data by specific key """
    values = []
    
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                values.append({"value":record[key1][k], "date":key1})

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        values.append({"value": elem[key], "date":key1})

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    values.append({"value":record[key1][k][key], "date":key1})

    return values
## Завдання 2.  Виведення значення за певним ключем             
def GetValueByKey(result_file, data, key):
    """ Write to result_file values from data by specific key """
    #result_file.write(f'\n\nPrint value by key: {key}:')
    a = 'Print value by key:'
    a += key
    values = GetValuesByKey(data, key)
    for value in values:
        if('value'== 'temp' or 'value'=='feels_like' or 'value'== 'temp_min' or 'value'== 'temp_max'):
            value['value'] += - 273.15
        #result_file.write(f'\nValue of key: {key} is {value["value"]} on {value["date"]}')
        a += '\nValue of key: '
        a += key
        a += ' is '
        a += str(value["value"])
        a += ' on '
        a += str(value["date"])
    return a
## Завдання 3. Друк максимального значення за допомогою ключа              
def GetLastValueByKey(result_file, data, key):
    """ Write to result_file max value from data by specific key """
    #result_file.write(f'\n\nPrint max value by key: {key}:')
    values = GetValuesByKey(data, key)
    maxPair = values[-1]
    if('value'== 'temp' or 'value'=='feels_like' or 'value'== 'temp_min' or 'value'== 'temp_max'):
        maxPair["value"] += - 273.15
    #result_file.write(f'\nMax value of key: {key} is {maxPair["value"]} on {maxPair["date"]}')
    
    #m = '\nMax value of key: '
    #m += key
    #m += ' is '
    m = str(maxPair["value"])
    #m += ' on '
    #m += str(maxPair["date"])
    return m

def temperature_outside():
    #with open('.\\result.txt', 'a') as result_file:
    result_file = None
    data = GatherAllData(result_file)
    res1 = GetLastValueByKey(result_file, data, 'temp')
    temperature = round(float(res1) - 273.15, 2)
    return temperature
GetDataFromServer()
temp_outside = temperature_outside()
#print(temp_outside)
## спосіб зібрати дані для графіка температурного режиму надворі
##resss = []
##with open('.\\result.txt', 'a') as result_file:
##    data = GatherAllData(result_file)
##    lis = GetValuesByKey(data, 'temp')
##    
##    for value in lis:
##        value['value'] += - 273.15
##        resss.append(round(value["value"], 2))
##print(resss)
