import miParamiko

router ={
    'hostname':'192.168.122.10',
    'port':22,
    'username':'CiscoR1',
    'password':'cisco1'
}

cliente = miParamiko.conectar(**router)
shell = miParamiko.obtener_shell(cliente)

#enviado comandos
miParamiko.enviar_comando(shell, 'terminal length 0')
miParamiko.enviar_comando(shell, 'enable')
miParamiko.enviar_comando(shell, 'cisco1')
miParamiko.enviar_comando(shell, 'show run') #muestra la configuracion actual.

salida = miParamiko.mostrar_resultado(shell)
#print(salida)

salida_lista = salida.splitlines()
print('Longitud de la lista: ', len(salida_lista))
#print(salida_lista)

#print('-'*20, 'LISTADO', '-'*20)
#print(salida_lista[12: -2])#iniciamos en version y terminamos en end
salida = salida_lista[12: -2]
salida = '\n'.join(salida)

#agregar informacion de la fecha y hora al nombre del archivo
from datetime import datetime
ahora = datetime.now()
anio = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

nombre_archivo = f'{router["username"]}_{anio}_{mes}_{dia}_{hora}:{minuto}:{segundo}'

print(nombre_archivo)


with open('miParamiko/archivos/backups/'+nombre_archivo, 'w') as f:
    f.write(salida)

miParamiko.cerrar(cliente)