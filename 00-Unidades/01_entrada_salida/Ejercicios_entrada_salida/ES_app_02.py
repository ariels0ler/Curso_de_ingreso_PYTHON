import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

#Enunciado clase de sábado
"""para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos"""  

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        #nombre_alumno = prompt("Ingreso de dato", "Nombre")
        #alert("Mensaje", nombre_alumno)
    def btn_mostrar_on_click(self):
        
        pasajero_uno_nombre = prompt("Mensaje","Pasajero uno. Ingrese su nombre")
        pasajero_uno_edad = int(prompt("Mensaje","Pasajero uno. Ingrese su edad"))
        pasajero_uno_peso = int(prompt("Mensaje","Pasajero uno. Ingrese su peso"))

        pasajero_dos_nombre = prompt("Mensaje","Pasajero dos. Ingrese su nombre")
        pasajero_dos_edad = int(prompt("Mensaje","Pasajero dos. Ingrese su edad"))
        pasajero_dos_peso = int(prompt("Mensaje","Pasajero dos. Ingrese su peso"))

        peso_suma = pasajero_uno_peso + pasajero_dos_peso
        costo_viaje = peso_suma * 1000
        
        promedio_edad = (pasajero_uno_edad + pasajero_dos_edad) / 2

        mensaje = (f"Hola {pasajero_uno_nombre} y {pasajero_dos_nombre}, sus pesos son {pasajero_uno_peso}kg y {pasajero_dos_peso}kg respectivamente."
                    f"Sumados da {peso_suma}kg. El promedio de edad es {promedio_edad} y su viaje cuesta {costo_viaje}$")

        alert("Mensaje",mensaje)





        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()