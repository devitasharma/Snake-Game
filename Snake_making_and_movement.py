from turtle import Turtle


"""things u want to stay as it is should be defined as GLOBAL CONSTANT VARIABLES as below:"""
SNAKE_BODY_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# SNAKE_COLOR = ["red", "green", "yellow"]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class SnakeMakingAndMoving:

    def __init__(self):
        """making snake body"""
        self.snakes = []
        self.creating_snakes()
        self.snake_head = self.snakes[0]

    def creating_snakes(self):
        for snake_position in SNAKE_BODY_POSITION:
            self.add_snake(snake_position)

    def add_snake(self, snake_position):
        self.snake = Turtle(shape="square")
        self.snakes.append(self.snake)
        self.snake.color("pink")
        self.snake.penup()
        self.snake.goto(snake_position)

    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def reset(self):
        for i in self.snakes:
            i.goto(1000,1000)
        self.snakes.clear()
        self.creating_snakes()
        self.snake_head = self.snakes[0]

    """ moving the snake in next position : step 1: so we have [snake0]=snake1 [snake1]=snake2 [snake2]=snake3 """
    """ step 2 : now their orientation is |snake3|snake2|snake1| on screen 
        so in order to move we want |    |snake3|snake2|snake1|  means snake3 at snake2 position
        and snake2 at snake1 position and snake1 to move on keypress direction..and so on"""
    """ step 3 : so first we too x,y position of snake2 as new_position and pass on to the snake3
        goto function. similar for next snake"""

    def snake_movement(self):

        for current_snake_num in range(len(self.snakes) - 1, 0, -1):
            new_position_x = self.snakes[current_snake_num - 1].xcor()
            new_position_y = self.snakes[current_snake_num - 1].ycor()
            self.snakes[current_snake_num].goto(new_position_x, new_position_y)
        """ below we move snake1 so that others can also move."""

        self.snakes[0].forward(MOVE_DISTANCE)

    """Moving snake in particular direction / given direction :"""
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)



