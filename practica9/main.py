from transporte import obtener_medio_transporte

if __name__ == '__main__':
    medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']
 
    while True:
        #indice = int(input("Ingrese Indice:"))
        transporte = obtener_medio_transporte(medios_transporte)
        print('Medios de Transporte:'+ transporte)
       
           