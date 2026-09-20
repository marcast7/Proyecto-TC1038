print("─────────███──────────███")
print("────────█▓▓▓█────────█▓▓▓█")
print("───────█▓▓▓▓██████████▓▓▓▓█")
print("───────█▓▓▓██▒▒▒▒▒▒▒▒██▓▓▓█")
print("────────████▒▒▒▒▒▒▒▒▒▒████")
print("──────────█▒▒▒██▒▒██▒▒▒█")
print("──────────█▒▒▒▒▒▒▒▒▒▒▒▒█")
print("──────────█▒▒▒▒░██░▒▒▒▒█")
print("──────────██▒▒▓▒▒▒▒▓▒▒██")
print("───────────██▒▒▓▓▓▓▒▒██")
print("────────────█▒▒▒▒▒▒▒▒█")
print("─────████████████████████████")
print("───▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓")
print("──▓▓▒▒▓▒░░░░░░░░░░░░░░░░░░▒▓▒▒▓▓")
print("──▓▒▒▒▓░░*♥ Foráneo Finanzas! ♥*▓")
print("──▓▓▒▒▓▒▒░░░░░░░░░░░░░░░░▒▒▓▒▒▓▓")
print("───▓▓▒▓▒▒░░░░░░░░░░░░░░░░▒▒▓▒▓▓")
print("─────████████████████████████")
print("─────────█▒▒▓▓▓▓▓▓▓▓▓▒▒█")
print("────────██▒▒▓▓▓▓▓▓▓▓▓▒▒██")
print("───────█▓▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▓█")
print("─███▄─█▒▒▓▒▒▒▓▓▓▓▓▓▓▒▒▒▓▒▒█─▄███")
print("█▓▓▓██▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒██▓▓▓█")
print("█▓▓▓▓█▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒█▓▓▓▓█")
print("█▓▓▓▓██▒▒▒▒▓█████████▓▒▒▒▒██▓▓▓▓█")
print("█▓▓▓▓▓█▒▒▒█▓─────────▓█▒▒▒█▓▓▓▓▓█")
print("─█▓▓▓▓█▒██▓───────────▓██▒█▓▓▓▓█")
print("──█▓▓▓██▓▓─────────────▓███▓▓▓█")
print("───████▓────────────────▓█████")


# Esta función muestra el menú y permite elegir qué hacer y registrar los datos
def menu(): 
    
    # Empiezo en 0 para que el menú pueda comenzar
    opcion=0
    
    # Empieza en False porque todavía no he registrado mis datos
    datos_guardados = False
    
    # El menú se va a repetir hasta que elija la opción 3
    while opcion !=3:
        print("--- MENU DE FINANZAS ---")
        print("1. Registrar gastos")
        print("2. Ver reporte financiero")
        print("3. Salir")
        
        # Aquí el usuario elige una opción del menú
        opcion= int(input("Elige una opcion: "))
            
        # Dependiendo de la opción elegida se realiza una acción
        match opcion:
            
            # Opción 1: registrar todos los datos de gastos
            case 1:
                ingresos= int(input("Ingresos mensuales:$ "))
                renta= int(input("Renta:$ "))
                comida=int(input("Comida:$ "))
                transporte= int(input("Transporte:$ "))
                escuela= int(input("Escuela:$ "))
                entretenimiento=int(input("Entretenimiento:$ "))
                otros=int(input("Otros gatos:$ "))
                dias=int(input("Dias faltantes para que el mes termine: "))
                
                # Cambio a True porque ya se registraron los datos
                datos_guardados = True
                
                print("Datos guardados correctamente")
                
            # Opción 2: mostrar el reporte de las finanzas
            case 2:
                
                # Si todavía no hay datos, primero debe registrarlos
                if datos_guardados == False:
                    print("Primero debes registrar tus datos.")
                
                # Si ya hay datos, se hacen los cálculos
                else:
                    ingreso_mensual=ingresos
                    
                    # Llamo a la función calcular_gastos para sumar todos los gastos
                    gastos=calcular_gastos(renta, comida, transporte, escuela, entretenimiento, otros)
                    
                    # Calculo cuánto dinero queda después de pagar los gastos
                    restante=ingreso_mensual-gastos
                    
                    # Calculo cuánto dinero puedo gastar aproximadamente por día
                    diario=restante/dias
                    
                    # Calculo qué porcentaje de mis ingresos ya gasté
                    porcentaje=gastos*100/ingresos
                    
                    # Aquí muestro el reporte financiero
                    print()
                    print("----- REGISTRO DE DATOS -----")
                    print("Ingresos mensuales:$ ", ingresos)
                    print("Total de gastos:$ ", gastos)
                    print("Dinero restante:$ ", restante)
                    print("Gasto diario disponible:$ ", diario)
                    print("Porcentaje gastado:% ", porcentaje)
                
                    # Reviso si gasté más dinero del que tenía
                    if gastos>ingresos:
                        print("Alerta! Tus gastos son mayores que tu ingreso!. Administra mejor tu dinero.")
                        
                    # Si gasté 80% o más, muestro una advertencia
                    elif porcentaje>=80: 
                        print("Precaución! Has usado más del 80% de tus ingresos.")
                    
                    # Si no pasa ninguna de las anteriores, significa que voy bien
                    else:
                        print("Felicidades!, sigue manteniendo un buen control de tus gastos.")
    
            # Opción 3: terminar el programa
            case 3:
                print("Hasta pronto!")
                break
            
            # Si escribe algo diferente a las opciones del menú
            case _:
                print("Opcion no valida")


# Esta función suma todos los gastos registrados
def calcular_gastos(renta, comida, transporte, escuela, entretenimiento, otros):
    
    # Sumo cada uno de los gastos
    gastos = renta + comida + transporte + escuela + entretenimiento + otros
    
    # Regreso el resultado para poder usarlo en el reporte
    return gastos

def generar_dashboard():
    # Pendiente: generar el dashboard financiero
    # utilizando los datos registrados y procesados.
    print("Aqui se generara el dashboard financiero con graficas de los gastos por categoria.")


# Esta es la función principal del programa
def main():
    
    # Llamo a la función del menú para iniciar el programa
    menu()


# Aquí comienza a ejecutarse el programa
main()
