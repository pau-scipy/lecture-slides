import matplotlib.pyplot as plt
import csv
import datetime


def get_data_from_file(filename, dates, heights):
    format = "%Y-%m-%dT%H:%M:00Z"
    with open(filename,'r') as f:
        csvreader = csv.reader(f)
        next(csvreader) # throw away header line
        next(csvreader) # throw away second header line
        for row in csvreader:
            thedatetime = row[1]
            height = float(row[2])
            dt = datetime.datetime.strptime(thedatetime, format)
            dates.append(dt)
            heights.append(height)

def plot_tides(dates, heights):
    plt.plot(dates, heights, 'c-')
    plt.ylabel("Height in m")
    plt.gcf().autofmt_xdate()
    plt.savefig("tides.png")

if __name__ == "__main__":
    dates = []
    heights = []
    # Castletownbere file
    get_data_from_file("IrishNationalTideGaugeNetwork_6b1b_95a2_06e9.csv", dates, heights)

    # Or try the Dublin Port file
    #get_data_from_file("IrishNationalTideGaugeNetwork_f432_a0a0_bc0e.csv", dates, heights)
    plot_tides(dates,heights)
