import miParamiko

router1 ={'hostname':'192.168.122.10','port':22,'username':'CiscoR1','password':'cisco1'}
router2 ={'hostname':'192.168.122.20','port':22,'username':'CiscoR2','password':'cisco2'}
router3 ={'hostname':'192.168.122.30','port':22,'username':'CiscoR3','password':'cisco3'}

dispositivos = [router1,router2,router3]

for router in dispositivos:
    cliente = miParamiko.conectar(**router)
    shell = miParamiko.obtener_shell(cliente)

    #enviado comandos
    miParamiko.enviar_comando(shell, 'terminal length 0')
    miParamiko.enviar_comando(shell, 'enable')
    miParamiko.enviar_comando(shell, router['password'])
    miParamiko.enviar_comando(shell, 'show run') #muestra la configuracion actual.

    salida = miParamiko.mostrar_resultado(shell)
    salida_lista = salida.splitlines()
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

    with open('miParamiko/archivos/backups/'+nombre_archivo, 'w') as f:
        f.write(salida)

    miParamiko.cerrar(cliente)
    
print('-------> Fin de la operacion')