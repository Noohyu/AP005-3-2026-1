#Se crea la lista
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# Función que permite la entrada de datos, pero no guarda ni se usa 
# Aunque internamente devuelva el valor String
# -> input()

# Imprime el array
print(my_lista)
# Imprime el tipo de dato
print(type(my_lista))
# Imprime 'Amarillo' o el tercer elemento
print(my_lista[2])

# Función que devuelve la cantidad de elementos de la lista
print("my_lista size: ", len(my_lista))
# Imprime una lista que contiene los elementos desde el índice 0 hasta el 1
# (no incluye el índice final)
print(my_lista[0:2])
# Es equivalente a print(my_lista[0:2]), ya que se asume que inicia desde el índice 0
print(my_lista[:2])

# Método que agrega un elemento al final de la lista
my_lista.append('Blanco')     
# Imprime la lista actualizada
print(my_lista)

# Método que inserta el valor 'Negro' en el índice 3 
# y desplaza los demás elementos hacia la derecha
my_lista.insert(3, 'Negro')
print(my_lista)

# Método que agrega elementos al final de la lista
my_lista.extend(['Marron', 'Gris']) 
print(my_lista)

# Imprime el índice del elemento 'Azul'
print(my_lista.index('Azul'))

# Método que elimina el elemento 'Marron'
my_lista.remove('Marron')
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

# Método que elimina un elemento basandosé en su índice y lo devuelve 
print(my_lista.pop())
size = len(my_lista)
print("size = ", size)

# Índice fuera de rango
# -> print(my_lista.pop(size))

# Repite la lista 3 veces
my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
# Método que ordena la lista de forma ascendente
my_listaSort = my_lista.sort()
# Ordena la lista original y no devuelve ninguna lista (retorna None)
print(my_listaSort)

# Nuevo array
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
# Mismo error que antes
# -> OrderedLList = my_NumList.sort()
# Llama el anterior error
# -> print(my_listaSort)

#Ordena la lista de mayor a menor correctamente
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)
print()
print()

#-------------------------------------------------------------------------------

#Tuplas

# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables

print("###########################")
print("###########TUPLAS##########")
print("###########################")


# Convierte la lista en una tupla
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

# Imprime los elementos en los índices 0 y 2
print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
#Cantidad de veces que aparece el 'Rojo' en la tupla
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
