#verificamos el modo configure
from netmiko import ConnectHandler
import csv

#Leemos el contenido del archivo
dispositivos = []
with open('/home/juan/Escritorio/CodigosPython/OSPF/Netmikov2/config/dispositivos.txt') as f:
    lector = csv.reader(f)
    for linea in lector:
        dispositivos.append(linea)
    
    #resolviendo enuna sola linea
    #routers = list(linea for linea in lector)
print(dispositivos)
#print(routers)

#una vez tenemos la info de los dispositivo en una varialbe, creamos los diccionarios
lista_dispositivos = []#list()
for ip, password, usuario in dispositivos:
    router = {
        'device_type':'cisco_ios',
        'host':ip,
        'username': usuario,
        'password': password,
        'port':22,
        'secret': password,
        'verbose':True
    }
    #agregamos el diccionario a la lista de dispositivos.
    lista_dispositivos.append(router)

for dispositivo in lista_dispositivos:
    conexion = ConnectHandler(**dispositivo)
    print('Entrando en modo enable...')
    conexion.enable()
    
    #archivo_comandos = input(f'Ingrese archivo de config (ruta validad) para {dispositivo["host"]}')#el usuario indica la ruta
    salida = conexion.send_config_from_file('/home/juan/Escritorio/CodigosPython/OSPF/Netmikov2/config/comandos.txt')
    print(salida)
        
    print('Cerrando conexion')
    conexion.disconnect()
    print('#'*50)