import numpy as np
import matplotlib

matplotlib.use('Agg')  # this needs to be here for travis build
import matplotlib.pyplot as plt  # not pep8 but will not pass travis otherwise

plt.style.use('bmh')


def trainplot(train_vals, test_vals):

    # creating the x-labels
    train_pos = np.array([1, 2, 3, 4, 5, 6]) * 2
    test_pos = train_pos + 0.55

    label_placeholder = test_pos - .3
    labels = ["acc_max", "acc_min", "acc_median",
              "acc_mean", "acc_midpoint", 'acc_last']

    fig = plt.figure(figsize=(16, 4), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111)

    ax.bar(train_pos, train_vals, width=.5, align='center', label='Train')
    ax.bar(test_pos, test_vals, width=0.5, align='center', label='Test')

    plt.ylim((0, 1))
    plt.tick_params(axis='both', labelsize=11, which='major', pad=10)
    plt.xticks(label_placeholder, labels)
    plt.grid(b=False)
    plt.legend(loc='upper right')

    plt.show()
