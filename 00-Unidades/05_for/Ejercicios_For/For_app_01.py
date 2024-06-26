import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Ariel 
apellido: Soler
---
Ejercicio: for_01
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        for i in range(6):
            
            print(i)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    '''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''
"""# Deducir el orden de los procesos

        #Que va antes del while
        seguir = True
        contador_masculino_IOT_IA = 0
        contador_IOT = 0
        contador_IA = 0
        contador_RV_RA = 0 

        contador_femenino = 0
        contador_masculino = 0
        contador_otro = 0


            #Que va dentro de whhile
        while seguir == True:

            nombre = prompt("Nombre","Ingrese nombre")
            
            edad = prompt("Edad","Ingrese edad")
            edad = int(edad)
            while edad < 18:
                edad = prompt("Error","Reingrese edad")
                edad = int(edad)


            genero = prompt("Genero","Ingrese género")

            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error","Reingrese género")

            tecnologia = prompt("Tencnologia", "Ingrese tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tenologia = prompt("Error","Reingrese tenologia")
            

            if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad > 24 and edad < 51:
                contador_masculino_IOT_IA += 1
            
            # if tecnologia == "IA":
            #     contador_IA += 1
            # elif tecnologia == "IOT":
            #     contador_IOT += 1
            # else:
            #     contador_RV_RA += 1
            seguir = question("Seguir","¿Desea continuar?")

            match tecnologia:
                case "IA":
                    contador_IA += 1
                case "IOT":
                    contador_IOT += 1
                case "RV/RA":
                    contador_RV_RA += 1

            match genero:
                case "Femenino":
                    contador_femenino += 1
                case "Masculino":
                    contador_masculino += 1
                case "Otro":
                    contador_otro += 1
                
            
            
            #Que va fuera del while
            # 2) - Tecnología que mas se votó.
            
        if contador_IA > contador_IOT and contador_IA > contador_RV_RA:
            tecnologia_mas_votada = "IA"
        elif contador_IOT > contador_RV_RA:
            tecnologia_mas_votada = "IOT"
        else:
            tecnologia_mas_votada = "RV/RA"

        total_empleados = contador_otro + contador_femenino + contador_masculino

        porcentaje_masculinos = (contador_masculino * 100) / total_empleados
        porcentaje_femeninos = (contador_femenino * 100) / total_empleados
        Porcentaje_otro = (contador_otro * 100) / total_empleados
        pocentaje_otro = 100 - (porcentaje_femeninos + porcentaje_masculinos)
        
        
        
        

        
        print(nombre,edad,genero,tecnologia,contador_masculino_IOT_IA)"""