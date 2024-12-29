import turtle
from turtle import Screen
import pandas

#|------------------------------UI Setup--------------------------------------|
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#|------------------------------Mechanism------------------------------------|
# Load data from CSV containing state names and their coordinates
data = pandas.read_csv("50_states.csv")
whole_list = data.to_dict()
states_list = whole_list["state"]
num_states = len(states_list)
xcor_list = whole_list["x"]
ycor_list = whole_list["y"]

# Initialize the score and answered states
score = 0
answered_states = []

#|------------------------------Game Logic-----------------------------------|
while len(answered_states) < 50:
    # Prompt the user for a state name
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    ).title()

    # Exit the game if the user types "Exit"
    if answer_state == "Exit":
        missing_states = [
            states_list[states] for states in states_list if states not in answered_states
        ]
        # Save missing states to a CSV file for learning later
        new_data = pandas.DataFrame(missing_states, columns=["Missing States"])
        new_data.to_csv("states_to_learn.csv", index=False)

        # Display missing states on the map in purple
        for state_index in range(0, num_states):
            if states_list[state_index] not in answered_states:
                t = turtle.Turtle()
                t.penup()
                t.hideturtle()
                t.color("purple")
                t.goto(xcor_list[state_index], ycor_list[state_index])
                t.write(arg=states_list[state_index], font=("Arial", 10, "normal"))
        break

    # Check if the user's answer is correct and not already answered
    for state_index in range(0, num_states):
        if answer_state == states_list[state_index] and answer_state not in answered_states:
            # Mark the state on the map
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(xcor_list[state_index], ycor_list[state_index])
            t.write(arg=states_list[state_index], font=("Arial", 10, "normal"))

            # Update the score and answered states list
            answered_states.append(answer_state)
            score += 1

# Keep the turtle window open until manually closed
turtle.mainloop()
