import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)

colors = ['red', 'purple', 'green', 'orange', 'blue']
y = -150
user_bet = screen.textinput(title="Make your bet,(red/orange/green/purple/blue)",prompt="Which turtle will win the race").lower()
all_ninja_turtles = []

for i in range(0,5): #creates the turtles,spaces them out,assigns different colours and places them in a list which we use later
    new_turt = Turtle(shape="turtle")
    new_turt.color(colors[i])
    new_turt.penup()
    y += 40
    new_turt.goto(x=-250, y=y)
    all_ninja_turtles.append(new_turt)

if user_bet:
    race_on=True #stops the race from happening without user input

while race_on:

    for turtle in all_ninja_turtles:
        if turtle.xcor() > 230:# onces turtle reaches this co-ordinate aka the finish line the race ends and the winner is announced
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"Congratulations the {turtle.pencolor()} turtle won,so you win!")
            else:
                print(f"The {turtle.pencolor()} won ,you lost!")
            race_on = False
        rand_int = random.randint(0, 10)
        turtle.forward(rand_int)





screen.exitonclick()
