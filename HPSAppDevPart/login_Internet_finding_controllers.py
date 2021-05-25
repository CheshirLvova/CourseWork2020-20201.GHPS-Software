from libs import *

router_ip='http://192.168.0.1'
auth_token='Authorization=Basic%20YWRtaW46YjAxYzZmYzYyMDgwMzA5Y2ZiMzc2ZTE4NzI3YzMwNzk%3D'

def logout(session_id):
    r = requests.get(router_ip+'/'+session_id+'/userRpm/LogoutRpm.htm',headers={'Referer':router_ip+'/'+session_id+'/userRpm/MenuRpm.htm','Cookie': auth_token})  
    if r.status_code==200:
        return 'Loging out: '+str(r.status_code)
    else:
        return 'Unnable to logout'

def login():

    r = requests.get(router_ip+'/userRpm/LoginRpm.htm?Save=Save',headers={'Referer':router_ip+'/','Cookie': auth_token})

    if r.status_code==200:
        x=1
        while x<3:
            try:
                session_id=r.text[r.text.index(router_ip)+len(router_ip)+1:r.text.index('userRpm')-1]
                return session_id
                break

            except ValueError:
                return 'Login error'
            
            x+=1
    else:
        return 'IP unreachable'

def routercontrol(operation,remote_ip='255.255.255.255'):
 
        #Авторизація

    if login()=='IP unreachable' or login()=='Login error':
        return login()
        exit(0)

    else:
        session=login()
        print ('Login OK: '+session)
 
    if operation=='Enable ports': 

        #Відкрити Port Forwarding
        r = requests.get(router_ip+'/'+session+'/userRpm/VirtualServerRpm.htm?doAll=EnAll&Page=1',headers={'Referer':router_ip+'/'+session+'/userRpm/VirtualServerRpm.htm','Cookie': auth_token})
        status=str(r.status_code)
        print (logout(session))
        return 'Enable all ports: '+status+' http://31.207.73.10:8082'
 
    elif operation=='Disable ports':

        #Закрити Port Forwarding
        r = requests.get(router_ip+'/'+session+'/userRpm/VirtualServerRpm.htm?doAll=DisAll&Page=1',headers={'Referer':router_ip+'/'+session+'/userRpm/VirtualServerRpm.htm','Cookie': auth_token})
        status=str(r.status_code)
        print (logout(session))
        return 'Disable all ports: '+status
 
    elif operation=='Reboot':

        #Перезавантаження
        r = requests.get(router_ip+'/'+session+'/userRpm/SysRebootRpm.htm?Reboot=%D0%9F%D0%B5%D1%80%D0%B5%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%B8%D1%82%D1%8C',headers={'Referer':router_ip+'/'+session+'/userRpm/SysRebootRpm.htm','Cookie': auth_token})
        status=str(r.status_code)
        print (logout(session))
        return 'Reboot: '+status
 
    elif operation=='Remote IP':
   
        #Зaдаємо IP адреси віддаленого користування
        r = requests.get(router_ip+'/'+session+'/userRpm/ManageControlRpm.htm?port=5110&ip='+remote_ip+'&Save=%D0%A1%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C',headers={'Referer':router_ip+'/'+session+'/userRpm/SysRebootRpm.htm','Cookie': auth_token})
        status=str(r.status_code)
        print (logout(session))
        return 'Remote IP '+remote_ip+': '+status

    elif operation=='Check presence':
  
        #Перевірка підключених пристроїв
        r = requests.get(router_ip+'/'+session+'/userRpm/WlanStationRpm.htm',headers={'Referer':router_ip+'/'+session+'/userRpm/MenuRpm.htm','Cookie': auth_token})
        status=str(r.status_code)
        print (logout(session))
        presence=[]

        if 'DC-31-54-97-51-06' in r.text:
            presence.append('DC-31-54-97-51-06')
        return presence 

    else:
        return 'Wrong command'

#Source code was taken from: https://habr.com/ru/post/342194/
