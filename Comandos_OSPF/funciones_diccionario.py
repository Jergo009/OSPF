

def miFuncion(nombre, edad, apellido):
    print(nombre)
    print(edad)
    print(apellido)


miFuncion(apellido='Garcia', edad=40, nombre='Pedro')

valores = {'apellido':'Lujan','edad':35,'nombre':'Luis'}

miFuncion(**valores)

