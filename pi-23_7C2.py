

import csv


def desafio(ambientes):
    print('Ejercicios con archivos CSV complejos')
    archivo = 'propiedades.csv'


    with open(archivo) as csvfile:
        data= list(csv.DictReader(csvfile))
    cantidad_2ambientes = 0
    cantidad_3ambientes = 0
    for fila in data:
        try:
            tipo_ambiente = int(fila.get("ambientes", 0.0))
        except:
            tipo_ambiente = 0
        if tipo_ambiente == 2:
            cantidad_2ambientes += 1
        elif tipo_ambiente == 3:
            cantidad_3ambientes += 1
    print(cantidad_2ambientes, cantidad_3ambientes)
    if ambientes == "2_ambientes":
        return cantidad_2ambientes        
    elif ambientes == "3_ambientes":
        return cantidad_3ambientes
    
    
if __name__ == '__main__':

    ambientes = desafio("2_ambientes")
    print(ambientes)
