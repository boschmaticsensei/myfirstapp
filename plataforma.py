import webbrowser
import tkinter as tk

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

def open_whats():
    # URL de la página web que deseas abrir
    url = "https://wa.me/5359399064"
    
    # Abre la página web en el navegador predeterminado
    webbrowser.open(url)
    
def open_mail():
    # URL de la página web que deseas abrir
    url = "mailto: boschmatichavana23@gmail.com"
    
    # Abre la página web en el navegador predeterminado
    webbrowser.open(url)


root = tk.Tk()
root.title("NUESTRA PLATAFORMA DE CONTACTO EN LINEA")
root.config(bg="lightgreen")
root.geometry("600x600")



# Cargar imagen del disco.
image = tk.PhotoImage(file="fondo1.png")
# Insertarla en una etiqueta.
label = tk.Label(image=image)
label.pack()

tit = tk.Label(root, text="Diferentes Secciones de la Plataforma en Linea de la Empresa", bg="lightgreen")
tit.config(font=("Arial", 14, "bold"), fg="blue", bg="lightgreen")
tit.place(x=10, y=40)


page = tk.Button(root, text="ABRIR LA PAGINA WEB DE LA EMPRESA", bg="lightgreen", command=open_webpage)
page.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
page.place(x=120, y=90)

store = tk.Button(root, text="ABRIR LA TIENDA VIRTUAL DE LA EMPRESA", bg="lightgreen", command=open_tienda)
store.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
store.place(x=105, y=150)

whats = tk.Button(root, text="ESCRIBANOS AL WHATSAPP LAS 24 H", bg="lightgreen", command=open_whats)
whats.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
whats.place(x=130, y=210)

mail = tk.Button(root, text="ESCRIBANOS AL CORREO ELECTRONICO LAS 24 H", bg="lightgreen", command=open_mail)
mail.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
mail.place(x=80, y=270)

data = tk.Label(root, text="LA EMPRESA BOSCHM@TIC SOLUTION LE SALUDA", bg="lightgreen")
data.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
data.place(x=85, y=350)

data1 = tk.Label(root, text="Y DESEA UN FELIZ FIN DE JORNADA", bg="lightgreen")
data1.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
data1.place(x=130, y=390)

ceo = tk.Label(root, text="Sr. Carlos Igaki Bosch González", bg="lightgreen")
ceo.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
ceo.place(x=140, y=470)

cargo = tk.Label(root, text="Fundador y Director General", bg="lightgreen")
cargo.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
cargo.place(x=155, y=500)

root.mainloop()