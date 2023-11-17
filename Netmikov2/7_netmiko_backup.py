#Script que realiza backup de un dispositivo
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
    
    #Backup de la configuracion
    salida=conexion.send_command("show run")
    
    #print(salida)
    hostname = conexion.find_prompt()[0:-1]
    #print(hostname)
    nombre_archivo = f'/home/juan/Escritorio/CodigosPython/OSPF/Netmikov2/archivo/{hostname}-backup.txt'
    print(nombre_archivo)
    with open(nombre_archivo,'w') as backup:
        backup.write(salida)
        print(f'Backup compelto de {hostname}')
        print('*'*50)
    
    print('Cerrando conexion')
    conexion.disconnect()
    print('#'*50)