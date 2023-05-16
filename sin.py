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
    ax.set_ylim([-2, 2])
    plt.legend(loc='upper left')

    # plot the actual function
    plt.plot(x,sin, 'b',label='sin(x)')
    # plot the taylor series
    # for i in range(0,len(exponents)):
    #     plt.plot(x,taylor[i],label=f"taylor{i}")
    plt.plot(x,taylor[len(exponents)-1],label=f"taylor{len(exponents)-1}")

    # show the plot
    plt.show()


# list of values from -5 to 5 in steps of 0.1
x = np.linspace(-20*np.pi,20*np.pi,1000)
# actual sin function   
sin = np.sin(x)
# how many terms to use in the taylor series
max_degree = 100

# start with positive sign
sign = 1
# list of odd exponents
exponents = [a for a in range(0,max_degree) if a%2!=0]
# list of taylor series
taylor = [0]*len(exponents)
# calculate the taylor series
for i in range(0,len(exponents)):
    e = exponents[i]
    if i > 0:
        taylor[i] = taylor[i-1] + sign * (x**e)/np.math.factorial(e)
    else:
        taylor[i] = sign * (x**e)/np.math.factorial(e)
    sign *= -1

# plot fubctions
plot()