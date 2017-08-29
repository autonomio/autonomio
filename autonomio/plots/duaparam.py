import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def duaparam(data, column, val_1, val_2):

    '''
    Draws out two plots side-by-side, both showing
    test and train accuracy and loss as a scatter plot.

    data = the pandas dataframe from hyperscan()

    column = which column to use for the parameters to be compared

    val_1 = the left side plots value (must be in the parameter column)

    val_2 = the right side plots value (must be in the parameter column)

    '''

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex=True, sharey=True)

    temp = data[data[column] == val_1]
    ax1.set_title(val_1)
    ax1.scatter(temp.train_loss, temp.train_acc, label='train')
    ax1.scatter(temp.test_loss, temp.test_acc, label='test')
    ax1.legend(loc='upper right')
    ax1.tick_params(axis='both', which='major', pad=15)
    ax1.set_xlim([0, 1])
    ax1.set_ylim([0, 1])

    temp = data[data[column] == val_2]
    ax2.set_title(val_2)
    ax2.scatter(temp.train_loss, temp.train_acc, label='train')
    ax2.scatter(temp.test_loss, temp.test_acc, label='test')
    ax2.legend(loc='upper right')
    ax2.tick_params(axis='both', which='major', pad=15)

    fig.text(0.5, -0.02, 'loss', ha='center', va='center', size=17, color='grey')
    fig.text(-0.02, 0.5, 'accuracy', ha='center', va='center', rotation='vertical', size=17, color='grey')

    plt.tight_layout()
    plt.show()
