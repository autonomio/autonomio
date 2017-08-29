import pandas as pd
import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def _create_alpha(data, parameter, limit):

    '''
    Helper function for paramscatter() which
    yields a list of values to be used for alpha (colors).
    '''

    if limit is not 'none':
        len_temp = limit
    else:
        len_temp = len(data[parameter].unique())
    len_temp = 100 / len_temp
    len_temp = range(10, 100, len_temp-1)
    len_temp = pd.Series(len_temp).sort_values(ascending=False)
    out = pd.Series(len_temp) / 100

    return out.values


def paramscatter(data, parameter, limit='none', sort=True):

    '''
    USE: paramscatter(df,'optimizer',limit=5)

    To create a single scatter plot for investigating a single parameter.

    data = pandas dataframe from hyperscan()
    parameter = a column of the dataframe
    limit = number of values to be shown in the plot
    sort = sorts automatically by label based on 'test_acc',
           the default setting is 'True' and can be set to 'False.

    '''

    title = parameter

    plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')

    alpha = _create_alpha(data, parameter, limit)

    marker_count = 0

    if type(parameter) is str:
        if sort is True:
            parameters = data[[parameter, 'test_acc']].groupby(parameter).mean().index.values
        else:
            parameters = data[parameter].unique()
        if limit is not 'none':
            parameters = parameters[:limit]

    for param in parameters:

        temp = data[data[parameter] == param]
        plt.scatter(temp.test_loss, temp.test_acc, edgecolors='black', s=50, linewidths=1, alpha=alpha[marker_count], c='red', label=param)
        marker_count += 1

    plt.title(title, fontsize=23, y=1.03, color="gray")
    plt.legend(loc='upper right')
    plt.tick_params(axis='both', which='major', pad=15)

    plt.xlabel('loss', fontsize=18, labelpad=15, color="gray")
    plt.ylabel('accuracy', fontsize=18, labelpad=15, color="gray")

    plt.show()
