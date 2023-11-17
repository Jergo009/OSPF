import paramiko
import time

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

#enviar comandos con el metodo exec command()
#se trabajo con el flujo de salida
fEntrada, fSalida, fError = cliente_ssh.exec_command('ifconfig\n')  #devuelve una tupla
time.sleep(1)
salida = fSalida.read().decode()
print(salida)

fEntrada, fSalida, fError = cliente_ssh.exec_command('who\n')  #devuelve una tupla
time.sleep(1)
salida = fSalida.read().decode()
print(salida)

#Flujo de Error
fEntrada, fSalida, fError = cliente_ssh.exec_command('whoQ\n')  #devuelve una tupla
time.sleep(1)
error = fError.read().decode()
print('------->', error)

#Flujo de Entrada
fEntrada, fSalida, fError = cliente_ssh.exec_command('sudo ifconfig\n', get_pty=True)  #devuelve una tupla
fEntrada.write('Emma11demarzo5379\n')
time.sleep(1)
print(fSalida.read().decode())

#verificamos si la conexion esta activa, para pasar a cerrarla
if(cliente_ssh.get_transport().is_active() == True):
    print('Cerrando la conexion')
    cliente_ssh.close()