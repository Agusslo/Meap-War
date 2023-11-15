import csv
import os

def guardar_puntaje(archivo, puntaje):
    '''brief: guarda los puntos en un csv'''
    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([puntaje])


def recuperar_puntaje(archivo):
    '''brief: recupera los puntos leyendo el csv que le pase'''
    try:
        with open(archivo, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                return int(row[0])
    except (FileNotFoundError, IndexError):
        return 0

