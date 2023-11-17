#scp secure copy
#Por medio de ssh permite compartir archivos

import miParamiko
#instalr scp con pip
#pip install scp

import scp

linux = {
    'hostname':'192.168.122.1',
    'port':22,
    'username':'juan',
    'password':'Emma11demarzo5379'
}

cliente = miParamiko.conectar(**linux)
shell = miParamiko.obtener_shell(cliente)

#objeto scp
#usamos la capa de transporte de paramiko
objetoSCP = scp.SCPClient(cliente.get_transport())
#enviar un archivo hacia el destino
#/home/juan/Escritorio
origen  = '/home/juan/Escritorio/prueba.txt'
destino = '/home/juan/Escritorio/CodigosPython/OSPF/recibido.txt'
objetoSCP.put(origen,destino)
miParamiko.cerrar(cliente)