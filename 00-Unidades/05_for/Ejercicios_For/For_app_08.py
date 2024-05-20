import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ariel
apellido: Soler
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        contador_primos = 0
        flag = False

        #pedir un número
        numero = input("Ingrese un número")
        numero = int(numero)

        for i in range(2,numero):
            flag = False
            for j in range(2,i):
                
                if i % j == 0:
                    flag = True
                    break
            
            if flag == False:
                contador_primos += 1
                print(f"El numero {i} es primo")
            else:
                print(f"El número {i} no es primo")
        print(f"La cantidad {contador_primos}")







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()