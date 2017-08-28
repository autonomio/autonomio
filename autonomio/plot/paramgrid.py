import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def paramgrid(data, col, col_count=4):

    '''

    USE: paramgrid(df,'loss')

    This plot is especially useful for investigating
    more than a few values at one go. For example if you
    want to see 16 different layer settings in one figure.

    data = pandas dataframe from hyperscan()
    col = the parameter column
    col_count = how many columns per row

    '''

    uniques = len(data[col].unique())

    if uniques is 1:
        print ("ERROR: column has only one unique item")

    if uniques < 4:
        col_count = uniques

    row_modulus = uniques % col_count
    row_count = uniques / col_count

    if row_modulus is not 0:
        row_count = row_count + 1

    fig, axs = plt.subplots(row_count,
                            col_count,
                            figsize=(16, row_count*4),
                            sharex=True,
                            sharey=True)

    axs = axs.ravel()

    for i in range(uniques):

        item = data[col].unique()[i]
        temp = data[data[col] == item]
        axs[i].scatter(temp.train_loss, temp.train_acc, label='train')
        axs[i].scatter(temp.test_loss, temp.test_acc, label='test')
        axs[i].set_title(item)
        axs[i].tick_params(axis='both', which='major', pad=15)

    for i in range(uniques, row_count*col_count):
        fig.delaxes(axs[i])

    fig.text(0.07,
             0.5,
             'x(loss)     y(accuracy)',
             ha='center',
             va='center',
             rotation='vertical',
             size=17,
             color='grey')
