# Get A Key
# Se accede a los valores del diccionario usando su clave

# Diccionario con alturas de edificios
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Imprime el valor asociado a la clave "Burj Khalifa"
print(building_heights["Burj Khalifa"]) # Prints 828

# Imprime el valor asociado a la clave "Ping An"
print(building_heights["Ping An"]) # Prints 599


# Diccionario con elementos del zodiaco
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Imprime la lista asociada a la clave "earth"
print(zodiac_elements["earth"])

# Imprime la lista asociada a la clave "fire"
print(zodiac_elements["fire"])

#------------------------------------------------------------------------------------------

# Get an Invalid Key
# Diccionario de alturas
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# La clave no existe en el diccionario
# -> print(building_heights["Landmark 81"])


# Verifica si una clave existe antes de acceder
key_to_check = "Landmark 81"

# Evalúa si la clave está en el diccionario
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])


# Diccionario de elementos
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Agrega una nueva clave con su valor
zodiac_elements["energy"] = "Not a Zodiac element"

# Verifica si la clave existe y la imprime
if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])


#------------------------------------------------------------------------------------------

# Safely Get a Key
# Diccionario de alturas
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Método get() devuelve el valor de la clave
building_heights.get("Shanghai Tower")

# Devuelve None si la clave no existe
building_heights.get("My House")


# Diccionario de usuarios
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Obtiene el valor de la clave "teraCoder"
user_ids.get("teraCoder")

# Verifica si la clave existe usando get()
if user_ids.get("teraCoder") == None:
   tc_id = 1000
else: 
   tc_id = user_ids.get("teraCoder")

# Imprime el resultado
print(tc_id)

# Si la clave no existe, asigna un valor por defecto
if user_ids.get("superStackSmash") == None:
     stack_id = 100000

print(stack_id)

#-----------------------------------------------------------------------------------------

# Delete a Key
# Método pop() elimina un elemento usando su clave y lo devuelve
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

# Elimina la clave 320291 y devuelve su valor
print(raffle.pop(320291, "No Prize"))

# Imprime el diccionario actualizado
print(raffle)

# Si la clave no existe, devuelve el valor por defecto
print(raffle.pop(100000, "No Prize"))

# Imprime el diccionario actualizado
print(raffle)

# Elimina otra clave
print(raffle.pop(872921, "No Prize"))

# Imprime el diccionario actualizado
print(raffle)


# Diccionario de objetos disponibles
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

# Variable de puntos de salud
health_points = 20

# Elimina elementos y suma sus valores a health_points
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

# Imprime resultados
print(available_items)
print(health_points)

#-------------------------------------------------------------------------------------------

# Get All Keys
# Diccionario de notas
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# Convierte las claves en una lista
print(list(test_scores))

# Recorre e imprime cada clave
for student in test_scores.keys():
 print(student)


# Diccionarios
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Obtiene todas las claves
users = user_ids.keys()
lessons = num_exercises.keys()

# Imprime las claves
print(users)
print(lessons)

#-------------------------------------------------------------------------------------------

# Get All Values
# Diccionario de notas
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# Recorre e imprime los valores
for score_list in test_scores.values():
 print(score_list)

# Diccionario de ejercicios
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Suma todos los valores
total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises

print(total_exercises)

#-------------------------------------------------------------------------------------------

# Get All Items
# Diccionario de marcas
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# Recorre clave y valor
for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")


# Diccionario de ocupaciones
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# Imprime porcentaje por ocupación
for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
