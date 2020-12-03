import abc
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
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

Builder.load_string('''
#:kivy 1.10.0
#: import Popup kivy.uix.popup

<MessageBox>:
    title: 'Popup Message Box'
    size_hint: None, None
    size: 400, 400

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.message
        Button:
            size_hint: 1, 0.2
            text: 'OK'
            on_press: root.dismiss()

<RecycleViewRow>:
    orientation: 'horizontal'
    Label:
        text: root.text
    Button:
        text: 'Mostrar'
        on_press: app.root.message_box(root.text)

<MainScreen>:
    viewclass: 'RecycleViewRow'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
                    ''')

class MessageBox(Popup):
    message = StringProperty()

class RecycleViewRow(BoxLayout):
    text = StringProperty()

class MainScreen(RecycleView):
    lista_v=[]
    lista_v.append(Camion("426-EE-9", "Honda", "Blanco"))
    lista_v.append(Camion("EMN-71-71", "Mercedes benz", "Negro"))
    lista_v.append(Coche("HAW-162-A", "Nissan", "Rojo"))
    lista_v.append(Coche("EF-16-199", "BMW", "Plateado"))
    def init(self, kwargs):
        super(MainScreen, self).init(kwargs)
        self.data = [{'text': "Button " + str(x), 'id': str(x)} for x in len(lista_v)]

    def message_box(self, message):
        p = MessageBox()
        p.message = messageg
        p.open() 
        print('test press: ', message)

class TestApp(App):
    title = "RecycleView Direct Test"

    def build(self):
        return MainScreen()

if __name__ == "__main__":
    TestApp().run()