#Foráneo Finanzas - Avance 3
# Programa que registra los ingresos y gastos del mes de un estudiante foráneo,
# calcula cuánto le queda y muestra un dashboard con tabla y gráficas.
#
# Novedades respecto al Avance 2 (marcadas como NUEVO en el código):
# Los gastos se guardan en listas en lugar de variables sueltas.
#   Se usa una lista de listas para armar la tabla del desglose.
# 	Se procesan cadenas para dar formato al reporte y para buscar una
#   categoría por su nombre sin importar mayúsculas o minúsculas.
#   Se puede modificar un gasto ya registrado (nueva opción del menú).
#   generar_dashboard() ya está implementada (antes solo era un mensaje).
 
# Librería externa para dibujar las gráficas del dashboard.
import matplotlib.pyplot as plt
 
 
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
 
 
# Controla el flujo del programa: deja al usuario registrar sus datos, ver el
# reporte o salir, y reparte el trabajo entre las demás funciones.
def menu():
 
# NUEVO: lista con las categorías de gasto. Una sola lista sirve para
# tres cosas: saber qué datos pedir, nombrar las filas de la tabla y
# etiquetar las gráficas, así no se repiten los nombres en cada parte.
    categorias = ["Renta","Comida","Transporte","Escuela","Entretenimiento","Otros gastos"]
 
    # Valores iniciales para que existan aunque el usuario elija ver el
    # reporte antes de registrar datos.
    opcion = 0
    ingresos = 0
    gastos = []
    dias = 0
    datos_guardados = False
 
    # El menú se repite hasta que el usuario decida salir.
    while opcion != 4:
        print("--- MENU DE FINANZAS ---")
        print("1. Registrar gastos")
        print("2. Ver reporte financiero")
        print("3. Modificar un gasto")
        print("4. Salir")
 
        opcion = int(input("Elige una opcion: "))
 
        match opcion:
 
            # Opción 1: captura de datos del mes.
            case 1:
                ingresos = int(input("Ingresos mensuales:$ "))
 
                # Se vacía la lista para que un nuevo registro reemplace al
                # anterior en lugar de acumularse con él.
                gastos = []
 
                # NUEVO: se pide un gasto por cada categoría de la lista. Así
                # "gastos" queda en el mismo orden que "categorias", y la
                # posición de un dato corresponde a la posición de su nombre.
                for nombre in categorias:
                    gasto = int(input(nombre + ":$ "))
                    gastos.append(gasto)
 
                dias = int(input("Dias faltantes para que el mes termine: "))
                datos_guardados = True
                print("Datos guardados correctamente")
 
            # Opción 2: cálculos, reporte y dashboard.
            case 2:
 
                # Evita calcular con datos vacíos.
                if datos_guardados == False:
                    print("Primero debes registrar tus datos.")
 
                else:
                    total_gastos = calcular_gastos(gastos)
                    restante = ingresos - total_gastos
 
                    # Se evita dividir entre cero cuando ya no quedan días
                    # o cuando no se registraron ingresos.
                    if dias > 0:
                        diario = restante / dias
                    else:
                        diario = 0
 
                    if ingresos > 0:
                        porcentaje = total_gastos * 100 / ingresos
                    else:
                        porcentaje = 0
 
                    print()
                    print("----- REGISTRO DE DATOS -----")
                    print("Ingresos mensuales:$ ", ingresos)
                    print("Total de gastos:$ ", total_gastos)
                    print("Dinero restante:$ ", restante)
                    print("Gasto diario disponible:$ ", diario)
                    print("Porcentaje gastado:% ", porcentaje)
 
                    # Mensaje de alerta según qué tan comprometido está el
                    # ingreso: gasto mayor al ingreso, 80% o más, o va bien.
                    if total_gastos > ingresos:
                        print("Alerta! Tus gastos son mayores que tu ingreso!. Administra mejor tu dinero.")
                    elif porcentaje >= 80:
                        print("Precaución! Has usado más del 80% de tus ingresos.")
                    else:
                        print("Felicidades!, sigue manteniendo un buen control de tus gastos.")
 
                    # NUEVO: al terminar el reporte numérico se muestra el
                    # dashboard visual con los mismos datos.
                    generar_dashboard(categorias, gastos, ingresos, total_gastos, restante)
 
            # NUEVO - Opción 3: corregir un gasto sin tener que registrar todo
            # de nuevo. Solo se puede si ya hay datos guardados.
            case 3:
                if datos_guardados == False:
                    print("Primero debes registrar tus datos.")
                else:
                    modificar_gasto(categorias, gastos)
 
            # Opción 4: salir.
            case 4:
                print("Hasta pronto!")
                break
 
            # Cualquier otra entrada no corresponde a una opción del menú.
            case _:
                print("Opcion no valida")
 
 
# Obtiene el total gastado en el mes para usarlo en el reporte y en las
# alertas.
# NUEVO: antes recibía un parámetro por cada gasto yyahora recibe la lista
# completa, así no depende de cuántas categorías existan.
def calcular_gastos(gastos):
    total = 0
    for gasto in gastos:
        total = total + gasto
    return total
 
 
