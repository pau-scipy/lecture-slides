"""Example of turtle drawing in Python"""

import turtle

def draw_shape(t,n):
    """Draws a polygon with n sides"""
    angle = 360 / n
    for i in range(n):      # Draw the polygon
        t.forward(40)
        t.left(angle)


def main():
    try:
        t = turtle.Turtle()
    except turtle.Terminator:
        print("Sorry, couldn't make a turtle window and turtle")
    else:
        t.width(4)
        draw_shape(t,5)
        draw_shape(t,6)
        draw_shape(t,7)
    finally:
        turtle.exitonclick()
        
if __name__ == "__main__":
    main()
    