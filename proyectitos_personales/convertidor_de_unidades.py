def C_a_K():
    Celsius=float(input("Introduce la temperatura en celcius: "))
    resultado=Celsius+273.15
    resultado=round(resultado,2)
    print(f"{Celsius} grados celsius son {resultado} grados kelvin")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           C_a_K()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
    
def K_a_C():
    Kelvin=float(input("Introduce la temperatura en kelvin: "))
    
    resultado= Kelvin-273.15
    resultado=round(resultado,2)
    print(f"{Kelvin} grados kelvin son {resultado} grados celsius")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           K_a_C()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
           
def C_a_F():
    Celsius=float(input("Introduce la temperatura en celcius: "))
    resultado= Celsius*9/5+32
    resultado=round(resultado,2)
    print(f"{Celsius} grados celsius son {resultado} grados farenheit")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           C_a_F()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
           
def F_a_C():
    Farenheit=float(input("Introduce la temperatura en farenheit: "))
    resultado= (Farenheit-32)*5/9
    resultado=round(resultado,2)
    print(f"{Farenheit} grados farenheit son {resultado} grados celsius")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           F_a_C()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
    
def K_a_F():
    Kelvin=float(input("Introduce la temperatura en kelvin: "))
    resultado=(Kelvin-273.15)*9/5+32
    resultado=round(resultado,2)
    print(f"{Kelvin} grados kelvin son {resultado} grados farenheit")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           K_a_F()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
    
def F_a_K():
    Farenheit=float(input("Introduce la temperatura en farenheit: "))
    resultado= (Farenheit-32)*5/9+273.15
    resultado=round(resultado,2)
    print(f"{Farenheit} grados farenheit son {resultado} grados kelvin")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           F_a_K()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
           
def Km_a_M():
    Km=float(input("Introduce la distancia en Km: "))
    resultado= Km/1.609
    resultado=round(resultado,2)
    print(f"{Km}Km son {resultado} millas")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           Km_a_M()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
    
def M_a_Km():
    Millas=float(input("Introduce la distancia en millas: "))
    resultado= Millas*1.609
    resultado=round(resultado,2)
    print(f"{Millas} millas son {resultado}Km")
    bucle=True
    while bucle==True:
       otroo=input("¿Quieres hacer otra conversión con las mismas unidades de medida? si/no: ")
       otro=otroo.lower()
       if otro=="si":
           bucle=False
           M_a_Km()
       elif otro=="no":
           bucle=False
           bucle2=True
           while bucle2==True:
              otroo2=input("¿Quieres hacer otra con otras unidades de medida? si/no: ")
              otro2=otroo2.lower()
              if otro2=="si":
                  bucle2=False
                  conjunto()
              elif otro2=="no":
                  print("¡Hasta luego!")
                  break
              else:
               print("Opción inváilda")
       else:
           print("Opción inválida")
           
def conjunto():
   Opcion=int(input("¿Qué unidad quieres convertir?\nCelsius a Kelvin(1)\nKelvin a Celsius(2)\nCelsius a Farenheit(3)\nFarenheit a Celsius(4)\nKelvin a Farenheit(5)\nFarenheit a Kelvin(6)\nKilómetros a Millas(7)\nMillas a Kilómetros(8)\n"))
   if Opcion==1:
       C_a_K()

   if Opcion==2:
       K_a_C()

   if Opcion==3:
       C_a_F()
    
   if Opcion==4:
       F_a_C()
    
   if Opcion==5:
       K_a_F()

   if Opcion==6:
       F_a_K()
   
   if Opcion==7:
       Km_a_M()

   if Opcion==8:
       M_a_Km()    
conjunto()
