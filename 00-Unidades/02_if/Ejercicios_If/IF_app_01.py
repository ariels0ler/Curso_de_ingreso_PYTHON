import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ariel
apellido: Soler
---
Ejercicio: if_01
---
Enunciado:
Al presionar el botón 'Mostrar', se deberá obtener el contenido de la caja de texto txt_edad,
transformarlo en número,
 si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

#Mejor solución con "esle". Se evitan procesos inncesarios. EN REALIDAD NO APLICA ACÁ, SINO EN EL EJERCICIO 3. Pero ya lo hice.

        edad = int(self.txt_edad.get())
        """if edad > 17:
            alert("Mensaje", f"Usted tiene {edad} años de edad")
            alert("Mensaje", "Gracias por brindarme tus datos, ahora puedeo venderte más y mejor")
            alert("Mensaje", "Fin del programa")
        else: alert("Mensaje","Este programa es exlusivo para diesiochoañeros, adios")"""


#Ejemplo del true/false en consola
        """edad = int(self.txt_edad.get()) #Ejemplo del true/false en consola
        print(edad == 18)"""

#Ejemplo sin usar el condicional "else"
#En este ejemplo se usan demasiadas alerts, hay que crear una variable con el mensaje
        if edad > 17:
            alert("Mensaje", f"Usted tiene {edad} años de edad")
            alert("Mensaje", "Gracias por brindarme tus datos, ahora puedeo venderte más y mejor")
            alert("Mensaje", "Fin del programa")
        if edad < 18:
            alert("Mensaje","Este programa es exlusivo para diesiochoañeros, adios")


        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()