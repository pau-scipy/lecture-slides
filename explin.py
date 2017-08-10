import numpy as np
import matplotlib.pyplot as plt

def gen_linear(m, c):
    """Generates data for y = mx + c"""
    x = np.linspace(0,10)
    y = m * x + c
    return (x, y)

def gen_exponential(a, n):
    """Generates data for y = ax^n"""
    x = np.linspace(0,10)
    y = a * x ** n
    return (x, y)
    
if __name__ == "__main__":
    (x, y) = gen_linear(5, 3)
    plt.plot(x, y, 'b-')
    plt.plot(x, y, 'bv')
    (x, y) = gen_exponential(5, 3)
    plt.plot(x, y, 'r-')
    plt.plot(x, y, 'rv')
    plt.savefig("linexp.png")
    plt.show()
    plt.loglog(x, y, 'r-')
    plt.loglog(x, y, 'rv')
    plt.savefig("loglog.png")
    plt.show()
