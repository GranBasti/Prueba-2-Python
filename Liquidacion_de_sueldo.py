#Programa de Python de Liquidación de sueldo
# de los trabajadores de una empresa
"""""
********
Funcion While True para validar 
carácteres de máximo 30 para el nombre del trabajador
********
"""""
while True:
    try:
        nombre_trabajador = input("Ingrese nombre del trabajador: ")
        if not nombre_trabajador.isspace() and 1 <= len(nombre_trabajador) <= 30:
            break
        else:
            print("Error: Ingresa un nombre real.")
    except ValueError:
        print("Error: Ingresa un valor válido.")

print(f"¡Excelente! Ingresaste el nombre {nombre_trabajador}.")

while True:
    try:
        sueldo_base_trb = int(input("Ingrese sueldo del trabajador: "))
        if sueldo_base_trb > 0:
            break
        else:
            print("Error: Ingresa un valor positivo.")
    except ValueError:
        print("Error: Ingresa un valor válido.")

print(f"¡Excelente! Ingresaste el sueldo base {sueldo_base_trb}.")

while True:
    try:
        horas_extras_trb = int(input("Ingrese N° de horas extras trabajadas al mes: "))
        if horas_extras_trb > 0:
            break
        else:
            print("Error: Ingresa un valor positivo.")
    except ValueError:
        print("Error: Ingresa un valor válido.")

print(f"¡Excelente! Ingresaste el N° de horas extras {horas_extras_trb}.")

"""""
********
TERMINO WHILE TRUES
********
"""""

#Cálculo de liquidación

#Cálculo valor horas extras

valor_hr_normal = (sueldo_base_trb/30)/8
print ("el valor de la hora normal es: ", valor_hr_normal)
valor_hora_extra = (valor_hr_normal*1.5)
print ("el valor de la hora extra es: ", valor_hora_extra)

pago_horas_extras = valor_hora_extra * horas_extras_trb

#Cálculo ingreso sueldo base + horas extras

sueldobase_horasextras = (horas_extras_trb*valor_hora_extra) + sueldo_base_trb
print ("el monto de su sueldo más horas extras asciende a: ", sueldobase_horasextras)

#Cálculo descuento Fonasa

dscto_fonasa = (sueldobase_horasextras*0.07)
print ("el descuento (7%) de fonasa es: ", dscto_fonasa)

#Cálculo descuento AFP

dscto_afp = (sueldobase_horasextras*0.1)
print ("el descuento (10%) de afp es: ", dscto_afp)

dscto_seguridadsocial = dscto_afp + dscto_fonasa

#Cálculo sueldo neto a pagar

sueldo_neto = sueldobase_horasextras - dscto_afp - dscto_fonasa
print ("el sueldo neto es: ", sueldo_neto)

diccionario_trabajador = {
    "Nombre del trabajador": nombre_trabajador,  
    "Sueldo base": sueldo_base_trb, 
    "Pago por horas extras": pago_horas_extras, 
    "Ingresos totales": sueldobase_horasextras, 
    "Descuento por seguridad social": dscto_seguridadsocial, 
    "Sueldo neto a pagar": sueldo_neto}

for clave, valor in diccionario_trabajador.items():
    print(f"{clave}: {valor}")

diccionario_trabajador = {
    "Nombre del trabajador": nombre_trabajador,
    "Sueldo base": sueldo_base_trb,
    "Pago por horas extras": pago_horas_extras,
    "Ingresos totales": sueldobase_horasextras,
    "Descuento por seguridad social": dscto_seguridadsocial,
    "Sueldo neto a pagar": sueldo_neto
}

for clave, valor in diccionario_trabajador.items():
    print(f"{clave}: {valor}")

with open("Datos liquidacion.txt", "w") as archivo:
    archivo.write(str(diccionario_trabajador))