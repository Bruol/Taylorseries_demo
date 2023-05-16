import matplotlib.pyplot as plt
from cycler import cycler
import numpy as np


def plot():
    # set up the plot
    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y']) +
                            cycler('linestyle', ['-', '--', ':', '-.'])))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_ylim([-20, 20])

    # plot the actual function
    plt.plot(x,exp, 'b',label='exp(x)')
    # plot the taylor series
    for i in range(0,len(exponents)):
        plt.plot(x,taylor[i],label=f"taylor{i}")

    #plt.legend(loc='upper left')

    # show the plot
    plt.show()


# list of values from -5 to 5 in steps of 0.1
x = np.linspace(-20*np.pi,20*np.pi,1000)
# actual sin function   
exp = np.exp(x)
# how many terms to use in the taylor series
max_degree = 50


# list of odd exponents
exponents = [a for a in range(0,max_degree)]
# list of taylor series
taylor = [0]*len(exponents)
# calculate the taylor series
for i in range(0,len(exponents)):
    e = exponents[i]
    if i > 0:
        taylor[i] = taylor[i-1] + (x**e)/np.math.factorial(e)
    else:
        taylor[i] = (x**e)/np.math.factorial(e)

# plot fubctions
plot()