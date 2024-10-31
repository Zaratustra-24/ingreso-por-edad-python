# Paso 1: Soliictar al usuario que ingrese la esas del cliente 
edad = int(input("Por favor, ingresa tu edad: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca

permitido = True if edad >= 18 else False # ternario

# Paso 3: Mostrar al usuaerio si su cliente puede o no ingresar a la discoteca
if permitido:
    print("¡Puedes ingreesar a la discoteca!")
else:
    print("Lo siento mucho, no se puede ingresar a la disacoteca siendo menor de edad")
