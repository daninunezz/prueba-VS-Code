def calculadora_de_impuestos():
    precio_sin_impuestos=float(input("Introduce el precio inicial del producto:"))
    xcentaje_impuestos=float(input("Introduce el impuesto que desea aplicar:"))
    xcentaje_impuestosok=xcentaje_impuestos*0.01
    precio_impuesto=precio_sin_impuestos*xcentaje_impuestosok
    precio_final=precio_sin_impuestos+precio_impuesto
    print(f"El precio final es {precio_final}€")

x=True
while x==True:
    calculadora_de_impuestos()
    continuar=int(input("¿Desea probar con otros datos?\n1=Sí\n2=No\n"))
    if continuar==1:
        x=True
    elif continuar==2:
        x=False
    else:
        while continuar!= 1 and continuar!=2:
            print("Valor inválido, prueba otro")
            continuar=int(input("¿Desea probar con otros datos?\n1=Sí\n2=No\n"))
            if continuar==2:
                x=False