# importamos los modulos que vamos a necesitar para generar contraseñas.
import random as rd # ramdom genera la aleatoriedad de los numeros.
import string # String contiene caracteres utiles para generar contraseñas.

# Definimos los caracteres que vamos a usar para generar la contraseña.
LETRAS_MINUSCULAS = string.ascii_lowercase # Letras minusculas del alfabeto.
LETRAS_MAYUSCULAS = string.ascii_uppercase # Letras mayusculas del alfabeto.
NUMEROS = string.digits # Numeros del 0 al 9.
SIMBOLOS = "!#$^%&/()_+-*=[]{}:,;'?¡?<>@" # Simbolos especiales.

# Definimos la funcion que va a generar la contraseña.
def generar_contrasena(longitud, usar_mayusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    # Definimos los tipos de caracteres que vamos a usar.
    caracteres_permitidos = "" # Inicializamos la variable que va a contener los caracteres permitidos.
    contrasena_temporal = [] # Inicializamos la lista que va a contener la contraseña temporal.

    if usar_minusculas:
        caracteres_permitidos += LETRAS_MINUSCULAS
    if usar_mayusculas:
        caracteres_permitidos += LETRAS_MAYUSCULAS
    if usar_numeros:
        caracteres_permitidos += NUMEROS
    if usar_simbolos:
        caracteres_permitidos += SIMBOLOS

    # verificamos que haya almenos un tipo de caracter seleccionado si la longitud es mayor a 0.
    if longitud > 0 and not caracteres_permitidos:
        return "Debe seleccionar al menos un tipo de caracter (mayúscula, minúscula, número o símbolo)."
    
    # Si la longitud es 0, devolvemos una cadena vacía.
    if longitud == 0:
        return ""

    # Aseguramos al menos un caracter de cada tipo seleccionado, si es posible y necesario.
    if usar_minusculas:
        contrasena_temporal.append(rd.choice(LETRAS_MINUSCULAS))
    
    if usar_mayusculas and len(contrasena_temporal) < longitud: # Solo añade si aún hay espacio
        contrasena_temporal.append(rd.choice(LETRAS_MAYUSCULAS))
        
    if usar_numeros and len(contrasena_temporal) < longitud: # Solo añade si aún hay espacio
        contrasena_temporal.append(rd.choice(NUMEROS))
        
    if usar_simbolos and len(contrasena_temporal) < longitud: # Solo añade si aún hay espacio
        contrasena_temporal.append(rd.choice(SIMBOLOS))

    # Si después de asegurar caracteres, la lista es más larga que la longitud deseada
    # (porque la longitud era muy pequeña), la recortamos y mezclamos.
    if len(contrasena_temporal) > longitud:
        rd.shuffle(contrasena_temporal) # Mezclar antes de cortar podría ser mejor
        contrasena_temporal = contrasena_temporal[:longitud]
    else:
        # Rellenamos el resto de la contraseña hasta la longitud deseada.
        longitud_restante = longitud - len(contrasena_temporal)
        for _ in range(longitud_restante): # No usamos la variable del bucle.
            contrasena_temporal.append(rd.choice(caracteres_permitidos))
        # Agregamos los caracteres restantes de manera aleatoria.

        rd.shuffle(contrasena_temporal) # Mezclamos los caracteres de la contraseña temporal.
    
    return "".join(contrasena_temporal) # unimos todos los caracteres de la generación en una sola cadena.

#Para hacer pruebas sin tkinter
if __name__ == "__main__":
    print("Prueba 1 (default, L=12):", generar_contrasena(12))
    print("Prueba 2 (L=8, sin mayús, sin símb):", generar_contrasena(8, usar_mayusculas=False, usar_simbolos=False))
    print("Prueba 3 (L=5, solo números):", generar_contrasena(5, usar_mayusculas=False, usar_minusculas=False, usar_simbolos=False))
    print("Prueba 4 (L=2, todos los tipos):", generar_contrasena(2)) # Debería dar 2 caracteres mezclados de los tipos activos
    print("Prueba 5 (L=0):", generar_contrasena(0))
    print("Prueba 6 (Error, sin tipos):", generar_contrasena(10, usar_mayusculas=False, usar_minusculas=False, usar_numeros=False, usar_simbolos=False))