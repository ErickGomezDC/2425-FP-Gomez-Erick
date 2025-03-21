#Programa que calcula el descuento de compras con el uso de funciones y parámetros

#Creamos una funcion para calcular el descuento

def calcular_descuento (monto_total_decompra, porcentaje_de_descuento=30): #esta función recibira dos valores valor total de la compra y valor predeterminado del descuento de 30%
    descuento = (monto_total_decompra * porcentaje_de_descuento) / 100 #calculo del descuento aplicado al porcentaje del monto total
    return descuento #retorna al valor del descuento calculado

#Cree una tienda basada en un mundo de mazmorras y dragones para hacerlo más interesante
print("_" * 30)
print("TIENDA DEL ARCANO POLVORIENTO")
print("_" * 30)
print("=" * 20)
print("OBJETOS DISPONIBLES:")
print("=" * 20)
print("Piedra luz Eterna 5x = $300 ")
print("Anillo de Protección +5 x1 = $500")
print("Grimorio de encantamientos avanzados x1 = $1000")
print("." * 20)

#Primera llamada a la función: solo con monto total de la compra
print("")
print("Compra 1:")
monto1 = float(input("ingresa el valor del objeto que desea adquirir: $")) #pedimos al usuario que ingrese el monto de la compra
descuento1 = calcular_descuento(monto1) #llamamos a la función con la variable "monto1" y como no se proporciona un segundo parametro se usa el valor por defecto que es 30%
monto_con_descuento1 = monto1 - descuento1 #calcula el monto del usuario para poder pagar despues del descuento
print(f"  Descuento aplicado por nuevo aventurero (30%) valor a restar: ${descuento1}") #proporcionamos el valor del descuento aplicado y el valor a pagar
print(f"  Monto final a pagar con descuento incluido!: ${monto_con_descuento1}\n")
print("Recoge tu objeto!")
print("")
print("." * 60)

#Segunda llamada a la función: monto total de la compra con porcentaje de descuento adicional
print("Compra 2:")
monto2 = float(input("ingresa el valor del objeto que desea adquirir: $"))#pedimos al usuario que ingrese el monto de la compra
porcentaje = float(input("Por nuevo aventurero puede ingresar el descuento de su elección para tu compra: %"))#pedimos al usuario que ingrese el valor del descuento para su compra
descuento2 = calcular_descuento (monto2, porcentaje) #llamamos a la función con la variable "monto2" y como se proporciona el descuento solo realiza el calculo del descuento
monto_con_descuento2 = monto2 - descuento2  #calcula el monto del usuario para poder pagar despues del descuento
print(f"  Descuento aplicado ({porcentaje}%) valor a restar: ${descuento2}")
print(f"  Monto final a pagar con descuento incluido!: ${monto_con_descuento2}") #proporcionamos el valor del descuento aplicado y el valor a pagar
print("")
print("Recoge tu objeto!")
print("." * 23)
print("Gracias por su compra")