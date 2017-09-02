import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def accuracy(data):

    '''Training Accuracy Plot

    WHAT: A plot for showing convergence between test and train for both
    accuracy metric and loss.

    HOW: accuracy(history)

    INPUT: a pandas dataframe that is created from Keras history object.

    OUTPUT: a pyplot line graph (x2) in a subplot.

    '''

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

    ax1.plot(data['train_acc'])
    ax1.plot(data['test_acc'])
    ax2.plot(data['train_loss'])
    ax2.plot(data['test_loss'])

    ax1.set_title('accuracy')
    ax1.set_xlabel('epoch')

    ax2.set_title('loss')
    ax2.set_xlabel('epoch')

    plt.ylim((0, 1))

    fig.set_size_inches(20, 5)
    fig.savefig('train.png', dpi=300, bbox_inches='tight')
    fig.show()


def prediction_distribution(x, bins):

    '''Training Accuracy Plot

    WHAT: a plot for showing prediction distribution for train().

    NOTE: this is used by both predictor() and train()

    '''

    plt.figure(num=None, figsize=(16, 4), dpi=80, facecolor='w', edgecolor='k')
    plt.hist(x, bins=bins, label='prediction')
    plt.grid(b=False)
    plt.tick_params(axis='both', labelsize=11, which='major', pad=10)
    plt.legend()
    plt.show()
