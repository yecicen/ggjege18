from dash import Dash
class Level:
    def __init__(self):
        self.dashList = []

    def generate(self, width, height):
        for x in range(width):
            for y in range(height):
                dash = Dash(x,y)
                self.dashList.append(dash)

    def render(self, display):
        for dash in self.dashList:
            dash.render(display)
