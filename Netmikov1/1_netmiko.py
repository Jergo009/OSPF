import netmiko

conexion = netmiko.Netmiko(host='192.168.122.10',port=22,username='CiscoR1',password='cisco1',device_type='cisco_ios')

salida = conexion.send_command('show ip interface brief')
print(salida)
print('Desconectando...')
conexion.disconnect()