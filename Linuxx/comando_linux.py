import paramiko
import time


#crear  cliente 
cliente_ssh = paramiko.SSHClient()
cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#variables para identificar el dispositivo
linux = {
    'hostname':'192.168.122.1',
    'port':22,
    'username':'juan',
    'password':'Emma11demarzo5379'
}

print('*'*50)
print('Conectandose a: ', linux['hostname'])
print('*'*50)

cliente_ssh.connect(**linux,
                    look_for_keys=False,
                    allow_agent=False)

miShell = cliente_ssh.invoke_shell()
miShell.send('whoami\n')
miShell.send('pwd\n')
miShell.send('cd /home/juan/Escritorio\n')
miShell.send('mkdir PRUEBA_CARPETA\n')
miShell.send('cat /etc/passwd\n')
miShell.send('ifconfig\n')
time.sleep(2)

salida = miShell.recv(10000).decode()
print(salida)

#verificamos si la conexion esta activa, para pasar a cerrarla
if(cliente_ssh.get_transport().is_active() == True):
    print('Cerrando la conexion')
    cliente_ssh.close()

