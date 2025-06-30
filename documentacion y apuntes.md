# Documentación: Generador de Contraseñas con Tkinter y Python

## 1. Introducción

Este proyecto consiste en una aplicación de escritorio simple con una interfaz gráfica (GUI) para generar contraseñas seguras y personalizables. El usuario puede especificar la longitud de la contraseña y los tipos de caracteres a incluir (mayúsculas, minúsculas, números, símbolos). La aplicación permite luego copiar la contraseña generada al portapapeles.

El proyecto está dividido en dos archivos Python principales:
* `generador_logica.py`: Contiene la lógica pura de Python para la generación de la contraseña.
* `gui_generador.py`: Contiene el código para construir y manejar la interfaz gráfica de usuario utilizando la librería Tkinter.

## 2. Archivo: `generador_logica.py` (Lógica de Generación)

Este módulo es el cerebro de la aplicación, responsable de crear la contraseña según los criterios dados.

* **Importaciones:**
    * `import random`: Se utiliza para realizar selecciones aleatorias de caracteres y para mezclar la lista final de caracteres de la contraseña. Es fundamental para la aleatoriedad de la contraseña.
    * `import string`: Proporciona cadenas predefinidas de caracteres comunes, lo que facilita la definición de los conjuntos de caracteres a utilizar (ej. `string.ascii_lowercase`, `string.ascii_uppercase`, `string.digits`).

* **Definición de Constantes de Caracteres:**
    ```python
    LETRAS_MINUSCULAS = string.ascii_lowercase
    LETRAS_MAYUSCULAS = string.ascii_uppercase
    NUMEROS = string.digits
    SIMBOLOS = "!@#$%^&*()_+-=[]{};':\",./<>?"
    ```
    * **Anotación:** Se definen como constantes globales (convención de nombres en MAYÚSCULAS) para tener acceso fácil y claro a los conjuntos de caracteres que se usarán para construir la contraseña.

* **Función `generar_contrasena()`:**
    ```python
    def generar_contrasena(longitud, usar_mayusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
        # ... cuerpo de la función ...
    ```
    * **Anotación:** Es la función principal de este módulo.
        * **Parámetros:**
            * `longitud`: Un entero que indica el largo deseado para la contraseña. Es un argumento posicional obligatorio.
            * `usar_mayusculas`, `usar_minusculas`, `usar_numeros`, `usar_simbolos`: Argumentos de palabra clave (keyword arguments) con un valor por defecto de `True`. Esto significa que si no se especifican al llamar la función, se asumirá que se quieren incluir todos los tipos de caracteres.
        * **Construcción de `caracteres_permitidos`:**
            ```python
            caracteres_permitidos = ""
            if usar_minusculas:
                caracteres_permitidos += LETRAS_MINUSCULAS
            # ... (similar para mayúsculas, números, símbolos)
            ```
            * **Anotación:** Se crea una cadena vacía y se le van concatenando los conjuntos de caracteres que el usuario haya elegido (según los parámetros booleanos). Esta cadena será la "piscina" de donde se elegirán los caracteres para la contraseña.
        * **Asegurar Tipos de Caracteres (`contrasena_temporal`):**
            ```python
            contrasena_temporal = []
            if usar_minusculas and longitud > 0:
                contrasena_temporal.append(random.choice(LETRAS_MINUSCULAS))
            # ... (similar para otros tipos, verificando longitud restante)
            ```
            * **Anotación:** Se crea una lista `contrasena_temporal`. Si se solicita un tipo de carácter y la longitud deseada aún lo permite, se añade un carácter aleatorio de ese tipo a la lista. Esto intenta asegurar que la contraseña final contenga al menos un carácter de cada tipo seleccionado, si la longitud es suficiente.
        * **Validación Principal:**
            ```python
            if not caracteres_permitidos and longitud > 0:
                return "Error: Debes seleccionar al menos un tipo de carácter."
            if longitud == 0:
                return ""
            ```
            * **Anotación:** Se verifica que si se pide una contraseña de longitud > 0, al menos un tipo de carácter haya sido seleccionado. Si se pide longitud 0, se devuelve una cadena vacía.
        * **Rellenar y Mezclar:**
            ```python
            longitud_restante = longitud - len(contrasena_temporal)
            for _ in range(longitud_restante):
                contrasena_temporal.append(random.choice(caracteres_permitidos))
            
            random.shuffle(contrasena_temporal)
            ```
            * **Anotación:** Se calculan cuántos caracteres faltan para alcanzar la `longitud` deseada. Se añaden caracteres aleatorios de `caracteres_permitidos` hasta completar. Luego, `random.shuffle()` mezcla todos los caracteres en `contrasena_temporal` para que los caracteres "asegurados" no queden siempre al principio.
        * **Retorno:**
            ```python
            return "".join(contrasena_temporal)
            ```
            * **Anotación:** El método `.join()` toma todos los elementos de la lista `contrasena_temporal` (que son caracteres individuales) y los une en una sola cadena de texto, que es la contraseña final.

