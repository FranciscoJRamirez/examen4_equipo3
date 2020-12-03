import abc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from functools import partial
from kivy.uix.popup import Popup

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
    def apaga(self):
        return "Esta apagado"
    def prenderApagar(self):
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
    def apaga(self):
        return "Esta apagado"
    def prenderApagar(self):
        if self.esta_encendido:
            self.esta_encendido = False
        else:
            self.esta_encendido = True

class Examen4(App):
    lista_v = []
    lista_v.append(Camion("GHA-45-43", "NISSAN", "BLANCO"))
    lista_v.append(Camion("HHP-22-12", "MERCEDES BENZ", "NEGRO"))
    lista_v.append(Coche("OJK-88-54", "CHEVROLETE", "ROJO"))
    lista_v.append(Coche("OKJ-12-36", "FORD", "AZUL"))
    def build(self):
        
        label = Label(text="Vehiculos")

        infolabel1= Label(text=self.lista_v[0].placa)
        boton1 = Button(text="Mostrar")
        boton1.bind(on_press=partial(self.popup_1, 0))

        infolabel2= Label(text=self.lista_v[1].placa)
        boton2 = Button(text="Mostrar")
        boton2.bind(on_press=partial(self.popup_1, 1))

        infolabel3= Label(text=self.lista_v[2].placa)
        boton3 = Button(text="Mostrar")
        boton3.bind(on_press=partial(self.popup_1, 2))

        infolabel4= Label(text=self.lista_v[3].placa)
        boton4 = Button(text="Mostrar")
        boton4.bind(on_press=partial(self.popup_1, 3))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(label)

        layout1 = BoxLayout(size_hint=(1, None), height=50)
        layout1.add_widget(infolabel1)
        layout1.add_widget(boton1)

        layout2= BoxLayout(size_hint=(1, None), height=50)
        layout2.add_widget(infolabel2)
        layout2.add_widget((boton2))

        layout3 = BoxLayout(size_hint=(1, None), height=50)
        layout3.add_widget(infolabel3)
        layout3.add_widget(boton3)

        layout4 = BoxLayout(size_hint=(1, None), height=50)
        layout4.add_widget(infolabel4)
        layout4.add_widget(boton4)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)
        root.add_widget(layout1)
        root.add_widget(layout2)
        root.add_widget(layout3)
        rott.add_widget(layout4)

        return root
    def popup_1(self, index, *args):
        box = BoxLayout(orientation = 'vertical', padding = (10))
        box.add_widget(Label(text="Placa: "+self.lista_v[index].placa))
        box.add_widget(Label(text="Marca}: "+self.lista_v[index].marca))
        box.add_widget(Label(text="Color: "+self.lista_v[index].color))
        box.add_widget(Label(text=self.lista_v[index].enciende()))
        
        
        box.add_widget(Label(text = "¿Encender el vehiculo? \n "))
        popup = Popup(title='Información del vehiculo', title_size= (30), 
                    title_align = 'center', content = box,
                    size_hint=(None, None), size=(400, 400),
                    auto_dismiss = True)
        box.add_widget(Button(text = "Encender/Apagar",  on_press=partial(self.funcionx, index)))
        box.add_widget(Button(text = "Cerrar",  on_press=popup.dismiss))

        popup.open()
    def funcionx(self, index, *args):
        self.lista_v[index].prenderApagar()
        
if __name__ == '__main__':
    Examen4().run()