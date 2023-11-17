from netmiko import ConnectHandler



router = {
    'device_type': 'cisco_ios',
    'host':'192.168.122.10',
    'username':'CiscoR1',
    'password':'cisco1',
    'port':22,                      #Opcional, por defecto es 22
    'secret':'cisco1',              #password para enable, por defecto es ''
    'verbose':True                  #opcional, falso por defecto
}

conexion = ConnectHandler(**router)
prompt = conexion.find_prompt()     #devuelve el prompt actual, util para sabet si estamos en modo enable.
print(prompt)
conexion.enable()
prompt = conexion.find_prompt()     #devuelve el prompt actual, util para sabet si estamos en modo enable.
print(prompt)
print('Desconectando del dispositivo ...')
conexion.disconnect()