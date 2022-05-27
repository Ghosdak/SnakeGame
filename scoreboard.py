from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-240,260)
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 18, 'normal'))
        
    def get_score(self):
        self.score += 1
        self.show_score()
        
    def game_over(self):
        self.goto(-10,0)
        self.write("Game Over!", align='center', font=('Arial', 18, 'normal'))
        