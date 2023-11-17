from datetime import datetime
ahora = datetime.now()
anio = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

nombre_archivo = f'{anio}_{mes}_{dia}_{hora}:{minuto}:{segundo}'

print(nombre_archivo)