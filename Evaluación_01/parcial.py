import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

# Enunciado:
# De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
# Nombre
# Tipo (gato ,perro o exotico)
# Peso ( entre 10 y 80)
# Sexo( F o M )
# Edad(mayor a 0)
# Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál fue el sexo mas ingresado (F o M)
# Informe B- El porcentaje de mascotas que hay por tipo (gato ,perro o exotico)
# Informe C- El nombre de la mascota más pesada
# Informe D- El sexo y nombre del gato más viejo
# Informe E- El promedio de edad de todas las mascotas

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
        

        #Antes del while

        contador_femenino = 0
        contador_masculino = 0 

        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0

        mascota_mayor_peso = 0
        gato_mayor_edad = 0
        
        acumulador_edad = 0
        contador_edad = 0

        continuar = 0
        
            #Dentro del while

        
        while continuar < 5:

            nombre = input("Ingrese el nombre de la mascota")
            
            tipo = input("Ingrese el tipo de mascota")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = input("Reingrese el tipo de mascota")

            peso = input("Ingrese el peso de la mascota")
            peso = int(peso)
            while peso < 10 or peso > 80:
                peso = input("Rengrese el peso de la mascota")
                peso = int(peso)
            
            sexo = input("Ingrese el sexo de la mascota")
            while sexo != "F" and sexo != "M":
                sexo = input("Ingrese el sexo de la mascota")


            edad = input("Ingrese la edad de la mascota")
            edad = int(edad)
            while edad < 1:
                edad = input("Reingrese la edad de la mascota")
                edad = int(edad)


            # A- Cuál fue el sexo mas ingresado (F o M)
            match sexo:
                case "F":
                    contador_femenino += 1
                case "M":
                    contador_masculino += 1
            
            
            # B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
            match tipo:
                case "gato":
                    contador_gato += 1
                #  D- El sexo y nombre del gato más viejo
                    if edad > gato_mayor_edad:
                        gato_mayor_edad = edad
                        sexo_gato_mayor = sexo
                        nombre_gato_mayor = nombre

                    
                case "perro":
                    contador_perro += 1
                case "exotico":
                    contador_exotico += 1
            
            
            # C- El nombre de la mascota más pesada
            if peso > mascota_mayor_peso:
                mascota_mayor_peso = peso
                nombre_mascota_mayor_peso = nombre
                
            # E- El promedio de edad de todas las mascotas

            acumulador_edad += edad
            
            
            
            
            
            
            
            
            
            #Rotura del bucle
            continuar += 1 



        #Fuera del While

        # A- Cuál fue el sexo mas ingresado (F o M)

        if contador_masculino > contador_femenino:
            sexo_mas_ingresado = "Masculino"
        else:
            sexo_mas_ingresado = "Femenino"


        # B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
        
        total_mascotas = contador_gato + contador_perro + contador_exotico
        porcentaje_gato = (contador_gato * 100) / total_mascotas
        porcentaje_perro = (contador_perro * 100) / total_mascotas
        porcentaje_exotico = (contador_exotico * 100) / total_mascotas

        # E- El promedio de edad de todas las mascotas
        promedio_edad_mascotas = acumulador_edad / 5


        print(f"A=\n\tEl sexo más es el {sexo_mas_ingresado}")
        print(f"B=\n\tEl porcentaje de gatos es {porcentaje_gato}\n\tEl porcentaje de perros es {porcentaje_perro}\n\tEl porcentaje exoticos es {porcentaje_exotico}")
        print(f"La mascota más pesada se llama {nombre_mascota_mayor_peso}")
        print(f"El gato más viejo es de sexo '{sexo_gato_mayor}' y se llama {nombre_gato_mayor}")
        print(f"Promedio de edad{promedio_edad_mascotas}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()