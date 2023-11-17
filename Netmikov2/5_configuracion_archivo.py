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
print('enviando comandos desde archivo')
salida = conexion.send_config_from_file('/home/juan/Escritorio/CodigosPython/OSPF/Netmikov2/config/comandos.txt')
print(salida)

#Fin ejemplo
print(f'Desconectandose de: {router["host"]}')
conexion.disconnect()