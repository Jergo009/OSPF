#Script que realiza backup de un dispositivo
from netmiko import ConnectHandler
import csv

#Leemos el contenido del archivo
dispositivos = []
with open('/home/juan/Escritorio/CodigosPython/OSPF/Netmikov2/config/dispositivos.txt') as archivo:
    lector = csv.reader(archivo)
    for linea in lector:
        dispositivos.append(linea)
#print(dispositivos)
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
    
    #Backup de la configuracion
    salida=conexion.send_command("show run")
    
    #print(salida)
    hostname = conexion.find_prompt()[0:-1]
    #print(hostname)
    
    #agregar informacion de la fecha y hora al nombre del archivo
    from datetime import datetime
    ahora = datetime.now()
    anio = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minuto = ahora.minute
    segundo = ahora.second
    
    nombre_archivo = f'/home/juan/Escritorio/CodigosPython/OSPF/Netmikov2/archivo/{hostname}_{anio}_{mes}_{dia}_{hora}:{minuto}:{segundo}-backup.txt'
    print(nombre_archivo)
    with open(nombre_archivo,'w') as backup:
        backup.write(salida)
        print(f'Backup compelto de {hostname}')
        print('*'*50)
    
    print('Cerrando conexion')
    conexion.disconnect()
    print('#'*50)
