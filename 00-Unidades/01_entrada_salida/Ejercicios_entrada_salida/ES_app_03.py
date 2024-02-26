import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar: 

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

El promedio de edad de las votantes de género Femenino 

Del votante más viejo, su nombre.

Nombre del votante más joven qué votó a Gianni.

Nombre de cada participante y porcentaje de los votos qué recibió.

El nombre del participante que debe dejar la casa (El que tiene más votos)"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        seguir = True 
        acumulador_edad_votantantes_femeninas = 0

        while seguir == True:
            nombre = input("Ingrese su Nombre")

            edad = input("Ingrese su edad")
            edad = int(edad)
            while edad < 18:
                edad = input("Error. Reingrese su edad")
                edad = int(edad)

            genero = input("Ingrese su género")
            if genero == "Femenino":
                acumulador_edad_votantantes_femeninas = acumulador_edad_votantantes_femeninas + edad

            participante_voto_negativo = input("Ingrese al participante que quiera darle el voto negativo")
            while participante_voto_negativo != "Giovanni" and participante_voto_negativo != "Gianni" and participante_voto_negativo != "Esteban":
                participante_voto_negativo = input("Error. Reingrese su voto")
            
            
            
                

                



        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

"""PASOS PARA LA RESOLUCIÓN DE EJERCICIOS ORDENADA:

-Inicializaciones(fuera del while/for)
-Validaciones(validamos con while si el dato ingresado cumple/es valido con lo pedido, no se programa nada más adentro que los datos a validar!!)
-Incremento de variables(fuera de las validaciones de while,  pero dentro del "while mayor" pongo los incrementos)
-Resolución de problematicas (promedio/porcentajes, etc. Fuera del while)
-Mostar mensaje al final"""