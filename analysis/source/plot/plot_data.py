import yaml
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    CONFIG =  yaml.load(open('config_global.yaml', 'rU'))
    data  = np.genfromtxt('%s/data.csv' % CONFIG['build']['draw_data'], delimiter = ',', skip_header = 1)
    x, y = data[:, 0], data[:, 1]

    color = [math.sqrt(x1 ** 2 + y1 ** 2) for (x1, y1) in zip(x, y)]
    plt.scatter(x, y, s = 1, alpha = 0.5, c = color)
    plt.title('Scatterplot of x, y')
    plt.savefig('%s/plot.eps' % CONFIG['build']['plot'])
    plt.clf()

    plt.hist(x)
    plt.title('Histogram of x')
    plt.savefig('%s/x_histogram.eps' % CONFIG['build']['plot'])
    plt.clf()

    plt.hist(y)
    plt.title('Histogram of y')
    plt.savefig('%s/y_histogram.eps' % CONFIG['build']['plot'])
    plt.clf()

main()
