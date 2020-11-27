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

    score = kivy.properties.NumericProperty(0)
    font = kivy.properties.NumericProperty(0)

    def start(self):
        balls = [self.red_ball_1, self.red_ball_2, self.red_ball_3, self.red_ball_4, 
        self.red_ball_5, self.blue_ball_1, self.blue_ball_2, self.blue_ball_3, self.blue_ball_4, 
        self.blue_ball_5]

        for i in balls:
            i.velocity = Vector(0, 1.5)

        
    def update(self, td):

        balls = [self.red_ball_1, self.red_ball_2, self.red_ball_3, self.red_ball_4, 
        self.red_ball_5, self.blue_ball_1, self.blue_ball_2, self.blue_ball_3, self.blue_ball_4, 
        self.blue_ball_5]


        for i in balls:
            i.move()
            if i.center_x <= 0 or i.center_x >= self.width or i.center_y >= self.height:
                i.center_x = random.choice([150.0, 650.0])
                i.center_y = -200
                i.velocity = Vector(0, 1.5)
            if i.center_y >= self.height - 30:
                i.center_y = self.height/4 * -1
                i.velocity = Vector(0, 0)
                self.score += 1
                if self.score >= 10:
                    self.font = 34
                    for i in balls:
                        i.center_y = -200
                        i.velocity = Vector(0,0)
                    

        for a in balls:
            for b in balls:
                if a != b:
                    deff = a.center_y - b.center_y
                    if deff < 90 and deff > 0:
                        a.center_x = random.choice([self.width/4 -50 , self.width * 3/4 + 50])
                        a.center_y = -200
                        a.velocity = Vector(0, 1.5)

       
    def on_touch_move(self, touch):

        balls = [self.red_ball_1, self.red_ball_2, self.red_ball_3, self.red_ball_4, 
        self.red_ball_5, self.blue_ball_1, self.blue_ball_2, self.blue_ball_3, self.blue_ball_4, 
        self.blue_ball_5]

        for i in balls:
            deff = math.sqrt((touch.x - i.center_x) ** 2 + (touch.y - i.center_y) ** 2)
            if deff <= self.width/8 + 3:
                i.center_x = touch.x

            if i.center_x >= self.width/2 - 100 and i.center_x <= self.width * 3/4 + 30:
                i.velocity_x = -15

            if i.center_x >= self.width * 3/4 + 70:
                i.velocity_x = 15

            if i.center_x <= self.width/4 - 70:
                i.velocity_x = -15

            if i.center_x >= self.width/4 - 40 and i.center_x <= self.width/2:
                i.velocity_x = 15

class app(App):
    def build(self):
        game = main()
        game.start()
        Clock.schedule_interval(game.update, 1.00/60.00)
        return game

app().run()