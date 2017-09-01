import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt
import mpld3


def scatterz(x, y, data, labels, xscale='linear', yscale='linear', n=250):

    fig, ax = plt.subplots(subplot_kw=dict(axisbg='#FFFFFF'), figsize=(10, 10))
    fig.set_size_inches(8, 8)
    data = data.head(n)

    scatter = ax.scatter(data[x],
                         data[y], s=25,
                         alpha=0.5)

    ax.grid(color='white', linestyle='solid')

    if yscale == 'linear':

        yl = data[y].min()
        yh = data[y].max()
        yx = (yh - yl) * 0.035
        yl = yl - yx
        yh = yh + yx
        plt.ylim((yl, yh))

    elif yscale == 'log':

        plt.yscale("log")

    if xscale == 'linear':

        xl = data[x].min()
        xh = data[x].max()
        xx = (xh - xl) * 0.035
        xl = xl - xx
        xh = xh + xx
        plt.xlim((xl, xh))

    elif xscale == 'log':

        plt.xscale("log")

    plt.xlabel(x, fontsize=18, labelpad=15, color="gray")
    plt.ylabel(y, fontsize=18, labelpad=15, color="gray")
    labels = [' {0}'.format(i + str(' ')) for i in data[labels].astype(str)]
    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    return mpld3.display()
