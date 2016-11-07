"""
docexample is an example of a python module with documentation
"""

import sys

def print_list_to_stdout(mylist):
    """This function prints elements of a list to stdout.
    
    No result is returned.
    Each element of the list will be converted to a string.
    Newlines will separate the elements."""
    for x in mylist:
        sys.stdout.write("printing: " + str(x) + "\n")

        
def add_them(i,j):
    """This function will add i and j together and return the result.
    """
    return (i+j)

    
def multiply_them(i,j):
    """This function will multiply its two arguments.
    
    It will then return the result.
    
    Parameters
    ----------
    
    i : int
        The first number to be multiplied
    j : int
        The second number
    """
    return (i*j)

    
def ten_times(i):
    """ten_times will multiply its argument by 10 and return the result."""
    return (i*10)


def main():
    """Code to test the module."""
    x = 1
    y = 3
    a = add_them(x,y)
    print(a)
    m = multiply_them(x,y)
    print(m)
    t = ten_times(x)
    print(t)
    z = add_them(t,y)
    print_list_to_stdout([x,y,z,a,m,t])


if __name__ == "__main__":
    main()
