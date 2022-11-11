def menu() -> str:
    m=input(' **** Calculadora ****\n'
          ' 1 -Suma '
          ' 2 -Resta '
          ' 3 -Multiplcacion '
          ' 4 -Division '
          ' 5 -Salir\n')
    
    return m
    
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
        num1 =int(input('Ingrese un numero:'))
        num2 =int(input('Ingrese un numero:'))
        resultado_resta=obtener_resta(num1,num2)
        print(f'El Resultado de la Suma es:{resultado_resta}')
    elif opcion == '3':
        num1 =int(input('Ingrese un numero:'))
        num2 =int(input('Ingrese un numero:'))
        resultado_multiplicacion=obtener_multiplicacion(num1,num2)
        print(f'El Resultado de la Suma es:{resultado_multiplicacion}')  
    elif opcion == '4': 
        num1 =int(input('Ingrese un numero:'))
        num2 =int(input('Ingrese un numero:'))
        resultado_division=obtener_division(num1,num2)
        print(f'El Resultado de la Suma es:{resultado_division}')
   
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