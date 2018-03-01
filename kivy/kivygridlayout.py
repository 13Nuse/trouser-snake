import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
kivy.require('1.10.0')

# The Grid Layout organizes everything in a grid pattern


class GridLayoutApp(App):

    def build(self):
        return GridLayout()


glApp = GridLayoutApp()

glApp.run()
