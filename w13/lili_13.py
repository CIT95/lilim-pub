from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=700)
# Changed the bgcolor to black so it'll be easier on the eyes.
screen.bgcolor("black")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will "
                                  "win the race? Enter a color:")
colors = ["red", "orange", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50]
all_turtles = []


for racer in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[racer])
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y_positions[racer])
    new_turtle.pendown()
    all_turtles.append(new_turtle)


def turn_left():
    new_heading = turtle.heading() + rand_ds
    turtle.setheading(new_heading)


def turn_right():
    new_heading = turtle.heading() - rand_ds
    turtle.setheading(new_heading)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color}turtle is the winner!")
        rand_ds = random.randint(0, 100)
# Have the turtles go in random distance in ziglag line. 
        turtle.fd(rand_ds)
        turn_right()
        turtle.fd(rand_ds)
        turn_left()
        turtle.fd(rand_ds)

screen.exitonclick()
