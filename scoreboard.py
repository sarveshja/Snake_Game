from turtle import Turtle

FONT = ("Arial",16,"normal")
ALIGNMENT = "center"

class ScreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0,220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increasescore(self):
        if(self.score >50):
            self.score += 2
        elif(self.score >150):
            self.score += 3
        else:
            self.score += 1
        self.clear()
        self.update_scoreboard()

