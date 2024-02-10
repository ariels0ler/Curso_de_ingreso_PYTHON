import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ariel
apellido: Soler
tutor: Mauro
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        #alert("E,S_01", "Esto no anda, funciona")
    def btn_mostrar_on_click(self):
        dolar_oficial = float(prompt("oficial","cantidad"))
        dolar_blue = float(prompt("blue","cantidad"))

        resta = dolar_oficial - dolar_blue
        porcentaje = resta / -(dolar_oficial)

        porcentaje_multiplicado = porcentaje * 100
        porcenta_redondeado = round(porcentaje_multiplicado)     
        
        alert("La diferencia es",f"La diferencia es de {porcenta_redondeado}%")
        
        
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
