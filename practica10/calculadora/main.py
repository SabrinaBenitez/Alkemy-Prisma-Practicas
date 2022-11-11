from funciones import menu,calculadora

if __name__  == '__main__':
   
    while True:
        opcion = menu()
        if opcion == '5':
            break
        else:
            calculadora(opcion)