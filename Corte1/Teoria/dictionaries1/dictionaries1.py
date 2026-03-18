
# Diccionarios

# Se crean diccionarios con pares clave:valor
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

# Imprime los diccionarios
print(sensors)
print(num_cameras)

# Diccionario de traducciones
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)

# las listas no pueden ser claves en un diccionario (no son inmutables)
# -> powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

# Diccionario con listas como valores
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
            "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# Diccionario vacío
my_empty_dictionary = {}
print(my_empty_dictionary)

# Diccionario menú
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Imprime el diccionario antes de modificarlo
print("Before: ", menu)

# Agrega un nuevo elemento al diccionario
menu["cheesecake"] = 8

# Imprime el diccionario actualizado
print("After", menu)

# Sobrescribe el diccionario (pierde el valor anterior)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)

#-------------------------------------------------------------------------------

# Agregar múltiples claves

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

# Método que agrega múltiples elementos al diccionario
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Imprime el diccionario actualizado
print("After", sensors)

# Otro ejemplo con update()
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)

# Agrega nuevos usuarios
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#-------------------------------------------------------------------------------

# Sobrescribir valores
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# Modifica el valor de una clave existente
menu["oatmeal"] = 5

# Imprime el diccionario actualizado
print("After", menu)

# Ejemplo con premios Oscar
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

print("Before", oscar_winners)
print()

# Agrega un nuevo elemento
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()

# Sobrescribe un valor existente
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)

#-------------------------------------------------------------------------------

# Dict Comprehensions

# Listas de nombres y alturas
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip() combina dos listas en pares (tuplas)
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

# Crea un diccionario a partir de dos listas
students = {key:value for key, value in zip(names, heights)}

# Imprime el diccionario resultante
print(students)

#-------------------------------------------------------------------------------

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Combina listas con zip()
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

# Convierte a diccionario
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

#-------------------------------------------------------------------------------

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Crea un diccionario combinando listas
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

# Agrega una nueva canción
plays.update({"Purple Haze": 1})

# Modifica el valor de una canción existente
plays.update({"Respect": 94})

# Imprime el diccionario actualizado
print("After: ", plays)

# Diccionario anidado
library = {"The Best Songs": plays, "Sunday Feelings": {}}

# Imprime la biblioteca
print(library)