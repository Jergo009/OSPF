import miParamiko
import getpass

#credenciales para establecer conexion
usuario = input('Ingrese usuario: ')
password = getpass.getpass('Ingrese password: ')

linux = {
    'hostname':'192.168.122.1',
    'port':22,
    'username': usuario,
    'password': password
}

cliente = miParamiko.conectar(**linux)
shell = miParamiko.obtener_shell(cliente)

print('-'*50)
nuevo_usuario = input('Ingrese nombre del nuevo usuario: ')
comando = 'sudo useradd -m ' + nuevo_usuario
print(comando)
miParamiko.enviar_comando(shell, comando)
miParamiko.enviar_comando(shell, password)

print('Se ha creado un nuevo usuario ')
respuesta = input('Mostrar usuarios? <s/n>')
if(respuesta == 's'):
    #cortamos usando el delimitador :, mostramos solamente el primer campo
    miParamiko.enviar_comando(shell, 'cut -d: -f 1 /etc/passwd')
    usuarios = miParamiko.mostrar_resultado(shell)
    print(usuarios)