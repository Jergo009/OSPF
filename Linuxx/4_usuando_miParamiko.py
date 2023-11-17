#importamos nuestro modulo
import miParamiko

cliente = miParamiko.conectar('192.168.122.10',22,'CiscoR1','cisco1')
shell = miParamiko.obtener_shell(cliente)

miParamiko.enviar_comando(shell, 'terminal length 0')
miParamiko.enviar_comando(shell, 'show users')
respuesta = miParamiko.mostrar_resultado(shell)
print(respuesta)

miParamiko.enviar_comando(shell, 'show ip int brief')
respuesta = miParamiko.mostrar_resultado(shell)
print(respuesta)

#usando enable
miParamiko.enviar_comando(shell, 'enable')
miParamiko.enviar_comando(shell, 'cisco1')
miParamiko.enviar_comando(shell, 'configure terminal')
miParamiko.enviar_comando(shell, 'do show users')
miParamiko.enviar_comando(shell, 'end')
respuesta = miParamiko.mostrar_resultado(shell)
print(respuesta)

miParamiko.cerrar(cliente)


#Cliente LINUX

print('-'*100)
print('Dispositivo Linux')
print('-'*100)

linux={'hostname':'192.168.122.1','port':22,'username':'juan','password':'Emma11demarzo5379'}
cliente = miParamiko.conectar(**linux)
shell = miParamiko.obtener_shell(cliente)

miParamiko.enviar_comando(shell, 'whoami',1)
respuesta = miParamiko.mostrar_resultado(shell)
print(respuesta)

miParamiko.enviar_comando(shell, 'ifconfig',1)
respuesta = miParamiko.mostrar_resultado(shell)
print(respuesta)

miParamiko.cerrar(cliente)
