from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            
class PongBall(Widget):
    
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    lable1 = ObjectProperty(None)
    lable2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = Vector(*vel).rotate(randint(0, 360))
    
    def update(self, dt):
        self.ball.move()
        
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
            
        if (self.ball.x < 0):
            self.player2.score += 1
            # print(self.player2.score)
            self.lable2.text = str(self.player2.score)
            # print()
            self.ball.velocity_x *= -1
            self.serve_ball()
        if (self.ball.right > self.width):
            self.player1.score += 1
            self.lable1.text = str(self.player1.score)
            self.ball.velocity_x *= -1
            self.serve_ball()
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y
class PongApp(App):
    def build(self):
        
        self.game = PongGame()
        self.game.serve_ball()
        Clock.schedule_interval(self.game.update, 1.0/60.0)
        
        return self.game
    
    
if __name__ == '__main__':
    PongApp().run()