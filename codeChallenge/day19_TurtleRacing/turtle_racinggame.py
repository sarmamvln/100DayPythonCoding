import random
import turtle
import sys
from turtle import Turtle, Screen

from click import prompt

is_race_on= False
screen= Screen()
screen.setup(width=500, height=500)
user_bet= screen.textinput(title="User Bet", prompt="Ente the color you wan tto bet ")
colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos= [-100, -70, -40, -10, 20, 50 ]
all_turtles= []

for turtle_index in range(0, 6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on= True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have WON!! the {winning_color} turtle is the winner.")
            else:
                print(f"You have LOST!! the {winning_color} turtle is the winner.")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

