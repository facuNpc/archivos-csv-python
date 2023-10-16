
import csv


def desafio():
    print('Ejercicio de archivos')    

    archivo = 'stock.csv'

    with open(archivo) as csvfile:
        data = list(csv.DictReader(csvfile))
    total_tornillos = 0
    for i in range(len(data)):
        cantidad_tornillos = float(data[i]["tornillos"])
        total_tornillos += cantidad_tornillos
    return total_tornillos

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
   