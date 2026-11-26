import tkinter as tk
from tkinter import messagebox

def calcular_media(event=None):
    texto = entrada.get().strip()

    if not texto:
        return

    try:
        notas = [float(nota.strip()) for nota in texto.split(",")]

        media = sum(notas) / len(notas)

        resultado.config(
            text=f"✅ Media: {media:.2f}",
            fg="green"
        )

        entrada.delete(0, tk.END)
        entrada.focus()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Introduce las notas separadas por comas.\nEjemplo: 7.5, 8, 6.25, 9"
        )

ventana = tk.Tk()
ventana.title("Calculadora de Medias")
ventana.geometry("500x250")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="Calculadora rápida de medias",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

instrucciones = tk.Label(
    ventana,
    text="Introduce las notas separadas por comas\nEjemplo: 7.5, 8, 6.25, 9"
)
instrucciones.pack(pady=5)

entrada = tk.Entry(
    ventana,
    width=50,
    justify="center",
    font=("Arial", 12)
)
entrada.pack(pady=10)

entrada.bind("<Return>", calcular_media)

boton = tk.Button(
    ventana,
    text="Calcular Media",
    command=calcular_media,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold")
)
boton.pack(pady=10)

resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 18, "bold")
)
resultado.pack(pady=15)

entrada.focus()

ventana.mainloop()