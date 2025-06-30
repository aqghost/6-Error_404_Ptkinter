import tkinter as tk
# Eliminamos: from tkinter import ttk
import logica

#Funciones que controlan los botones de la interfaz.
def actualizar_contrasena_interfaz():
    #obtiene la contraseña generada por la logica.
    try:
        longitud = longitud_var.get()
        usar_mayus = mayusculas_var.get()
        usar_minus = minusculas_var.get()
        usar_num = numeros_var.get()
        usar_sim = simbolos_var.get()

        #llama a la funcion de generar contraseña
        nueva_contrasena = logica.generar_contrasena (
            longitud,
            usar_mayusculas=usar_mayus,
            usar_minusculas=usar_minus,
            usar_numeros=usar_num,
            usar_simbolos=usar_sim
        )
        contrasena_generada_var.set(nueva_contrasena)
    except Exception as e:
    # Captura cualquier error inesperado durante la generación o al setear la variable.
        contrasena_generada_var.set(f"Error: {e}")

def copiar_contrasena():
    # copia la contraseña generada al portapapeles.
    contrasena_actual = contrasena_generada_var.get()
    #solo copia si no tiene errores.
    if contrasena_actual and not contrasena_actual.startswith("Error:"):
        ventana.clipboard_clear() #limpia el portapapeles.
        ventana.clipboard_append(contrasena_actual) #copia al portapapeles.
        print("¡Contraseña copiada al portapapeles!")
    elif contrasena_actual.startswith("Error:"):
        print("No se puede copiar, hay un error")
    else:
        print("Aún hay ninguna contraseña generada")

#Configuramos la ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("420x480") # Mantenemos un buen tamaño

# Eliminamos las líneas de ttk.Style
# style = ttk.Style()
# try:
#     style.theme_use('clam') #Usamos el tema clam.
# except tk.TclError: #Si clam no anda usamos el tema por defecto.
#     print("Tema 'clam' no disponible, usando tema por defecto.")

# variables de tkinter
contrasena_generada_var =tk.StringVar(value="Tu contraseña aparecerá aquí")
longitud_var = tk.IntVar(value=16) #longitud por defecto de la contraseña
minusculas_var = tk.BooleanVar(value=True)
mayusculas_var = tk.BooleanVar(value=True)
numeros_var = tk.BooleanVar(value=True)
simbolos_var = tk.BooleanVar(value=True)

# Cambiamos ttk.Frame a tk.Frame. El padding se maneja mejor en .pack() para tk.Frame
frame_principal = tk.Frame(ventana)
frame_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20) # Añadimos padx/pady aquí
#Esto es para mostrar la etiqueta de la ventana

#visualizacion de la contraseña generada
#usamos un entry pero le aplicamos "deadonly" para que se vea mas minimal.
# Cambiamos ttk.Entry a tk.Entry
entry_contrasena = tk.Entry(frame_principal, textvariable=contrasena_generada_var, font=("Arial", 16, "bold"), state="readonly", justify="center")
entry_contrasena.pack(fill=tk.X, pady=(0, 15), ipady=5) #ipady lo hace mas alto

#Opciones de generación
# Cambiamos ttk.LabelFrame a tk.LabelFrame. tk.LabelFrame SÍ acepta padx/pady en constructor.
frame_opciones = tk.LabelFrame(frame_principal, text="Personaliza tu Contraseña", padx=15, pady=15)
frame_opciones.pack(fill=tk.X, pady=10)

# Opción de Longitud
# Cambiamos ttk.Frame a tk.Frame
subframe_longitud = tk.Frame(frame_opciones)
subframe_longitud.pack(fill=tk.X, pady=(5,10))
# Cambiamos ttk.Label a tk.Label
label_longitud = tk.Label(subframe_longitud, text="Longitud:")
label_longitud.pack(side=tk.LEFT, padx=(0,10))

# Slider para la longitud
# Cambiamos ttk.Scale a tk.Scale
scale_longitud = tk.Scale(subframe_longitud, from_=8, to=64, orient=tk.HORIZONTAL, variable=longitud_var, length=200, command=lambda s: longitud_var.set(int(float(s))))
scale_longitud.pack(side=tk.LEFT, expand=True, fill=tk.X)
# Label para mostrar el valor actual de la escala
# Cambiamos ttk.Label a tk.Label
label_valor_longitud = tk.Label(subframe_longitud, textvariable=longitud_var, width=3, anchor="w") # anchor w para alinear a la izquierda
label_valor_longitud.pack(side=tk.LEFT, padx=(5,0))

# Checkboxes para tipos de caracteres
# Cambiamos ttk.Checkbutton a tk.Checkbutton
check_minusculas = tk.Checkbutton(frame_opciones, text="Incluir Minúsculas (a-z)", variable=minusculas_var)
check_minusculas.pack(anchor=tk.W, pady=2) # anchor=tk.W para alinear a la izquierda (West)
check_mayusculas = tk.Checkbutton(frame_opciones, text="Incluir Mayúsculas (A-Z)", variable=mayusculas_var)
check_mayusculas.pack(anchor=tk.W, pady=2)
check_numeros = tk.Checkbutton(frame_opciones, text="Incluir Números (0-9)", variable=numeros_var)
check_numeros.pack(anchor=tk.W, pady=2)
check_simbolos = tk.Checkbutton(frame_opciones, text="Incluir Símbolos (!@#...)", variable=simbolos_var)
check_simbolos.pack(anchor=tk.W, pady=2)

# --- Frame para Botones de Acción (Generar, Copiar) ---
# Cambiamos ttk.Frame a tk.Frame
frame_botones_accion = tk.Frame(frame_principal)
frame_botones_accion.pack(fill=tk.X, pady=(20, 0))

# Para centrar los botones, los metemos en un subframe que se centrará por defecto
# Cambiamos ttk.Frame a tk.Frame
subframe_botones = tk.Frame(frame_botones_accion)
subframe_botones.pack() # .pack() sin fill/expand centra el widget

# Cambiamos ttk.Button a tk.Button y eliminamos la opción 'style'
boton_generar = tk.Button(subframe_botones, text="Generar Contraseña", command=actualizar_contrasena_interfaz)
boton_generar.pack(side=tk.LEFT, padx=10, ipady=5)

# Cambiamos ttk.Button a tk.Button
boton_copiar = tk.Button(subframe_botones, text="Copiar", command=copiar_contrasena)
boton_copiar.pack(side=tk.LEFT, padx=10, ipady=5)

# Eliminamos la configuración de estilo para Accent.TButton que ya no aplica
# # Definir un estilo para el botón (opcional, para que se vea más destacado)
# # Esto depende del tema ttk que estés usando.
# # style.configure("Accent.TButton", font=("Arial", 10, "bold"), background="green")


# --- Iniciar el Bucle Principal de la GUI ---
ventana.mainloop()