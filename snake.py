from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.snake = []
        self.x_pos = [0, 20, 40]
        for position in range(0,3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.up()
            new_turtle.goto(x=self.x_pos[position], y=0)
            self.snake.append(new_turtle)
        self.head = self.snake[0]

    def add_segment(self,x,y):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.up()
        new_turtle.goto(x=x, y=y)
        self.snake.append(new_turtle)

    def extend(self):
        self.add_segment(self.snake[-1].xcor(),self.snake[-1].ycor())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.snake[0].forward(20)

    def up(self):
        if(self.head.heading() != DOWN):
            self.snake[0].setheading(90)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.snake[0].setheading(180)

    def right(self):
        if (self.head.heading() != LEFT):
            self.snake[0].setheading(0)

    def down(self):
        if (self.head.heading() != UP):
            self.snake[0].setheading(270)