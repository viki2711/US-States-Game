import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle_pen = turtle.Turtle()
turtle_pen.hideturtle()

guess_list = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while len(guess_list) <= 50:
    # title() converts the str to camel case
    answer_state = screen.textinput(title=f"{len(guess_list)}/50 states", prompt="What's another state name?").title()
    state_row = data[data.state == answer_state]

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if len(state_row) != 0 and answer_state not in guess_list:
        guess_list.append(answer_state)
        turtle_pen.penup()
        turtle_pen.goto(float(state_row.x), float(state_row.y))
        turtle_pen.pendown()
        turtle_pen.write(arg=answer_state, align="center")

# turtle.mainloop()
# We have the coordinates in the csv file, so no need to get hold of them via screen
# def get_mouse_click_coord(x, y):
#     print(x, y)
# passing the x, y coordinates to the function to get hold of them
# turtle.onscreenclick(get_mouse_click_coord)

# we don't need to exit on click, we need the click to play
# screen.exitonclick()