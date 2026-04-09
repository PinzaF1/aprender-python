import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AplicacionVisual:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Visual - Calculadora")
        self.root.geometry("400x500")
        self.root.config(bg="#2b2b2b")
        
        # Título
        titulo = tk.Label(
            root,
            text="Calculadora",
            font=("Arial", 24, "bold"),
            bg="#2b2b2b",
            fg="#00ff00"
        )
        titulo.pack(pady=20)
        
        # Pantalla de resultado
        self.pantalla = tk.Entry(
            root,
            font=("Arial", 20),
            justify="right",
            bg="#1e1e1e",
            fg="#00ff00",
            bd=2,
            relief="sunken"
        )
        self.pantalla.pack(padx=10, pady=10, fill="x")
        self.pantalla.insert(0, "0")
        
        # Frame para botones
        frame_botones = tk.Frame(root, bg="#2b2b2b")
        frame_botones.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Botones
        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for fila in botones:
            frame_fila = tk.Frame(frame_botones, bg="#2b2b2b")
            frame_fila.pack(fill="both", expand=True, pady=5)
            
            for boton_texto in fila:
                btn = tk.Button(
                    frame_fila,
                    text=boton_texto,
                    font=("Arial", 18, "bold"),
                    bg="#404040" if boton_texto != "=" else "#00aa00",
                    fg="#ffffff",
                    activebackground="#505050",
                    command=lambda x=boton_texto: self.presionar_boton(x)
                )
                btn.pack(side="left", fill="both", expand=True, padx=2)
        
        # Botón limpiar
        btn_limpiar = tk.Button(
            root,
            text="Limpiar (C)",
            font=("Arial", 12, "bold"),
            bg="#aa0000",
            fg="white",
            command=self.limpiar,
            activebackground="#cc0000"
        )
        btn_limpiar.pack(padx=10, pady=5, fill="x")
        
        # Label de info
        self.info = tk.Label(
            root,
            text=f"Hora: {datetime.now().strftime('%H:%M:%S')}",
            font=("Arial", 10),
            bg="#2b2b2b",
            fg="#888888"
        )
        self.info.pack(pady=10)
        
        self.expresion = ""
        self.actualizar_hora()
    
    def presionar_boton(self, valor):
        contenido = self.pantalla.get()
        
        if valor == "=":
            try:
                resultado = eval(self.expresion)
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                messagebox.showerror("Error", "Operación inválida")
                self.limpiar()
        else:
            if contenido == "0":
                self.pantalla.delete(0, tk.END)
            
            self.pantalla.insert(tk.END, valor)
            self.expresion += valor
    
    def limpiar(self):
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, "0")
        self.expresion = ""
    
    def actualizar_hora(self):
        self.info.config(text=f"Hora: {datetime.now().strftime('%H:%M:%S')}")
        self.root.after(1000, self.actualizar_hora)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionVisual(root)
    root.mainloop()
