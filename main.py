from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter #放大縮小的功能

class Create_App(App):
    def build(self):
        label1=Label(text="Hi",font_size=96)
        sct=Scatter()
        sct.add_widget(label1)

        return sct

if __name__=="__main__":
    Create_App().run()