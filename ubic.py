import tkinter as tk



root = tk.Tk()
root.title("UBICACION DELA EMPRESA")
root.config(bg="lightgreen")
root.geometry("600x500")


# Cargar imagen del disco.
image = tk.PhotoImage(file="fondo5.png")
# Insertarla en una etiqueta.
label = tk.Label(image=image)
label.pack()

tit = tk.Label(root, text="UBICACION DE NUESTRA EMPRESA", bg="lightgreen")
tit.config(font=("Arial", 14, "bold"), fg="blue", bg="lightgreen")
tit.place(x=135, y=10)

addr = tk.Label(root, text="Calle C # 302 e/ Loma y Central. Rpto Mendoza. A. Naranjo. Cerca del Capri", bg="lightgreen")
addr.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
addr.place(x=15, y=80)

hor = tk.Label(root, text="Abrimos de lunes a Viernes de 9 Am a 5 Pm", bg="lightgreen")
hor.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
hor.place(x=15, y=150)

info = tk.Label(root, text="CONTACTANOS CON 72 HORAS DE ANTELACION", bg="lightgreen")
info.config(font=("Arial", 12, "bold"), fg="blue", bg="lightgreen")
info.place(x=50, y=410)




root.mainloop()