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

print(f'{"*"*10}Entrando en modo enable')
conexion.enable()
#forma1, una lista
comandos = ['interface loopback 0',
            'ip address 1.1.1.1 255.255.255.255',
            'exit',
            'username netmiko secet cisco']
#Enviamos la lista de comandos
conexion.send_config_set(comandos)

#Forma 2, cadena de caracteres con separadores unicos
comandos_cadena= 'interface loopback 1;ip address 2.2.2.2 255.255.255.255;exit;username netmiko2 secet cisco'
#convertimos la cadena a una lista de comandos
conexion.send_config_set(comandos_cadena.split(';'))

#Forma 3, cadena multilinea
comando_multi_linea='''interface loopback 2
ip address 3.3.3.3 255.255.255.255
exit
username netmiko3 secet cisco'''
conexion.send_config_set(comando_multi_linea.split('\n'))


#Fin ejemplo
print(f'Desconectandose de: {router["host"]}')
conexion.disconnect()