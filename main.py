from kivy.app import App
import kivy
from kivy.uix.widget import Widget
from kivy import properties
from kivy.clock import Clock
from kivy.vector import Vector
import math
import random 

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

    red_ball_1 = kivy.properties.ObjectProperty(None)
    red_ball_2 = kivy.properties.ObjectProperty(None)
    red_ball_3 = kivy.properties.ObjectProperty(None)
    red_ball_4 = kivy.properties.ObjectProperty(None)
    red_ball_5 = kivy.properties.ObjectProperty(None)

    blue_ball_1 = kivy.properties.ObjectProperty(None)
    blue_ball_2 = kivy.properties.ObjectProperty(None)
    blue_ball_3 = kivy.properties.ObjectProperty(None)
    blue_ball_4 = kivy.properties.ObjectProperty(None)
    blue_ball_5 = kivy.properties.ObjectProperty(None)
    lane = "right"

    red_ball_1_lane = "right"


    def start(self):
        balls = [self.red_ball_1, self.red_ball_2, self.red_ball_3, self.red_ball_4, 
        self.red_ball_5, self.blue_ball_1, self.blue_ball_2, self.blue_ball_3, self.blue_ball_4, 
        self.blue_ball_5]

        for i in balls:
            i.velocity = Vector(0, 3)

        
    def update(self, td):

        balls = [self.red_ball_1, self.red_ball_2, self.red_ball_3, self.red_ball_4, 
        self.red_ball_5, self.blue_ball_1, self.blue_ball_2, self.blue_ball_3, self.blue_ball_4, 
        self.blue_ball_5]

        for i in balls:
            i.move()

        if self.red_ball_1.center_x <= 0 or self.red_ball_1.center_x >= self.width:
            self.red_ball_1.center_x = random.choice([150.0, 650.0])
            self.red_ball_1.center_y = -100
            self.red_ball_1.velocity = Vector(0, 3)

        if self.red_ball_1.center_x == 150.0:
            self.red_ball_1_lane = "left"
        else:
            self.red_ball_1_lane = "right"
       
    def on_touch_move(self, touch):

        balls = [self.red_ball_1, self.red_ball_2, self.red_ball_3, self.red_ball_4, 
        self.red_ball_5, self.blue_ball_1, self.blue_ball_2, self.blue_ball_3, self.blue_ball_4, 
        self.blue_ball_5]

        for i in balls:
            deff = math.sqrt((touch.x - i.center_x) ** 2 + (touch.y - i.center_y) ** 2)
            if deff <= 150:
                i.center_x = touch.x

        if self.red_ball_1.center_x >= 500 and self.red_ball_1.center_x <= 630:
            self.red_ball_1.velocity_x = -15

        if self.red_ball_1.center_x >= 670:
            self.red_ball_1.velocity_x = 15

        if self.red_ball_1.center_x <= 130:
            self.red_ball_1.velocity_x = -15

        if self.red_ball_1.center_x >= 180 and self.red_ball_1.center_x <= 400:
            self.red_ball_1.velocity_x = 15


class app(App):
    def build(self):
        game = main()
        game.start()
        Clock.schedule_interval(game.update, 1.00/60.00)
        return game

app().run()