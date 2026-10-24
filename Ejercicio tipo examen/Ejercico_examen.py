saldo = 1000

def depositar(valordepositar):
    if valordepositar < 1:
        print("El monto a depositar tiene que ser mayor que 0")
    else:
        valordepositar = valordepositar + saldo
    return valordepositar

def retirar (valorretirar):
    if valorretirar > saldo:
        print("No tienes el dinero suficiente para retirar ese monto")
    elif valor <0:
        print("Los montos a retirar no pueden ser negativos")
    else: 
        valor = saldo - valorretirar
    return valor



def menu ():
    print(
"""
*********** MENU ************
Elija una opcion:
1. Consultar saldo
2. Depositar Dinero
3. Retirar diner0
4. Salir

Aviso: Si Presiona 0, tambien saldra del sistema. 
""")




def leeropcion ():
    opcion = (input("Ingrese la accion que quiere realizar: "))
    while "0" > opcion > "4":
        print ("*** ERROR *** \n Las opciones a digitar son del 1 al 4. \n Si presiona 0 (CERO) tambien saldra del sistema")
        print ("\n")
        menu()
        opcion ("Digite nuevamente la accion que quiere realizar: ")

    return int(opcion)

def opcion_consultar():
    print("\n\n ----- CONSULTAR SALDO ----- \n\n")
    print("Tu saldo es: $", saldo)


def opcion_depositar ():
    print (" ----- DEPOSITO ----- ")
    deposito = int(input("Ingresa el monto a depositar \n"))
    print("\n\n Deposito exitoso, depositaste", deposito)
    return  depositar(deposito)
    



def opcion_retirar ():
    print(" ----- RETIRAR ----- ")
    retiro = int(input("Ingresa el monto a retirar "))
    print ("Retiro exitoso, tu retiro fue de:", retiro)
    return retirar(retiro)



while True:
    menu()
    opcion = leeropcion()
    match opcion:
        case 0:
            print ("\n\n")
            print ("Gracias por utilizar nuestros servicios.")
            break
        case 1:
            opcion_consultar()
        case 2:
            saldo = opcion_depositar()
        case 3:
            saldo = opcion_retirar()
        case 4:
            print ("\n\n")
            print("Gracias por utilizar nuestros servicios.")
            break