# NUEVO: permite corregir el gasto de una categoría sin volver a capturar
# todos los datos. El usuario escribe el nombre de la categoría y se busca
# en la lista "categorias"; la posición donde se encuentra es la misma que
# le corresponde en la lista "gastos", y ahí se guarda el monto nuevo.
# No necesita return porque las listas se modifican directamenteee
def modificar_gasto(categorias, gastos):
    nombre_buscado = input("Categoria a modificar: ")
 
    # Se pasa todo a minúsculas, tanto lo que escribe el usuario como los
    # nombres de la lista, para que "renta", "Renta" y "RENTA" pues seaan igualws.
    nombre_buscado = nombre_buscado.lower()
 
    # Indica si la categoría existe; sirve para avisar cuando no se encontró.
    encontrada = False
 
    for posicion, nombre in enumerate(categorias):#aqui no estaba segura como podria por ner en el for dos variables pero en mi asesoria que nos compartieron por correo pregunté.
        if nombre.lower() == nombre_buscado:
            gastos[posicion] = int(input("Nuevo monto para " + nombre + ":$ "))
            encontrada = True
            print("Gasto modificado correctamente")
 
    if encontrada == False:
        print("Esa categoria no existe.")
 
 #dashboard
# NUEVO: arma una lista de listas con los datos de cada categoría juntos:
# [nombre, monto, porcentaje del ingreso]. Se eligió una lista de listas
# porque cada categoría tiene varios datos relacionados, y así la tabla se
# puede recorrer fila por fila para mostrarla.
def crear_tabla(categorias, gastos, ingresos):
    tabla = []
 
    # Se necesita la posición para tomar, de la lista "gastos", el monto que
    # corresponde a cada nombre de la lista "categorias".
    for posicion, nombre in enumerate(categorias):
        monto = gastos[posicion]
 
        # Se evita dividir entre cero si no hay ingresos registrados.
        if ingresos > 0:
            porcentaje = monto * 100 / ingresos
        else:
            porcentaje = 0
 
        tabla.append([nombre, monto, porcentaje])
 
    return tabla
 
 
# NUEVO: muestra el desglose de gastos en consola. Aquí se procesan cadenas
# para que el reporte sea fácil de leer: se alinean las columnas y cada
# categoría lleva una barra de texto proporcional a su porcentaje.
def mostrar_tabla(tabla):
    print()
    print("----- " + "DESGLOSE DE GASTOS".upper() + " -----")
 
    # Cada fila de la lista de listas tiene: fila[0] nombre, fila[1] monto
    # y fila[2] porcentaje.
    for fila in tabla:
 
        # Un bloque por cada 5% del ingreso, para que las barras sean cortas
        # y comparables entre categorías.
        bloques = int(fila[2] // 5)
        barra = "█" * bloques
 
        # El monto se convierte a cadena para poder agregarle el signo "$" y
        # alinearlo con las demás filas.
        texto_monto = "$" + str(fila[1])
        print(fila[0].ljust(16), texto_monto.ljust(8), barra, round(fila[2], 1), "%")
 
 
# NUEVO: implementa el dashboard que en el Avance 2 estaba pendiente.
# Muestra la tabla en consola, indica en qué se gastó más y abre una ventana
# con dos gráficas: barras para comparar categorías y pastel para ver qué
# parte del gasto total representa cada una.
def generar_dashboard(categorias, gastos, ingresos, total_gastos, restante):
 
    tabla = crear_tabla(categorias, gastos, ingresos)
    mostrar_tabla(tabla)
 
    # Se busca la categoría con mayor gasto para destacarla: la posición del
    # monto máximo en "gastos" es la misma que la de su nombre en "categorias".
    mayor = max(gastos)
    categoria_mayor = categorias[gastos.index(mayor)]
    print()
    print("Categoría con más gasto:", categoria_mayor.upper(), "($" + str(mayor) + ")")
 
    # Una sola ventana con las dos gráficas lado a lado, para verlas juntas.
    figura, (grafica_barras, grafica_pastel) = plt.subplots(1, 2, figsize=(12, 5))
 
    # Barras: permiten comparar cuánto se gastó en cada categoría.
    grafica_barras.bar(categorias, gastos, color="#1677b8")
    grafica_barras.set_title("GASTOS POR CATEGORIA")
    grafica_barras.set_ylabel("Gasto ($)")
 
    # Los nombres se inclinan para que no se encimen entre sí.
    grafica_barras.tick_params(axis="x", rotation=30)
 
    # Pastel: muestra la proporción de cada gasto respecto al total. Solo se
    # dibuja si hay gastos, porque con todo en cero no hay proporciones.
    if total_gastos > 0:
        grafica_pastel.pie(gastos, labels=categorias, autopct="%1.1f%%", startangle=90)
    else:
        grafica_pastel.text(0.5, 0.5, "Todavia no hay gastos", ha="center", va="center")
    grafica_pastel.set_title("DISTRIBUCION DE GASTOS")
 
    # Resumen del mes en el título para ver los totales junto a las gráficas.
    figura.suptitle("Ingresos: $" + str(ingresos) + "    Gastos: $" + str(total_gastos) + "    Restante: $" + str(restante))
 
    plt.tight_layout()
    plt.show()
 
 
# PENDIENTE: verificar mas estilos de dashboard, al ser principiante en progra
#tuve que  uscar dif tutoriales peor al ver que no todos tenian todos los elementos
#que yo usaba solicité ayuda a otro ITC además de investigar yo por mi cuenta.
 
 

def main():
    menu()
 
 
main()
 
