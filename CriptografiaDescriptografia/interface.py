import tkinter as tk
from tkinter import ttk
from criptografia import Criptografia

class InterfaceCriptografia:
    def __init__(self, root):
        self.root = root
        self.root.title("Criptografia e Descriptografia")
        self.root.geometry("425x400")
        self.criptografia = Criptografia()
        
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', padding=5)
        
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(main_frame, text="Digite a mensagem:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entrada_texto = tk.Text(main_frame, height=4, width=50)
        self.entrada_texto.grid(row=1, column=0, columnspan=2, pady=5)
        
        ttk.Button(main_frame, text="Criptografar", command=self.criptografar).grid(row=2, column=0, pady=10)
        ttk.Button(main_frame, text="Descriptografar", command=self.descriptografar).grid(row=2, column=1, pady=10)
        
        ttk.Label(main_frame, text="Resultado:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.resultado_texto = tk.Text(main_frame, height=4, width=50, state='disabled')
        self.resultado_texto.grid(row=4, column=0, columnspan=2, pady=5)
        
        ttk.Button(main_frame, text="Limpar", command=self.limpar).grid(row=5, column=0, columnspan=2, pady=10)
        
    def criptografar(self):
        mensagem = self.entrada_texto.get("1.0", tk.END).strip()
        resultado = self.criptografia.criptografar(mensagem)
        self.mostrar_resultado(resultado)
        
    def descriptografar(self):
        mensagem = self.entrada_texto.get("1.0", tk.END).strip()
        resultado = self.criptografia.descriptografar(mensagem)
        self.mostrar_resultado(resultado)
        
    def mostrar_resultado(self, texto):
        self.resultado_texto.config(state='normal')
        self.resultado_texto.delete("1.0", tk.END)
        self.resultado_texto.insert("1.0", texto)
        self.resultado_texto.config(state='disabled')
        
    def limpar(self):
        self.entrada_texto.delete("1.0", tk.END)
        self.resultado_texto.config(state='normal')
        self.resultado_texto.delete("1.0", tk.END)
        self.resultado_texto.config(state='disabled')

def main():
    root = tk.Tk()
    app = InterfaceCriptografia(root)
    root.mainloop()

if __name__ == "__main__":
    main() 