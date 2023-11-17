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
#Ejemplo
prompt = conexion.find_prompt()
print(prompt)

if '>' in prompt:
    conexion.enable()
print(conexion.find_prompt())

salida = conexion.send_command('show run')
print(salida)

print(f'Desconectandose de: {router["host"]}')
conexion.disconnect()