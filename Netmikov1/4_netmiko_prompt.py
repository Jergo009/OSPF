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
prompt = conexion.find_prompt()     #CiscoR1>
if '>' in prompt:
    #entramos a modo enable
    conexion.enable()

salida = conexion.send_command('show run')
print(salida)
print('*'*50)
print('Modo configuracion?',conexion.check_config_mode())
print('*'*50)
if conexion.check_config_mode() == False:
    conexion.config_mode()
print('*'*50)
print('Modo configuracion?',conexion.check_config_mode())
print('*'*50)
salida = conexion.send_command('username u3 secret cisco')
conexion.exit_config_mode()
print(salida)

print('Desconectando del dispositivo ...')
conexion.disconnect()