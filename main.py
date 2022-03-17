from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout



class WidgetsExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("1")
    #slider_value_txt = StringProperty("0")
    texte_input_str = StringProperty("DessIA")

    def on_toggle_button_state(self, widget): # self dans le kv
        # print("Toggle state : " + widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True

    def on_button_click(self):
        print("Button click")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_switch_active(self, widget):
        print("Switch : " + str(widget.active))

    # def on_slider_value(self, widget):
        # print("Slider : " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.texte_input_str = widget.text






"""class BoxLayoutExemple(BoxLayout):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""





#class GridLayoutExemple(GridLayout):
#    pass






class LeLabApp(App):
    pass

LeLabApp().run()