from obtener_transporte import obtener_medio_transporte


if __name__ == '__main__':
    medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']
    while True:
        print(obtener_medio_transporte(medios_transporte))