import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')

def quadparam(data, x, y, size, color, title='auto'):

    '''

    USE: quadparam(df,'layers','batch_size','test_acc','test_loss')

    Used for taking in 4 different parameters, where 'x'
    and 'y' are for the axis, and then 'size' and 'color'
    are for adding another two dimesions.

    data = pandas dataframe coming from hyperscan()
    x = should be numeric (one of the columns in data)
    y = should be numeric
    size = should be numeric
    color = should be numeric
    title = a string to be used as the title of the plot.
            The default is 'auto' that generates a title
            based on the inputs.
    '''

    if title is 'auto':

        title = x + ' & ' + y + ' correlation'

    fig = plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')

    s_label = size
    c_label = color

    temp = np.array(data[size].astype(float))
    temp *= (500 / temp.max())
    s = temp

    color = data[color]**data[color]

    plt.scatter(data[x], data[y], edgecolors='black', cmap='coolwarm', s=s, c=color)
    plt.tick_params(axis='both', which='major', pad=15)

    plt.title(title, fontsize=23, y=1.09, color="gray")
    plt.suptitle("size = " + s_label + " || " "hue = " + c_label,
                 verticalalignment='top',
                 fontsize=16,
                 y=.93,
                 x=0.52,
                 color="gray")
    plt.xlabel(x, fontsize=18, labelpad=15, color="gray")
    plt.ylabel(y, fontsize=18, labelpad=15, color="gray")

    plt.tick_params(axis='both', which='major', pad=25)
    plt.grid(b=False)
    plt.show()