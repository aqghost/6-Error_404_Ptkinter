import tkinter as tk
import sqlite3
from tkinter import messagebox

# Inicialización de base de datos
con = sqlite3.connect("passman.db")
cursor = con.cursor()
cursor.execute("""  CREATE TABLE IF NOT EXISTS manager (
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NOMBREAPP TEXT,
               IDEMAIL TEXT,
               PASSWORD TEXT
               )
""")
con.commit()
con.close()

# Función de envío de formulario para la tabla
def formulario():
    con = sqlite3.connect("passman.db")
    cursor = con.cursor()
    if nombreApp.get()!="" and idEmail.get()!="" and password.get()!="":
        cursor.execute("INSERT INTO manager VALUES (:NOMBREAPP, :IDEMAIL, :PASSWORD)",
            {
                'NOMBREAPP': nombreApp.get(),
                'IDEMAIL': idEmail.get(),
                'PASSWORD': password.get()
            }
        )
        con.commit()
        con.close()
    
        messagebox.showinfo("Éxito", "Su contraseña fue agregada a la base de datos exitosamente!")

        # Limpiar el texto en las entry boxes
        nombreApp.delete(0, END)
        idEmail.delete(0, END)
        password.delete(0, END)

    else:
        messagebox.showinfo("Error", "Por favor, rellene todos los campos.")
        con.close()

# Función de consulta
def query():
    btn_consulta.configure(text="Ocultar Registros", command=ocultarRegistros)
    con = sqlite3.connect("passman.db")
    cursor = con.cursor()

    # Consulta a la tabla
    cursor.execute("SELECT *, oid FROM manager")
    registros = cursor.fetchall()

    mostrarRegistros = ""
    for registro in registros:
        mostrarRegistros += str(registro[4])+ " " + str(registro[0])+ " "+ str(registro[1]) + " " + str(registro[2]) + " " + str(registro[3])

    label_consulta['text'] = mostrarRegistros

    con.commit()
    con.close()

# Función para eliminar registros
def eliminar():
    con = sqlite3.connect("passman.db")
    cursor = con.cursor()

    t = borrarRegistros.get()
    if(t!=""):
        cursor.execute("DELETE FROM manager where oid = " + t)
        borrarRegistros.delete(0, END)
        messagebox.showinfo("Éxito", "Registro %s fue eliminado.")
    else:
        messagebox.showinfo("Error", "Debes ingresar una ID de registro para eliminar!")
    con.commit()
    con.close()

def ocultarRegistros():
    label_consulta['text'] = ""
    btn_consulta.configure(text="Mostrar Registros", command=consulta)

# Ventana
ventana = tk.Tk()
ventana.title("PassMan")
ventana.iconbitmap("passman-logo.ico")
ventana.geometry('450x450')

frame = tk.Frame(ventana, bg="#80c1ff", bd=5)
frame.place(relx=0.50, rely=0.50, relwidth=0.98, relheight=0.45, anchor = "n")

label_nombreApp = tk.Label(ventana, text="Nombre del servicio:")
label_nombreApp.grid(row=1,column=0)
nombreApp = tk.Entry(ventana, width=30)
nombreApp.grid(row=1, column=1, padx=20)

label_idEmail = tk.Label(ventana, text="Email:")
label_idEmail.grid(row=2,column=0)
idEmail = tk.Entry(ventana, width=30)
idEmail.grid(row=2, column=1, padx=20)

label_password = tk.Label(ventana, text="Contraseña:")
label_password.grid(row=3,column=0)
password = tk.Entry(ventana, width=30)
password.grid(row=3, column=1, padx=20)

borrarRegistro = tk.Entry(ventana, width=20)
borrarRegistro.grid(row=6, column=1, padx=20)

btn_formulario = tk.Button(ventana, text = "Agregar Registro", command=formulario)
btn_formulario.grid(row = 5, column=0, pady=5, padx=15, ipadx=35)



ventana.mainloop()