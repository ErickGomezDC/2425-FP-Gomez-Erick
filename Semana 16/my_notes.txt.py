#Creamos un archivo llamado "my_notes.txt"
#Escritura de Archivo de Texto
with open("my_notes.txt", "w") as archivo: #abrimos el archivo en modo escritura
    archivo.write("1. Buenas tardes mi nombre es Erick Gomez estudiante de fundamentos en programacion\n") #escribimos las líneas que se quieran agregar en el archivo en este caso van a ser 3
    archivo.write("2. La creacion e interaccion de archivos de texto en Python fue muy interesante y divertido.\n")
    archivo.write("3. no se olviden de cerrar el archivo despues de trabajar en el, para no perder el progreso realizado.\n")
#"with" va a cerrar automáticamente al terminar el bloque

#Abrimos el archivo en modo lectura
archivo = open("my_notes.txt", "r")
linea = archivo.readline()  #aquí permitimos que se lea la primera línea del archivo para guardarlo en la variable "linea"

while linea:  # creamos un bucle que se ejecutara mientras haya líneas con contenido
    print(linea.strip())  # imprimimos las líneas del archivo y "strip()" eliminara los saltos de línea
    linea = archivo.readline()  # Lee la siguiente linea del archivo

#nos aseguramos de cerrar el archivo ya que en esta parte no usamos "with"
archivo.close()