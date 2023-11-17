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
try:
    cliente_ssh.connect(**linux,
                        look_for_keys=False,
                        allow_agent=False, timeout=3)

    miShell = cliente_ssh.invoke_shell()
    miShell .send('whoami\n')
    time.sleep(1)
    salida = miShell.recv(10000).decode()
    print(salida)
except TimeoutError:
    print('Error de tiempo de respuesta, revisar valores')
except paramiko.ssh_exception.AuthenticationException:
    print('Verificar credenciales')
except paramiko.ssh_exception.NoValidConnectionsError:
    print('Error en puerto o direccion ip')
except Exception as e:
    print('Se produjo un error.',e)

#verificamos si la conexion esta activa, para pasar a cerrarla
if(cliente_ssh.get_transport().is_active() == True):
    print('Cerrando la conexion')
    cliente_ssh.close()