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
                print("Datos ordenados ascendentemente")
                a = self.ordenarAsc(self.copiarLista(self.lista))
                self.imprimirLista(a)
                c=3
            elif comando == "DESC":
                a =2
            elif comando == "AVG":
                a = 2
            elif comando == "MIN":
                a = 2
            elif comando == "MAX":
                a = 2
            elif comando == "APR":
                a = 2
            elif comando == "REP":
                a = 2

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


    #def ordenarDesc(self):
    #def avg(self):
  #  def min(self):
  #  def max(self):
  #  def apr(self):
  #  def rep(self):

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