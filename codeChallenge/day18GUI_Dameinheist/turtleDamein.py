import random
import sys
import turtle
from turtle import Turtle, Screen


class turtleDamein:
    turtle.colormode(255)
    def __init__(self):

        self.mybrush= Turtle()
        self.gui= Screen()

    def uiScreenUp(self):
        return self.gui.exitonclick()

    def __availableShapes(self):
        return self.gui.getshapes()

    def setDesiredShpae(self, desiredShape='turtle'):
        if desiredShape not in self.__availableShapes():
            sys.exit(f"Icon '{desiredShape}' NOT available, you might want to consider Registering the new shape, "
                  f"if you have gif of your shape")
        else:
            self.mybrush.shape(desiredShape)


    def goForward(self, length=0):
        self.mybrush.forward(length)

    def updateTurnByDirection(self, direction='left', angle= 90):
        """

        :param angle: degree of turn
        :param direction: direction of turn 'left' or 'right'
        :return:
        """
        if direction.lower() == 'left':
            self.mybrush.left(angle)
        elif direction.lower() == 'right':
            self.mybrush.right(angle)
        elif direction.lower() in ['back', 'reverse' ] :
            self.mybrush.right(angle)
            self.mybrush.right(angle)


    def drawSquare(self, length):
        if length==0:
            sys.exit('Cannot create a squar ewith 0 length, please correctly enter required length if square')
        else:
            # self.goForward(length)
            # self.updateTurnByDirection('right')
            # self.goForward(length)
            # self.updateTurnByDirection('right')
            # self.goForward(length)
            # self.updateTurnByDirection('right')
            # self.goForward(length)s
            for _ in range(4):
                self.goForward(length)
                self.updateTurnByDirection('right', 90)

    def drawDottedLine(self, length= 0, dot_length=5, gap_length=5):
        if length==0:
            sys.exit("zero length speicifed, cannot proceed, enter valid length")
        else:
            total_steps = length // (dot_length + gap_length)
            for _ in range(total_steps):
                self.mybrush.pendown()
                self.goForward(dot_length)
                self.mybrush.penup()
                self.goForward(gap_length)

    def drawCircle(self, radius=0):
        if radius==0:
            sys.exit("zero diameter circle cannot be drawn, update diameter to >0")
        else:
            self.mybrush.circle(radius=radius)

    def drawShapes(self, num_sides=3):
        color= ['dark green', 'orange', 'dark magenta', 'hot pink', 'pale violet red',
                'medium slate blue', 'linen', 'bisque', 'moccasin', 'gold', 'yellow', 'mint cream'
                ]
        angel= 360/num_sides
        self.mybrush.color(random.choice(color))
        for _ in range(num_sides):
            self.goForward(100)
            self.updateTurnByDirection('right', angel)

    def draw_randomWalk(self):
        for _ in range(100) :
            randdir= random.choice(['left', 'right', 'reverse'])
            randlen= random.randint(15, 25)
            color = ['dark green', 'orange', 'dark magenta', 'hot pink', 'pale violet red',
                     'medium slate blue', 'linen', 'bisque', 'moccasin', 'gold', 'yellow', 'mint cream'
                     ]
            self.mybrush.pen(pencolor=random.choice(color), pensize=random.randint(15,20), speed=random.randint(5, 15))
            self.goForward(randlen)
            self.updateTurnByDirection(randdir)

    def random_color(self):
        r= random.randint(0, 255)
        g= random.randint(0, 255)
        b= random.randint(0, 255)
        randomcolor= (r, g, b)
        return randomcolor

    def draw_spirograph(self, size_of_gap):

        # for i in range(0,370,10):
        #     #self.mybrush.color(self.random_color())
        #     self.drawCircle(100, self.random_color())
        #     self.updateTurnByDirection('left', i)

        for _ in range(int(360/size_of_gap)):
            self.mybrush.pen(pencolor=self.random_color(), speed=200000)
            self.drawCircle(100)
            self.mybrush.setheading(self.mybrush.heading()+size_of_gap)


    def draw_art(self):
        self.mybrush.penup()
        self.mybrush.hideturtle()
        self.mybrush.setheading(225)
        self.mybrush.forward(300)
        self.mybrush.setheading(0)
        number_dots= 100

        for dot_count in range(1, number_dots+1):
            self.mybrush.speed('fastest')

            self.mybrush.dot(20, self.random_color())
            self.goForward(50)

            if  dot_count%10==0:
                self.mybrush.setheading(90)
                self.mybrush.forward(50)
                self.mybrush.setheading(180)
                self.mybrush.forward(500)
                self.mybrush.setheading(0)








tu= turtleDamein()
tu.setDesiredShpae()

#tu.drawSquare(100)
#tu.drawDottedLine(100)
#tu.drawCircle(20)
# tu.drawShapes(3)
# tu.drawShapes(4)
# tu.drawShapes(5)
# tu.drawShapes(6)
#tu.draw_randomWalk()
#tu.draw_spirograph(10)
tu.draw_art()

tu.uiScreenUp()