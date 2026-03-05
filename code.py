# Ingresar cuantos estudiantes quiere ingresar, por cada estudiante, nombre y 3 notas, calcular promedio de notas de cada estudiante y decir si aprobo o reprobó, de 0 a 5, con 3 se aprueba, cuantos aprueban y promedio total

reprobados = 0
aprobados = 0
sumpromedio = 0

while True:
    try:
        entrada = int(input("¿Cuantos estudiantes desea ingresar al sistema?: "))
        break
    except ValueError:
        print("El valor no es valido")

for i in range(entrada):
    
    nombres = input("Ingrese el nombre del estudiante: ")

    while True:
        try:
            nota1 = float(input("Digite la 1ra nota del estudiante: "))
            if 1 <= nota1 <= 5:
                break
            else:
                print ("Ingrese una nota valida 1-5")
        except ValueError:
            print("El valor no es valido")
        
    while True:
        try:        
            nota2 = float(input("Digite la 2da nota del estudiante: "))
            if 1 <= nota2 <= 5:
                break
            else:  
                print("Ingresa una nota valida 1-5")
        except ValueError:
            print("El valor no es valido")
    
    while True:
        try:      
            nota3 = float(input("Digite la 3ra nota del estudiante: "))
            if 1 <= nota3 <= 5:
                break
            else:
                print("Ingrese una nota valida 1-5")
        except ValueError:
            print("Ingrese un valor valido")

    prom = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de {nombres}, es de {prom}")
    
    if prom >= 3:
        aprobados += 1
        print("Aprobó")
    else:
        reprobados += 1
        print("Reprobó")

    sumpromedio += prom
promtotal = sumpromedio / entrada

print("----------")
print(f"La cantidad de aprobados es de {aprobados} ")
print(f"La cantidad de reprobados es de {reprobados} ")

print(f"El promedio total de los estudiantes es de {promtotal}")