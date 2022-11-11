def obtener_medio_transporte(medios_transporte: list) -> str:
    indice = int(input('Ingrese indice:'))
    try: 
        if indice > 0:
            return f'Medio de Transporte:{medios_transporte[indice]}'  
        else:
            print('Indice debe ser Positivo')
    except IndexError:
        print('Ocurrio un error...')
        obtener_medio_transporte(medios_transporte)