import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def accuracy(data):

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
