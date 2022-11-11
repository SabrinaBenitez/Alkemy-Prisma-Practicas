def cantidad_caracteres_lista_animales(animales: list)->list:
    # La funcion recorre la lista de animales
    # calcula la longitud de cada palabra contenida en la lista de animales
    # retorna una lista con longitud obtenida

    """ funcion que obtiene la cantidad de caracteres de las palabras contenidas en una lista

    :return: caracteres
    :rtype:  lista
    """
    lista_longitud = []
    for animal in animales:
        longitud_palabra = len(animal)
        lista_longitud.append(longitud_palabra)
        return lista_longitud


if __name__ == '__main__':

    animales = ['perro', 'elefante', 'dragón']

    caracteres_lista_animales = cantidad_caracteres_lista_animales(animales)

    print(animales)
    print(caracteres_lista_animales)