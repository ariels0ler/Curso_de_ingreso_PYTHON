import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. Minimo numero y que sea positivo
    H. Maximo numero y que sea negativo
    I. Promedio de los negativos y Promedio de los positivos
    J. Cantidad de numeros ingresados

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        #Fuera del while
        #Declaramos acumuladore y contadores

        numero_maximo = 0
        numero_minimo = 0

        acumulador_positivos = 0 
        acumulador_negativos = 0

        contador_positivos = 0
        contador_negativos = 0 
        contador_ceros = 0

        flag = True
        
        #Bucle principal
        while True:
            
            numero = prompt("Mensaje","Ingrese un número")

            #Condición que rompe el bucle
            if numero == None or numero == "":
                break
            else:
                
                numero = int(numero)
                #Calcula el máximo
                if numero > numero_maximo or flag == True:
                        numero_maximo = numero
                #B. La suma acumulada de los positivos
                        if numero > 0:
                            acumulador_positivos += numero
                            #C. Cantidad de números positivos ingresados
                            contador_positivos += 1
                        

                if numero < numero_minimo or flag == True:
                        numero_minimo = numero
                        
                        #A. La suma acumulada de los negativos
                        if numero < 0:
                            acumulador_negativos += numero 
                            # D. Cantidad de números negativos ingresados
                            contador_negativos += 1

                # E. Cantidad de ceros 
                if numero == 0:
                    contador_ceros += 1
                flag = False
        #Fuera del While
        
        # J. Cantidad de numeros ingresados
        
        total_numeros_ingresados = contador_ceros + contador_negativos + contador_positivos
        
        # I. Promedio de los positivos y Promedio de los negativos
        if contador_positivos != 0:
            promedio_positivos = acumulador_positivos / contador_positivos
        else:
            promedio_positivos = "No se ingresaron números positivos"
        if contador_negativos != 0:
            promedio_negativos = acumulador_negativos / contador_negativos
        else:
            promedio_negativos = "No se ingresaron números negativos"
        
        #F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
        diferencia_positivos_negativos = acumulador_positivos - acumulador_negativos

        print(diferencia_positivos_negativos)

        


            

"""
if numero > 0:
    
"""


            


        

        
        


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

"""acumulador_positivos = 0
        acumulador_negativos = 0
        
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        
        bandera = True # Control de estado --> True ó False

        while bandera:
            numero = prompt("EJ 10", "Ingrese numero:")
            # numero = int(numero)

            # if numero != None and numero != "":
            #     numero = int(numero)
            # else:
            #     break

            # if numero == None or numero == "":
            #     break
            # numero = int(numero)
    
            if numero == None or numero == "":
                bandera = False
            else:
                numero = int(numero)

                if numero > 0:
                    acumulador_positivos += numero
                    contador_positivos += 1
                elif numero < 0:
                    acumulador_negativos += numero
                    contador_negativos += 1
                else:
                    contador_ceros += 1
            

            # if numero == None or numero == "":
            #     break
            # else:
            #     numero = int(numero)

            # if numero > 0:
            #     acumulador_positivos += numero
            #     contador_positivos += 1
            # elif numero < 0:
            #     acumulador_negativos += numero
            #     contador_negativos += 1
            # else:
            #     contador_ceros += 1
        
        #diferencia = acumulador_positivos + acumulador_negativos
        # diferencia = contador_positivos - contador_negativos
        
        # mensaje = f"Resultado \n la suma acumulada de los negativos es: {acumulador_negativos} \n la suma acumulada es de los positivos es: {acumulador_positivos} \n la diferencia: {diferencia} \n cantidad positivos: {contador_positivos} \n cantidad negativos: {contador_negativos} \n cantidad ceros: {contador_ceros}"
        # alert("EJ 10", mensaje) """