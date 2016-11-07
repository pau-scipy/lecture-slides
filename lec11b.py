"""Another Example of turtle drawing in Python"""

import turtle

# Define functions that will make specific moves
def turn_left(t):
    t.left(45)

def turn_right(t):
    t.right(45)
        
def move_forward(t):
    t.forward(10)

# Define a dictionary that provides a specific move function 
# for each character
rules = {'f':move_forward, 'r':turn_right, 'l':turn_left}


def run_sequence(t, instruction_string):
    for i in instruction_string:
        rules[i](t)


def main():
    try:
        t = turtle.Turtle()
    except turtle.Terminator:
        print("Sorry, couldn't make a turtle window and turtle")
    else:
        t.width(5)
        run_sequence(t,"llfffffffffrrffffrrffffrrffff")
    finally:
        turtle.exitonclick()
      
      
if __name__ == "__main__":
    main()
    
