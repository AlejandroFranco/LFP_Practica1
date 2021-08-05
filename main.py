import re
import webbrowser
import tkinter as tk
from tkinter import filedialog
from pip._vendor.distlib.compat import raw_input

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Main:

    lista = []
    comandos = []

    def menu(self):
        print("\n")
        print("1 Cargar archivo de entrada")
        print("2 Mostrar reporte en consola")
        print("3 Exportar reporte")
        print("4 salir" + "\n")
        entrada = input("Ingrese un numero 1-6" + "\n")
        patron = "[1-6]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarArchivo()
                self.menu()
            elif entrada == "2":
                self.mostrarReporte()
                self.menu()
            elif entrada == "3":
                    c = 2
            elif entrada == "4":
                raw_input("Presione una tecla" + "\n")
        else:
            self.menu()

    def mostrarReporte(self):
        for comando in self.comandos:
            comando = comando.strip()
            if comando == "ASC":
                print("\n")
                print("-------------------------------")
                print("Datos ordenados ascendentemente")
                print("\n")
                a = self.ordenarAsc(self.copiarLista(self.lista))
                self.imprimirLista(a)
            elif comando == "DESC":
                print("\n")
                print("-------------------------------")
                print("Datos ordenados descendentemente")
                print("\n")
                a = self.ordenarDesc(self.copiarLista(self.lista))
                self.imprimirLista(a)
            elif comando == "AVG":
                print("\n")
                print("-------------------------------")
                print("Promedio de la clase")
                print(self.avg())
            elif comando == "MIN":
                print("\n")
                print("-------------------------------")
                print("Nota minima de la clase")
                a = self.min()
                print(a.nombre + " " + str(a.nota))
            elif comando == "MAX":
                print("\n")
                print("-------------------------------")
                print("Nota maxima de la clase")
                a = self.max()
                print(a.nombre + " " + str(a.nota))
            elif comando == "APR":
                print("\n")
                print("-------------------------------")
                print("Numero de aprobados")
                print(self.apr())
            elif comando == "REP":
                print("\n")
                print("-------------------------------")
                print("Numero de reprobados")
                print(self.rep())

    def imprimirLista(self,lista):
        for elemento in lista:
            print("Nombre__"+elemento.nombre+" Nota__"+str(elemento.nota))

    def copiarLista(self, lista_original):
        a = []
        for i in lista_original:
            a.append(i)
        return a

    #quicksort
    def ordenarAsc(self, lista):
        longitud = len(lista)
        if longitud <= 1:
            return lista
        else:
            pivote = lista.pop()
        elementos_mayores = []
        elementos_menores = []
        for elemento in lista:
            if elemento.nota > pivote.nota:
                elementos_mayores.append(elemento)
            else:
                elementos_menores.append(elemento)

        return self.ordenarAsc(elementos_menores) + [pivote] + self.ordenarAsc(elementos_mayores)

    # quicksort
    def ordenarDesc(self, lista):
        longitud = len(lista)
        if longitud <= 1:
            return lista
        else:
            pivote = lista.pop()
        elementos_mayores = []
        elementos_menores = []
        for elemento in lista:
            if elemento.nota < pivote.nota:
                elementos_mayores.append(elemento)
            else:
                elementos_menores.append(elemento)

        return self.ordenarDesc(elementos_menores) + [pivote] + self.ordenarDesc(elementos_mayores)

    def avg(self):
        suma = 0
        n = 0
        for elemento in self.lista:
            n += 1
            suma += elemento.nota
        return suma/n

    def min(self):
        return self.ordenarAsc(self.copiarLista(self.lista))[0]

    def max(self):
        return self.ordenarAsc(self.copiarLista(self.lista))[-1]

    def apr(self):
        n = 0
        for elemento in self.lista:
            if elemento.nota > 61:
                n += 1
        return str(n)

    def rep(self):
        n = 0
        for elemento in self.lista:
            if elemento.nota < 61:
                n += 1
        return str(n)

    def exportarReporte(self):
        c =1
    def organizarDatos(self, contenido):
        lineas = contenido.split("\n")
        for i in range(1, len(lineas)-1):
            nombre = lineas[i][lineas[i].index('"')+1:lineas[i].rindex('"')]
            nota = int(lineas[i][lineas[i].index(";")+1:lineas[i].index(">")])
            self.lista.append(Estudiante(nombre, nota))
            self.comandos = lineas[-1][lineas[-1].index("}")+1: len(lineas[-1])].split(",")


    def cargarArchivo(self):
        root = tk.Tk()
        #root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                        filetypes=(("texto", "*.lfp"), ("todos", "*.*")))
        try:
            archivo = open(nombre_archivo, "r")
            contenido_archivo = archivo.read()
            self.organizarDatos(contenido_archivo)
        except FileNotFoundError:
            print("archivo no encontrado")


Main().menu()