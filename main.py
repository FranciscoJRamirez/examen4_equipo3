import abc
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stencilview import StencilView
from random import random as r
from functools import partial

class Vehiculo(abc.ABC):
    def __init__(self, placa, marca, color):
        self.placa = placa
        self.marca = marca
        self.color = color
    @abc.abstractmethod
    def apaga(self):
        pass
    @abc.abstractmethod
    def enciende(self):
        pass
class Camion(Vehiculo):
    esta_encendido=False
    def enciende(self):
        if self.esta_encendido:
            return("Esta encendido")
        else:
            return self.apaga()
    def apaga():
        return "Esta apagado"
    def prenderApagar():
        if self.esta_encendido:
            self.esta_encendido = False
        else:
            self.esta_encendido = True

class Coche(Vehiculo):
    esta_encendido=False
    def enciende(self):
        if self.esta_encendido:
            return("Esta encendido")
        else:
            return self.apaga()
    def apaga():
        return "Esta apagado"
    def prenderApagar():
        if self.esta_encendido:
            self.esta_encendido = False
        else:
            self.esta_encendido = True

class Examen4(App):
    self.lista_v = []
    self.lista_v.append(Camion("GHA-45-43", "NISSAN", "BLANCO"))
    self.lista_v.append(Camion("HHP-22-12", "MERCEDES BENZ", "NEGRO"))
    self.lista_v.append(Coche("OJK-88-54", "CHEVROLETE", "ROJO"))
    self.lista_v.append(Coche("OKJ-12-36", "FORD", "AZUL"))
    def build(self):
        
        label = Label(text="Vehiculos")

        infolabel1= Label(lista_v[0].placa)
        boton1 = Button(text="Mostrar")
        boton1.bind(on_press=partial(self.mostrarInfo, 0))

        infolabel2= Label(lista_v[1].placa)
        boton2 = Button(text="Mostrar")
        boton2.bind(on_press=partial(self.mostrarInfo, 1))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(label)
        layout1 = BoxLayout(size_hint=(1, None), height=50)
        layout1.add_widget(infolabel1)
        layout1.add_widget(boton1)

        layout2= BoxLayout(size_hint=(1, None), height=50)
        layout2.add_widget(infolabel2)
        layout2.add_widget((boton2))

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)
        root.add_widget(layout1)
        root.add_widget(layout2)

        return root
    def mostrarInfo(self, index):
        pass

if __name__ == '__main__':
    Examen4().run()