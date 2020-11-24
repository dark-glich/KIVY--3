from kivy.app import App
import kivy
from kivy.uix.widget import Widget
from kivy import properties
from kivy.clock import Clock
from kivy.vector import Vector

class blue_ball(Widget):
    velocity_x = kivy.properties.NumericProperty(0)
    velocity_y = kivy.properties.NumericProperty(0)
    velocity = kivy.properties.ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class red_ball(Widget):
    kivy.lang.Builder.load_file("components.kv")
    velocity_x = kivy.properties.NumericProperty(0)
    velocity_y = kivy.properties.NumericProperty(0)
    velocity = kivy.properties.ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class main(Widget):
    ball_1 = kivy.properties.ObjectProperty(None)
    ball_2 = kivy.properties.ObjectProperty(None)
    blue_ball_1 = kivy.properties.ObjectProperty(None)

    def start(self):
        self.ball_1.velocity = Vector(0, 3)
        self.ball_2.velocity = Vector(0, 3)
        self.blue_ball_1.velocity = Vector(0, 3)
        

    def update(self, td):
        self.ball_1.move()
        self.ball_2.move()
        self.blue_ball_1.move()
        

class app(App):
    def build(self):
        game = main()
        game.start()
        Clock.schedule_interval(game.update, 1.00/60.00)
        return game

app().run()