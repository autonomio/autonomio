import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt

plt.style.use('bmh')


def lstm_plot(predicted_data, true_data, prediction_len=None):

    fig = plt.figure(facecolor='white', figsize=(16, 4))
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.tick_params(axis='both', which='major', pad=15)

    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.show()


def histplot(x, y, bins=50):

    fig = plt.figure(num=None, figsize=(16, 4), dpi=80, facecolor='w', edgecolor='k')
    plt.hist(y, bins=bins, label='actual');
    plt.hist(x, bins=bins, label='prediction', alpha=.8);
    plt.grid(b=False)
    plt.tick_params(axis='both', which='major', pad=15)
    plt.legend()
    plt.show()
