import paramiko
import time

#Funcion para establecer conexion a dispositivos mediante ssh v2
def conectar(hostname, port, username, password):
    """Funcion que permite conectarse a un dispositivo por medio de ssh

    Args:
        hostname str: IP del dispositivo
        port int: Puerto a utilizar
        username str: Usuario
        password str: Contraseña

    Returns:
        SSHClient: Un Cliente SSH
    """
    cliente_ssh = paramiko.SSHClient()
    cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    print('*'*50)
    print('Conectandose a: ',hostname)
    print('*'*50)
    cliente_ssh.connect(hostname=hostname,port=port,username=username,password=password,
                        look_for_keys=False,
                        allow_agent=False)
    return cliente_ssh

#Funcion para obtener shell
def obtener_shell(cliente):
    """Funcion para obtener un Shell

    Args:
        cliente clienteSSH: _clienteSSH

    Returns:
        Shell: shell del cliente
    """
    shell = cliente.invoke_shell()
    return shell

#Funcion para enviar comandos
def enviar_comando(shell, comando, tiempo=2):
    print('-'*50)
    print(f'Enviando el comando: {comando}')
    print('-'*50)
    shell.send(comando + '\n')
    time.sleep(tiempo)

#Funcion para mostrar resultados
def mostrar_resultado(shell, bytes=10000):
    salida = shell.recv(bytes).decode()
    return salida

#Funcion para cerrar conexiones
def cerrar(cliente):
    if(cliente.get_transport().is_active() == True):
        print('Cerrando la conexion')
        cliente.close()
    #return cliente
