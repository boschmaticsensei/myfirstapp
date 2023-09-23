import webbrowser
import subprocess
import tkinter as tk
from tkinter import messagebox, font

def abrir_platadorma():
    subprocess.Popen(["python", "plataforma.py"])
    
def abrir_serv():
    subprocess.Popen(["python", "serv.py"])

def abrir_programa2():
    pass

def abrir_ubic():
    subprocess.Popen(["python", "ubic.py"])
    
def open_webpage():
    # URL de la página web que deseas abrir
    url = "https://boschmaticsolutions.simdif.com"
    
    # Abre la página web en el navegador predeterminado
    webbrowser.open(url)

def open_tienda():
    # URL de la página web que deseas abrir
    url = "https://boschmatichavana23.mabisy.com"
    
    # Abre la página web en el navegador predeterminado
    webbrowser.open(url)



def somos():
    messagebox.showinfo(message="Somos la Empresa de Servicios Informáticos y Tecnológicos BoschM@tic Solutions, Prestamos servicios de reparacion y mantenimiento de equipos electrónicos de todo tioia particulares, TCP, Cooperativas no Agropecuarias y MyPymes", title="SOBRE NOSOTROS")

def serv():
    messagebox.showinfo(message="Prestamos resvicios de: Reparación y Mantenimiento de Computadoras, Instalación de Programas como Sistemas Operativos y Cualquier otro programa, Diseño y Actualización de Páginas web, Diseño de multimedias, Diseño y Ejecución de proyectos de redes y muchos mas", title="MEJORES PRECIOS, MEJOR SERVICIO")

def eq():
    messagebox.showinfo(message="Contamos con un Equipo de Profesionales Altamente Calificados y con mas de 15 años de Experiecia en su trabajo. Siempre en constante superación en busca de la Excelencia en cada Servcio o Producto que Ofertamos", title="NUESTRO EQUIPO DE PROFESIONALES")



root = tk.Tk()
root.title("PROGRAMA DE BOSCHM@TIC SOLUTIONS")
root.config(bg="lightgreen")
root.geometry("600x600")


# Cargar imagen del disco.
image = tk.PhotoImage(file="fondo.png")
# Insertarla en una etiqueta.
label = tk.Label(image=image)
label.pack()

tit = tk.Label(root, text="Información Detallada sobre nuestra Empresa", bg="lightgreen")
tit.config(font=("Arial", 14, "bold"), fg="blue", bg="lightgreen")
tit.place(x=80, y=10)

nos = tk.Button(root, text="ACERCA DE NOSOTROS", bg="lightgreen", command=somos)
nos.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
nos.place(x=30, y=70)

serv = tk.Button(root, text="SERVICIOS QUE OFERTAMOS", bg="lightgreen", command=serv)
serv.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
serv.place(x=320, y=70)

eq = tk.Button(root, text="EL EQUIPO DE TRABAJO", bg="lightgreen", command=eq)
eq.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
eq.place(x=30, y=140)

plat = tk.Button(root, text="PLATAFORMA DE CONTACTOS", bg="lightgreen", command=abrir_platadorma)
plat.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
plat.place(x=320, y=140)

servicios = tk.Button(root, text="LISTADO DE SERVICIOS", bg="lightgreen", command=abrir_serv)
servicios.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
servicios.place(x=30, y=210)

ubic = tk.Button(root, text="UBICACION SEDE CENTRAL", bg="lightgreen", command=abrir_ubic)
ubic.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
ubic.place(x=320, y=210)

page = tk.Button(root, text="ABRIR LA PAGINA WEB DE LA EMPRESA", bg="lightgreen", command=open_webpage)
page.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
page.place(x=120, y=520)

store = tk.Button(root, text="ABRIR LA TIENDA VIRTUAL DE LA EMPRESA", bg="lightgreen", command=open_tienda)
store.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
store.place(x=105, y=470)

root.mainloop()
