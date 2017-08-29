import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def paramagg(data):

    '''
    USE: paramagg(df)

    Provides an overview in one plot for a parameter scan. Useful
    to understand rough distribution of accuracacy and loss for both
    test and train.

    data = a pandas dataframe from hyperscan()
    '''

    plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')

    plt.scatter(data.train_loss, data.train_acc, label='train')
    plt.scatter(data.test_loss, data.test_acc, label='test')

    plt.legend(loc='upper right')
    plt.tick_params(axis='both', which='major', pad=15)

    plt.xlabel('loss', fontsize=18, labelpad=15, color="gray")
    plt.ylabel('accuracy', fontsize=18, labelpad=15, color="gray")

    plt.show()
