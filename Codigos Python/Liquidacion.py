def calcular_sueldo_bruto(horas_trabajadas, tarifa_hora, horas_extras=0, tarifa_extra=0):
    sueldo_normal = horas_trabajadas * tarifa_hora
    sueldo_extras = horas_extras * tarifa_extra
    return sueldo_normal, sueldo_extras

def calcular_descuento_afp(sueldo_bruto):
    return sueldo_bruto * 0.1

def calcular_descuento_fonasa(sueldo_bruto):
    return sueldo_bruto * 0.07

def calcular_sueldo_neto(sueldo_bruto, descuento_afp, descuento_fonasa):
    return sueldo_bruto - descuento_afp - descuento_fonasa

def obtener_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def verificar_longitud_nombre(nombre):
    if len(nombre) > 30:
        return False
    else:
        return True

def inicio():
    while True:
        while True:
            nombre = input("Ingrese el nombre del empleado: ")
            if verificar_longitud_nombre(nombre):
                break
            else:
                print("Ingrese un nombre que no supere los 30 caracteres.")
        
        horas_trabajadas = obtener_float("Ingrese la cantidad de horas trabajadas: ")
        tarifa_hora = obtener_float("Ingrese la tarifa por hora: ")
        horas_extras = obtener_float("Ingrese la cantidad de horas extras trabajadas: ")
        
        tarifa_extra = tarifa_hora * 1.5

        sueldo_normal, sueldo_extras = calcular_sueldo_bruto(horas_trabajadas, tarifa_hora, horas_extras, tarifa_extra)
        sueldo_bruto = sueldo_normal + sueldo_extras
        descuento_afp = calcular_descuento_afp(sueldo_bruto)
        descuento_fonasa = calcular_descuento_fonasa(sueldo_bruto)
        sueldo_neto = calcular_sueldo_neto(sueldo_bruto, descuento_afp, descuento_fonasa)

        sueldo_normal = int(sueldo_normal)
        sueldo_extras = int(sueldo_extras)
        sueldo_bruto = int(sueldo_bruto)
        descuento_afp = int(descuento_afp)
        descuento_fonasa = int(descuento_fonasa)
        sueldo_neto = int(sueldo_neto)

        with open("liquidacion_de_sueldo.txt", "w") as archivo:
            archivo.write("Liquidación de Sueldo\n")
            archivo.write(f"  {nombre}\n")
            archivo.write("======================\n")
            archivo.write(f"Sueldo Bruto: ${sueldo_bruto}\n")
            archivo.write(f"Sueldo Normal: ${sueldo_normal}\n")
            archivo.write(f"Ganancia por Horas Extras: ${sueldo_extras}\n")
            archivo.write(f"Descuento AFP: ${descuento_afp}\n")
            archivo.write(f"Descuento FONASA: ${descuento_fonasa}\n")
            archivo.write("======================\n")
            archivo.write(f"Sueldo Neto: ${sueldo_neto}\n")

        print("Los datos de la liquidación de sueldo se han guardado en el archivo 'liquidacion_de_sueldo.txt'.")

        break

inicio()

 