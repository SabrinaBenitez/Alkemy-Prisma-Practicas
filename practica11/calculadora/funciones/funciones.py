import datetime
import unittest
import sys

def menu() -> str:
    opcion=input(' **** Calculadora ****\n'
          ' 1 -Suma '
          ' 2 -Resta '
          ' 3 -Multiplcacion '
          ' 4 -Division '
          ' 5 -Salir\n')
    return opcion
    
def calculadora(opcion : str):
  
    if opcion == '1':
        
        try:
            num1 =int(input('Ingrese un numero:'))
            num2 =int(input('Ingrese un numero:'))
            resultado_suma = obtener_suma(num1,num2)
            print(f'El Resultado de la Suma es:{resultado_suma}')
        except ValueError:
            print('el numero debe ser un entero')

        
    elif opcion== '2':
        try:
            num1 =int(input('Ingrese un numero:'))
            num2 =int(input('Ingrese un numero:'))
            resultado_resta=obtener_resta(num1,num2)
            print(f'El Resultado de la Suma es:{resultado_resta}')
        except ValueError:
            print('el numero debe ser un entero')
    elif opcion == '3':
        try:
            num1 =int(input('Ingrese un numero:'))
            num2 =int(input('Ingrese un numero:'))
            resultado_multiplicacion=obtener_multiplicacion(num1,num2)
            print(f'El Resultado de la Suma es:{resultado_multiplicacion}') 
        except ValueError:
            print('el numero debe ser un entero')     
    elif opcion == '4': 
        try:
            num1 =int(input('Ingrese un numero:'))
            num2 =int(input('Ingrese un numero:'))
            resultado_division=obtener_division(num1,num2)
            print(f'El Resultado de la Suma es:{resultado_division}')
        except ValueError:
            print('el numero debe ser un entero')    
   
def obtener_suma(num1: int, num2: int) -> int:
    return num1 + num2
   

def obtener_resta(num1: int, num2: int) -> int:
    return num1 - num2
 

def obtener_multiplicacion(num1: int, num2: int) -> int:
    return num1 * num2
  

def obtener_division(num1: int, num2: int) -> int:
    try:
        return num1 / num2 
    except ZeroDivisionError:
        print('No es Posible realizar una division por cero(0)')

def insertar_cabecera(f):
    f.write('\n')
    f.write('************ Testing ************')
    f.write('\n')

    now = datetime.datetime.now()
    date_time=now.strftime('%m/%d/%Y, %H:%M:%S')
    f.write(date_time)
    f.write('\n')
    return f

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 

if __name__  == '__main__':
   
    while True:
        opcion = menu()
        if opcion == '5':
            break
        else:
            calculadora(opcion)
            
    with open('/mnt/c/Users/Alan Hernandez/Desktop/practica11/calculadora/tests/testing.txt','a') as f:
        f = insertar_cabecera(f)
        main(f)         
       
            