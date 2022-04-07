"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from typing import List


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]
    
    data1 = []
    for i in tablefile:
        data1.append(int(i[1]))

    suma = sum(data1)
    
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    list_letter = []
    for i in tablefile:
        if i[0] not in list_letter:
            list_letter.append(i[0])
    
    list_letter.sort(reverse=False)

    list_quantity=[]
    for j in list_letter:
        contador = 0
        for k in tablefile:
            if j == k[0]:
                contador += 1
        list_quantity.append(contador)

    tupla = list(zip(list_letter,list_quantity))

    return tupla


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    list_letter = []
    for i in tablefile:
        if i[0] not in list_letter:
            list_letter.append(i[0])
    
    list_letter.sort(reverse=False)

    list_sums=[]
    for j in list_letter:
        sumaAux = 0
        for k in tablefile:
            if j == k[0]:
                sumaAux += int(k[1])
        list_sums.append(sumaAux)

    tupla = list(zip(list_letter,list_sums))

    return tupla


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]
    
    list_months = []
    for i in tablefile:
        list_months.append(i[2])
    
    list_months_new =[]
    for j in list_months:
        list_months_new.append(j[5:7])
   
    final_list = list(set(list_months_new))
    final_list.sort(reverse=False)

    list_quantity=[]
    for k in final_list:
        contador=0
        for rows in list_months_new:
            if k == rows:
                contador +=1
        list_quantity.append(contador)

    tupla = list(zip(final_list,list_quantity))
    
    return tupla


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    list_letter = []
    for i in tablefile:
        if i[0] not in list_letter:
            list_letter.append(i[0])
    
    list_letter.sort(reverse=False)

    list_min=[]
    list_max=[]
    for j in list_letter:
        maxAux = 0
        for k in tablefile:
            if k[0] == j:
                if int(k[1])>maxAux:
                    maxAux = int(k[1])
        list_max.append(maxAux)
        minAux = maxAux
        for k in tablefile:
            if k[0] == j:  
                if int(k[1])<minAux:
                    minAux = int(k[1])
        list_min.append(minAux)


    
    tupla = list(zip(list_letter,list_max,list_min))

    return tupla


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    list_dict=[]
    for i in tablefile:
        list_dict.append(i[4])

    main_dict = [row.split(",") for row in list_dict]
    
    main_dict2 = []
    for i in main_dict:
        main_dict2.extend(i)

    final_dict = []
    for j in main_dict2:
        if j[:3] not in final_dict:
            final_dict.append(j[:3])

    final_dict.sort(reverse=False)

    list_min=[]
    list_max=[]
    auxList =[]
    
    for m in final_dict:
        for k in main_dict2:
            if k[:3] == m :
                auxList.append(int(k[4:]))
        minAux = min(auxList)
        maxAux = max(auxList)
        list_min.append(minAux)
        list_max.append(maxAux)
        auxList.clear()
        minAux = 0
        maxAux = 0

    tupla = list(zip(final_dict,list_min,list_max)) 
    return tupla


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        tablefile = file.readlines()
        
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    dataAux = [row[0] for row in tablefile]
    data2 = [row[1] for row in tablefile]
    data1 = list(zip(data2,dataAux))

    result = {}
    
    for clave, valor in data1:
        if clave in result.keys():
            result[clave].append(valor)
        else:
            result[clave] = [valor]

    result = [(int(key),valor) for key, valor in result.items()]
    result = sorted(result, key=itemgetter(0), reverse = False)

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    from operator import itemgetter
    with open("data.csv","r") as file:
        tablefile = file.readlines()
        
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    dataAux = [row[0] for row in tablefile]
    data2 = [row[1] for row in tablefile]
    data1 = list(zip(data2,dataAux))

    result = {}
    
    for clave, valor in data1:
        if clave in result.keys():
            result[clave].append(valor)
        else:
            result[clave] = [valor]

    for valor in result:
        list(set(result[valor]))

    result = [(int(key),sorted(list(set(valor)),key=itemgetter(0), reverse=False)) for key, valor in result.items()]
    result = sorted(result, key=itemgetter(0), reverse = False)

    return result

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    list_dict=[]
    for i in tablefile:
        list_dict.append(i[4])

    list_dict = [row.split(",") for row in list_dict]

    main_dict = []
    for i in list_dict:
        main_dict.extend(i)

    main_dict = [row[:3] for row in main_dict]

    final_dict = {}
    for clave in main_dict:
        if clave in final_dict.keys():
            final_dict[clave] = final_dict[clave] + 1
        else:
            final_dict[clave] =  1
 
    #final_dict = sort(final_dict)
    final_dict = [(key, valor) for key, valor in final_dict.items()]
    final_dict = sorted(final_dict, key=itemgetter(0), reverse = False)
    final_dict = {key: valor for key, valor in final_dict}

    #print(final_dict)
    return final_dict


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    letras = [row[0] for row in tablefile]
    fila4 = [row[3] for row in tablefile]
    fila4 = [len(row.split(",")) for row in fila4]
    fila5 = [row[4] for row in tablefile]
    fila5 = [len(row.split(",")) for row in fila5]

    finallist = list(zip(letras, fila4, fila5))

    return finallist


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]
    
    col2 = [row[1] for row in tablefile]
    col4 = [row[3] for row in tablefile]
    col4 = [row.split(",") for row in col4]

    basis_list2=[]
    basis_listAux=[]
    for element in range(0, len(col2)):
        for listas in range(0, len(col4[element])):
            #print(fila4[element][listas])
           basis_list2.append(col4[element][listas])
           basis_listAux.append(int(col2[element]))
    
    final_list = list(zip(basis_list2, basis_listAux))
    final_list = sorted(final_list, key=itemgetter(0), reverse = False)

    final_dict = {}
    for i in final_list:
        if i[0] in final_dict.keys():
            final_dict[i[0]] = final_dict[i[0]] + i[1]
        else:
            final_dict[i[0]] = i[1]

    return final_dict


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        tablefile = file.readlines()
    
    tablefile = [row.replace("\n", "") for row in tablefile]
    tablefile = [row.split("\t") for row in tablefile]

    letras = [row[0] for row in tablefile]
    fila5 = [row[4] for row in tablefile]
    fila5 = [row.split(",") for row in fila5]

    values_list=[]
    letras_list=[]
    for element in range(0, len(letras)):
        for listas in range(0, len(fila5[element])):
            #print(fila4[element][listas])
           values_list.append(fila5[element][listas])
           letras_list.append(letras[element])

    values_list = [int(row[4:]) for row in values_list]

    final_list = list(zip(letras_list, values_list))
    final_list = sorted(final_list, key=itemgetter(0), reverse = False)

    final_dict = {}
    for i in final_list:
        if i[0] in final_dict.keys():
            final_dict[i[0]] = final_dict[i[0]] + i[1]
        else:
            final_dict[i[0]] = i[1]

    return final_dict

