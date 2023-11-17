#verificamos el modo configure
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
conexion.enable()
#verificamos si estamos en modo config
conexion.check_config_mode()
#entramos en modo config
conexion.config_mode()
print(f'Modo config? {conexion.check_config_mode()}')

#enviamos el comando
conexion.send_command('username u2 secret cisco1')
#cerramos el modo config
print('Saliendo del modo config')
conexion.exit_config_mode()
print(f'Modo config? {conexion.check_config_mode()}')
print(f'Modo enable? {conexion.check_enable_mode()}')
#saliendo del modo enable
print('Saliendo del modo enable')
conexion.exit_enable_mode()
print(f'Modo enable? {conexion.check_enable_mode()}')
#Fin ejemplo
print(f'Desconectandose de: {router["host"]}')
conexion.disconnect()