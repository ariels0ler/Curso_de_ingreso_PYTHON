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

        
        
        # El promedio de edad de las votantes de género Femenino 
        #Del votante más viejo, su nombre.
        # Nombre del votante más joven qué votó a Gianni.
        # Nombre de cada participante y porcentaje de los votos qué recibió.
        # El nombre del participante que debe dejar la casa (El que tiene más votos)

    def btn_mostrar_on_click(self):
        
        #Antes del while
        contador_femenino = 0
        acumulador_edad_femenino = 0

        votante_mas_viejo = 0
        votante_mas_joven = 0

        nombre_votante_mas_viejo = ""
        nombre_votante_gianni = ""
        flag_votante_viejo = True

        # contador_giovanni = 0
        # contador_gianni = 0
        # contador_esteban = 0
        
        acumulador_giovanni = 0
        acumulador_gianni = 0
        acumulador_esteban = 0 

        seguir = True

        
        

        

        #Dentro del while
        while seguir == True:
            
            
            nombre_votante = input("Ingrese su nombre")

            edad_votante = input("Ingrese su edad")
            edad_votante = int(edad_votante)
            while edad_votante < 14:
                edad_votante = input("Reingrese su edad")
                edad_votante = int(edad_votante)

            genero_votante = input("Ingrese su género")
            while genero_votante != "Masculino" and genero_votante != "Femenino" and genero_votante != "Otro":
                genero_votante = input("Reingrese su género")
            

            nombre_participante = input("Ingrese el nombre del participante que quiere votar")
            while nombre_participante != "Giovanni" and nombre_participante != "Gianni" and nombre_participante != "Esteban":
                nombre_participante = input("Ringrese su voto")

            
            # El promedio de edad de las votantes de género Femenino 
            if genero_votante == "Femenino":
                acumulador_edad_femenino += edad_votante
                contador_femenino += 1

            #Del votante más viejo, su nombre.
            if edad_votante > votante_mas_viejo or flag_votante_viejo == True:
                votante_mas_viejo = edad_votante
                nombre_votante_mas_viejo = nombre_votante
            
            if edad_votante < votante_mas_joven or flag_votante_viejo == True:
                votante_mas_joven = edad_votante
                flag_votante_viejo = False
                    
                
            # Nombre del votante más joven qué votó a Gianni.
            if nombre_participante == "Gianni":
                nombre_votante_gianni = nombre_votante
            else:
                nombre_votante_gianni = "(Nadie votó por Gianni)"
                

            # Nombre de cada participante y porcentaje de los votos qué recibió.
            match nombre_participante:
                case "Giovanni":
                    acumulador_giovanni += 1
                    
                case "Gianni":
                    acumulador_gianni += 1
                    
                case "Esteban":
                    acumulador_esteban += 1

                

            
            
            
            
            seguir = question("Mensaje","¿Desea continuar?")

            #Después del while

            # El promedio de edad de las votantes de género Femenino 
        if acumulador_edad_femenino != 0:
            promedio_votantes_femenino = edad_votante / contador_femenino
        else:
            promedio_votantes_femenino = "(No se ingresaron votos femeninos)"

        # porcentaje de los votos qué recibió.
        total_votos = acumulador_giovanni + acumulador_gianni + acumulador_esteban
            
        total_votos_giovanni = (acumulador_giovanni * 100) / total_votos
        total_votos_gianni = (acumulador_gianni * 100) / total_votos
        total_votos_esteban = (acumulador_esteban * 100) / total_votos

        # El nombre del participante que debe dejar la casa (El que tiene más votos)
        if total_votos_giovanni > total_votos_gianni and total_votos_giovanni > total_votos_esteban:
            participante_mas_votado = "Giovani"
        elif total_votos_gianni > total_votos_esteban:
            participante_mas_votado = "Gianni"
        else:
            participante_mas_votado = "Esteban"
        
#Me está fallando la parte del votante más jove
        print(f"1= El votante más viejo es {nombre_votante_mas_viejo}")
        print(f"2= El votante joven que votó por Gianni es {nombre_votante_gianni}")
        print(f"3= Promedio de votos femeninos: {promedio_votantes_femenino}")
        print(f"4= Giovanni {total_votos_giovanni}\n\tGianni {total_votos_gianni}\n\tEsteban {total_votos_esteban}")
        print(f"6= El participante que abandona la casa es {participante_mas_votado}")



# El promedio de edad de las votantes de género Femenino 
#Del votante más viejo, su nombre.
# Nombre del votante más joven qué votó a Gianni.
# Nombre de cada participante y porcentaje de los votos qué recibió.
# El nombre del participante que debe dejar la casa (El que tiene más votos)
        
        
        
        




    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()