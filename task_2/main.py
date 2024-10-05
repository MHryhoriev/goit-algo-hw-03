import turtle

def koch_curve(t, order, size):
    """
    Draws a Koch curve using a turtle.

    Parameters:
    t (turtle.Turtle): The turtle object used to draw the curve.
    order (int): The order of the Koch curve. A higher order 
                 results in a more detailed curve.
    size (float): The length of the line segment to be drawn.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    """
    Sets up the turtle environment to draw a Koch snowflake.

    Parameters:
    order (int): The order of the Koch curve. Higher values will 
                 produce a more intricate snowflake.
    size (float, optional): The length of each side of the snowflake. 
                            Defaults to 300.
    """
    window = turtle.Screen()
    window.bgcolor('white')

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    input_value = input("Enter the recursion depth (default is 3): ")

    if not input_value:
        recursion_depth = 3
    try:
        recursion_depth = int(input_value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    draw_koch_curve(recursion_depth)

if __name__ == "__main__":
    main()