* **Bloque `if __name__ == "__main__":` (Para Pruebas):**
    ```python
    if __name__ == "__main__":
        # ... código de prueba ...
    ```
    * **Anotación:** Este bloque especial solo se ejecuta cuando el archivo `generador_logica.py` se corre directamente (ej. `python generador_logica.py`). Si este archivo es *importado* por otro script (como `gui_generador.py`), el código dentro de este `if` *no* se ejecuta. Es útil para poner pruebas de la lógica del módulo sin que afecten a quien lo importa.

## 3. Archivo: `gui_generador.py` (Interfaz Gráfica)

Este módulo crea la ventana y los controles con los que el usuario interactúa.

* **Importaciones:**
    * `import tkinter as tk`: Importa la librería principal de Tkinter, comúnmente con el alias `tk`.
    * `from tkinter import ttk`: `ttk` es un sub-módulo de Tkinter que provee acceso a widgets "temáticos" o más modernos, que suelen verse mejor que los widgets clásicos de Tkinter.
    * `import generador_logica`: Importa el módulo que creamos antes para poder usar su función `generar_contrasena()`.

* **Funciones Controladoras (Callbacks):**
    * **`actualizar_contrasena_gui()`:**
        * **Anotación:** Esta función se ejecuta cuando el usuario presiona el botón "Generar Contraseña".
        * Obtiene los valores actuales de las opciones de la GUI (longitud, qué tipos de caracteres usar) a través de las variables de Tkinter (`longitud_var.get()`, `mayusculas_var.get()`, etc.).
        * Llama a `generador_logica.generar_contrasena()` pasándole estos valores.
        * Actualiza la variable `contrasena_generada_var` (y por ende, el campo de texto en la GUI) con el resultado.
        * Incluye un `try-except Exception as e` para atrapar cualquier error general que pudiera ocurrir y mostrar un mensaje amigable.
    * **`copiar_al_portapapeles()`:**
        * **Anotación:** Se ejecuta con el botón "Copiar".
        * Obtiene la contraseña actual del `contrasena_generada_var`.
        * Usa `ventana.clipboard_clear()` para limpiar el portapapeles del sistema y luego `ventana.clipboard_append()` para añadir la contraseña.
        * Proporciona un feedback simple en la consola (podría mejorarse con un mensaje en la GUI).

* **Configuración de la Ventana Principal (`ventana = tk.Tk()`):**
    * **Anotación:** `tk.Tk()` crea la ventana raíz de la aplicación.
    * `.title()`: Establece el título de la ventana.
    * `.geometry("Ancho_x_Alto")`: Define el tamaño inicial de la ventana en píxeles.
    * `.resizable(False, False)`: Evita que el usuario pueda cambiar el tamaño de la ventana.

* **Estilo `ttk` (Opcional):**
    * **Anotación:** `style = ttk.Style()` y `style.theme_use('clam')` intentan aplicar un tema visual más moderno a los widgets `ttk`. Si el tema no está disponible, usa el de por defecto.

* **Variables de Tkinter:**
    * `tk.StringVar()`, `tk.IntVar()`, `tk.BooleanVar()`:
    * **Anotación:** Son variables especiales de Tkinter que se "enlazan" a los widgets. Cuando el valor de la variable cambia en el código Python, el widget se actualiza automáticamente, y viceversa, si el usuario interactúa con el widget (ej. escribe en un Entry, marca un Checkbutton), la variable de Python toma ese valor.
        * `contrasena_generada_var` (String) para el campo donde se muestra la contraseña.
        * `longitud_var` (Integer) para el slider de longitud.
        * `minusculas_var`, etc. (Boolean) para los checkboxes.

* **Widgets (Elementos de la Interfaz):**
    * `ttk.Frame`, `ttk.LabelFrame`: Contenedores para organizar otros widgets y agruparlos visualmente. `LabelFrame` además muestra un título y un borde.
    * `ttk.Entry`: Campo de texto. Lo usamos para mostrar la contraseña (`textvariable=contrasena_generada_var`, `state="readonly"` para que no se pueda editar). `justify="center"` centra el texto.
    * `ttk.Scale`: Un slider para seleccionar la longitud. `from_` y `to_` definen el rango, `orient=tk.HORIZONTAL`, `variable=longitud_var` lo enlaza a la variable, `length` es el largo visual del slider, `command=lambda s: longitud_var.set(int(float(s)))` actualiza la variable (y el label que muestra el número) en tiempo real mientras se mueve el slider.
        * **`lambda s: ...`**: Una pequeña función anónima. El `Scale` pasa su valor actual como un string (que puede ser float) a esta lambda, la cual lo convierte a `int` y actualiza `longitud_var`.
    * `ttk.Label`: Para mostrar texto estático o el valor de una `StringVar` (`textvariable=longitud_var`).
    * `ttk.Checkbutton`: Casillas de verificación, enlazadas a `BooleanVar`s. `anchor=tk.W` las alinea a la izquierda.
    * `ttk.Button`: Botones, con `text` para la etiqueta y `command` para la función que se ejecuta al hacer clic.

* **Gestor de Layout (`.pack()`):**
    * **Anotación:** Tkinter usa gestores de geometría (`pack`, `grid`, `place`) para posicionar los widgets. `.pack()` es uno de los más simples; va "empaquetando" widgets en el espacio disponible.
    * `fill=tk.X` o `tk.BOTH`: Hace que el widget se expanda para llenar el espacio horizontal (`X`) o ambos (`BOTH`).
    * `expand=True`: Permite que el widget use espacio adicional si la ventana se agranda (aunque aquí la ventana es no redimensionable).
    * `side=tk.LEFT`: Empaqueta el widget a la izquierda del espacio disponible.
    * `anchor=tk.W`: Alinea el widget al Oeste (izquierda) dentro de su celda asignada por `pack`.
    * `padx`, `pady`: Añaden relleno externo horizontal o vertical.
    * `ipady`: Añade relleno interno vertical.

* **Bucle Principal (`ventana.mainloop()`):**
    * **Anotación:** Esta línea es esencial. Inicia el bucle de eventos de Tkinter. La aplicación se queda esperando interacciones del usuario (clics, movimientos de mouse, etc.) y responde a ellas según lo programado. Sin esto, la ventana aparecería y desaparecería instantáneamente.

## 4. Cómo Usar

1.  Asegúrate de tener Python instalado.
2.  Guarda ambos archivos (`generador_logica.py` y `gui_generador.py`) en la misma carpeta.
3.  Abre una terminal en esa carpeta.
4.  Ejecuta el script de la interfaz: `python gui_generador.py`
5.  Interactúa con la ventana para generar y copiar contraseñas.

## 5. Posibles Mejoras Futuras (Ideas)

* Validación de entrada más robusta en `generador_logica.py` (ej. asegurar que `longitud` sea un entero positivo).
* Usar excepciones más específicas en los bloques `try-except` de `gui_generador.py`.
* Añadir un feedback visual más claro en la GUI cuando se copia la contraseña (ej. un mensaje temporal).
* Implementar la funcionalidad de *guardar* contraseñas (esto requeriría pensar en almacenamiento seguro, encriptación, etc., un tema mucho más complejo).
* Añadir un indicador de "fortaleza" de la contraseña generada.