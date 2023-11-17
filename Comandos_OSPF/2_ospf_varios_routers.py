

import paramiko
import time

cliente_ssh = paramiko.SSHClient()
cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {
    'hostname' : '192.168.122.10',
    'port' : 22,
    'username' : 'CiscoR1',
    'password' : 'cisco1'
}

router2 = {
    'hostname' : '192.168.122.20',
    'port' : 22,
    'username' : 'CiscoR2',
    'password' : 'cisco2'
}

router3 = {
    'hostname' : '192.168.122.30',
    'port' : 22,
    'username' : 'CiscoR3',
    'password' : 'cisco3'
}

dispositivos= [router1, router2, router3]

#for que aplica configuraciones
for router in dispositivos:
    print('*'*50)
    print('Conectandose a: ',router['hostname'])
    print('*'*50)

    cliente_ssh.connect(**router,
                        look_for_keys=False, #permite el intecambio de llaves, pero se realizo de manera manual en la linea 6
                        allow_agent=False)   #permite recordar las sesiones

    #crear un shell para enviar comandos
    miShell = cliente_ssh.invoke_shell()
    #habilitar OSPF
    miShell.send('enable\n')
    #interpolacion de candenas para enviar el password
    miShell.send(f'{router["password"]}\n')
    miShell.send('configure terminal\n')
    miShell.send('router ospf 1\n')
    miShell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    miShell.send('end\n')
    #miShell.send('no router ospf 1\n') #desabilitar ospf
    #miShell.send('end\n')
    miShell.send('terminal length 0\n')
    miShell.send('show ip protocols\n')
    time.sleep(2)                           #damos tiempo para que de respuesta el router
    #10000 es la cantidad de caracteres a visualizar
    salida = miShell.recv(10000).decode()   #pasamos de bytes a texto
    print(salida)
#fin del for de configuracion

#verificamos si la conexion esta activa, para pasar a cerrarla
if(cliente_ssh.get_transport().is_active() == True):
    print('Cerrando la conexion')
    cliente_ssh.close()
