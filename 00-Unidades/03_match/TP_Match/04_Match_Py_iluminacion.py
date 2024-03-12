import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ariel
apellido: Soler
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        
        precio = 800
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad)
        

        match cantidad:
            case  10 | 11 | 12:
                precio_cantidad = precio * cantidad
                precio_sin_descuento =  precio_cantidad - (precio_cantidad * 0.50)
                precio_final =  precio_sin_descuento - (precio_sin_descuento * 0.05)
            case 6 | 7 | 8 | 9:
                precio_cantidad = precio * cantidad
                precio_final = (precio * cantidad) - (precio * 0.50)
            case 5:
                match marca:
                    case "ArgentinaLuz":
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.40)
                    case _:
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.30)
            case 4:
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.25)
                    case _:
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.20)
            case 3:
                match marca:
                    case "ArgentinaLuz":
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.15)
                    case "FelipeLamparas":
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.10)
                    case _:
                        precio_cantidad = precio * cantidad
                        precio_final = precio_cantidad - (precio_cantidad * 0.5)
            case _:
                precio_final = precio * cantidad
        
        
        
        # precio_final = precio * cantidad
        # precio_final_descuento = precio_final - (precio_final * descuento)
        print(precio_final)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()