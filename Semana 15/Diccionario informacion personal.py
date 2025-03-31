#Diccionario que contiene información personal (ficticia)

#Creamos un Diccionario que contenga información personal (ficticia) como el nombre,edad, ciudad y profesión
informacion_personal = {
    "Nombre": "Renato Aguilar",
    "Edad" : 30,
    "Ciudad" : "Quito",
    "Profesión": "Doctor"
}
# si queremos modificar la ciudad accedemos al valor de la clave que es "ciudad" y lo cambiaremos por otra en este caso es "Guayaquil"
informacion_personal["Ciudad"] = "Guayaquil"

#si queremos agregar una nueva clave valor a nuestro diccionario lo haremos de la siguiente manera en este caso agregaremos el apartado del numero de telefono
if "telefono" not in informacion_personal: #si la clave no se encuentra en el diccionario"
    informacion_personal["Telefono"] = "954-367-901" #se agregara la clave "Telefono" con el siguiente valor "954-367-901"(ficticio)

#si queremos eliminar una clave del diccionario escibimos lo siguiente, llamando al diccionario y la clave que queremos eliminar
del informacion_personal["Edad"]

#Imprimimos la descripción de los datos en este caso es "información personal"
print("=" * 22)
print("INFORMACIÓN PERSONAL")
print("=" * 22)

#Imprimimos los valores para que el usuario pueda observar la información
for clave, valor in informacion_personal.items(): #creamos una lista de pares usando un bucle for
    print(f"{clave}: {valor}")   #esto recorrera cada par imprimiendo en formato de clave con valor de forma descendente