import matplotlib.pyplot as plt
import csv

def read_data(filename):
    """Read x, y and description from 3 cols of a CSV"""
    x = []
    y = []
    labels = []
    with open(filename) as f:
        csvr = csv.reader(f)
        for row in csvr:
            x.append(float(row[0]))
            y.append(float(row[1]))
            labels.append(row[2])
    return(x,y,labels)


def make_plot(x,y,labels):
    """Plot x against log y, with label annotations for each point"""
    plt.semilogy(x,y,'b-')
    plt.semilogy(x,y,'bv')
    plt.xlabel("Richter scale")
    plt.ylabel("Appox equivalent kg of TNT")
    plt.grid(True, axis='y')
    
    # Add the labels, shifted across a little on the x axis
    for (x1, y1, l) in zip(x, y, labels):
        plt.annotate(l, xy=(x1, y1), xytext=(x1+0.2, y1) )

    plt.savefig("richter.png", bbox_inches='tight')
    plt.show()

    
if __name__ == "__main__":
    (x,y,labels) = read_data("richter.csv")
    make_plot(x,y,labels)
