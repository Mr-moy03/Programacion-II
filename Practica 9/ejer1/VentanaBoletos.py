import tkinter as tk
from tkinter import ttk, messagebox
from Boleto import Boleto
from Palco import Palco
from Platea import Platea
from Galeria import Galeria

class VentanaBoletos:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Teatro Municipal")
        self.raiz.geometry("420x350")
        self.raiz.configure(bg="white")
        self.raiz.resizable(False, False)

        self.tipo_boleto = tk.StringVar(value="Palco")
        self.numero = tk.StringVar()
        self.dias = tk.StringVar()
        self.resultado = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.raiz, text="Teatro Municipal", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        # Marco superior
        marco_superior = tk.LabelFrame(self.raiz, text="Datos del Boleto", bg="white", padx=10, pady=10)
        marco_superior.pack(padx=10, pady=10, fill="x")
        # Opciones
        opciones_frame = tk.Frame(marco_superior, bg="white")
        opciones_frame.pack(pady=5)
        opciones = [("Palco", "Palco"), ("Platea", "Platea"), ("Galeria", "Galeria")]
        for texto, valor in opciones:
            tk.Radiobutton(opciones_frame, text=texto, variable=self.tipo_boleto,
                           value=valor, bg="white", command=self.actualizar_estado).pack(side="left", padx=5)
        # entrada
        entrada_frame = tk.Frame(marco_superior, bg="white")
        entrada_frame.pack(pady=10)
        tk.Label(entrada_frame, text="Número:", bg="white").grid(row=0, column=0, sticky="e", padx=5)
        tk.Entry(entrada_frame, textvariable=self.numero, width=10).grid(row=0, column=1, sticky="w")
        tk.Label(entrada_frame, text="Días antes:", bg="white").grid(row=1, column=0, sticky="e", padx=5)
        self.campo_dias = tk.Entry(entrada_frame, textvariable=self.dias, width=10, state="disabled")
        self.campo_dias.grid(row=1, column=1, sticky="w")
        # Botones
        botones_frame = tk.Frame(marco_superior, bg="white")
        botones_frame.pack(pady=10)
        tk.Button(botones_frame, text="Vender", width=10, command=self.vender).pack(side="left", padx=10)
        tk.Button(botones_frame, text="Salir", width=10, command=self.raiz.quit).pack(side="left", padx=10)
        # Marco inferior
        marco_inferior = tk.LabelFrame(self.raiz, text="Información del Boleto", bg="white", padx=10, pady=10)
        marco_inferior.pack(padx=10, pady=5, fill="x", expand=True)
        self.etiqueta_resultado = tk.Label(marco_inferior, textvariable=self.resultado, bg="white",
                                           fg="blue", font=("Arial", 10, "bold"), wraplength=380)
        self.etiqueta_resultado.pack(pady=10)

    def actualizar_estado(self):
        if self.tipo_boleto.get() in ["Galeria", "Platea"]:
            self.campo_dias.config(state="normal")
        else:
            self.campo_dias.config(state="disabled")
            self.dias.set("")

    def vender(self):
        try:
            numero = int(self.numero.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número de boleto válido.")
            return

        tipo = self.tipo_boleto.get()

        if tipo == "Palco":
            boleto = Palco(numero)
        elif tipo in ["Platea", "Galeria"]:
            try:
                dias = int(self.dias.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese la cantidad de días de anticipación.")
                return
            if tipo == "Platea":
                boleto = Platea(numero, dias)
            else:
                boleto = Galeria(numero, dias)
        else:
            return

        self.resultado.set(str(boleto))