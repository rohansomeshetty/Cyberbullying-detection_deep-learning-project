# Import libraries
from matplotlib import pyplot as plt
import numpy as np


def gen(data, file):
    num = list(data.values())
    names = list(data.keys())
    # num = []
    # names = []

    # Creating plot

    
    fig = plt.figure(figsize=(10, 7))
    plt.pie(num, labels=names)
    plt.savefig(file)

if __name__ == '__main__':
    gen({'jan': 2, 'feb': 2}, 'g2.jpg')