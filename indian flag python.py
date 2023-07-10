#!/usr/bin/env python
# coding: utf-8

# In[38]:


import turtle

# Function to draw rectangle
def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.end_fill()

# Function to draw the Indian flag
def draw_indian_flag():
    # Set up the turtle
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-180, 90)
    turtle.pendown()

    # Draw the green rectangle
    draw_rectangle(360, 180, "#138808")

    # Draw the white rectangle
    turtle.goto(-180, 0)
    draw_rectangle(360, 180, "white")

    # Draw the orange rectangle
    turtle.goto(-180, -90)
    draw_rectangle(360, 90, "#FF9933")

    # Draw the blue circle
#     turtle.goto(0, 45)
#     turtle.color("navy")
#     turtle.fillcolor("navy")
#     turtle.begin_fill()
#     turtle.circle(45)
#     turtle.end_fill()

    # Draw 24 spokes
    turtle.penup()
    turtle.goto(-15,-45)
    turtle.pendown()
    turtle.color("Blue")
    turtle.width(3)
    for _ in range(24):
        turtle.forward(45)
        turtle.backward(45)
        turtle.left(15)

    # Hide the turtle
    turtle.hideturtle()

    # Display the flag
    turtle.done()

# Run the function to draw the Indian flag
draw_indian_flag()


# In[ ]:





# In[ ]:




