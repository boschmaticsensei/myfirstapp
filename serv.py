import tkinter as tk
from tkinter import messagebox, font


root = tk.Tk()
root.title("LISTADO DE SERVICIOS DE LA EMPRESA")
root.geometry("600x500")

# Cargar imagen del disco.
image = tk.PhotoImage(file="fondo4.png")
# Insertarla en una etiqueta.
label = tk.Label(image=image)
label.pack()

tit = tk.Label(root, text="SERVICIOS QUE OFERTA NUESTRA EMPRESA", bg="lightyellow")
tit.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
tit.place(x=70, y=20)

serv1 = tk.Label(root, text="1. Reparación y Mantenimiento de Computadoras", bg="lightyellow")
serv1.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
serv1.place(x=35, y=70)

serv2 = tk.Label(root, text="2. Instalación y Actualización de Programas Generales", bg="lightyellow")
serv2.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
serv2.place(x=35, y=110)

s3 = tk.Label(root, text="3. Publicación y Actualización de páginas Web", bg="lightyellow")
s3.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
s3.place(x=35, y=150)

s4 = tk.Label(root, text="4. Diseño y Ejecución de Proyectos de Redes", bg="lightyellow")
s4.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
s4.place(x=35, y=190)

s5 = tk.Label(root, text="5. Diseño de Multimedias Promocionales", bg="lightyellow")
s5.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
s5.place(x=35, y=230)

s6 = tk.Label(root, text="6. Diseño e Impresión de Material Promocional", bg="lightyellow")
s6.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
s6.place(x=35, y=270)

s7 = tk.Label(root, text="7. Programación de Sistemas Simplificados de Contabilidad", bg="lightyellow")
s7.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
s7.place(x=35, y=310)

s8 = tk.Label(root, text="8. Programación de Aplicacions para Windows y Android", bg="lightyellow")
s8.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
s8.place(x=35, y=350)

info = tk.Label(root, text="Los precios varían según a las necesidades del cliente", bg="lightyellow")
info.config(font=("Arial", 14, "bold"), fg="red", bg="lightyellow")
info.place(x=35, y=410)


root.mainloop()