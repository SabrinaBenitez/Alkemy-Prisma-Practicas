def obtener_medio_transporte(medios_transporte: list) -> str:
    try:
        indice = int(input("Ingrese Indice:"))
        return medios_transporte[indice]
    except ValueError:
            return "Error. El valor ingresado debe ser un numero"    
    except IndexError:
            return "Error. Indice fuera de rango."
    
                    