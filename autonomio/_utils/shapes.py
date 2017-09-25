from autonomio._utils.get_method import get_method

import math


def shapes(para):

    '''Shapes

    WHAT: function that creates a list of neurons
    according to a chosen shape.
    '''

    neuron_count = []

    shape = get_method(para['shape'], mode='shapes')
    neuron_count = shape(para, neuron_count)

    for i in range(len(neuron_count)):
        if neuron_count[i] is 1:
            neuron_count[i] = 2

    return neuron_count

# Returns a List


def funnel(para, neuron_count):

    l = []
    for x in [2, 3, 4]:
        l.append(x)

    for i in range(para['layers'] - 3):
        n = 2 * l[i + 2] - l[i]
        l.append(n)
    l = l[::-1]

    for i in range(para['layers']):
        neuron_count.append(l[i])

    return neuron_count


def brick(para, neuron_count):

    for i in range(para['layers']):
        neuron_count.append(para['neuron_max'])

    return neuron_count


def triangle(para, neuron_count):

    neuron_first = 2
    step = (para['neuron_max'] - neuron_first) / float(para['layers'])

    if int(step) is 0:
        step = 1

    for i in range(para['layers'] - 1):
        n2 = int(round(neuron_first + i * step))
        if n2 <= para['neuron_max']:
            neuron_count.append(n2)
        else:
            neuron_count.append(para['neuron_max'])

    neuron_count.append(para['neuron_max'])

    return neuron_count


def pyramid(para, neuron_count):

    neuron_first = 2
    step = (para['neuron_max'] - neuron_first) / float(para['layers'])
    l = []

    if int(step) is 0:
        step = 1

    for i in range(para['layers'] - 1):
        n2 = int(round(neuron_first + i * step))
        if n2 <= para['neuron_max']:
            l.append(n2)
        else:
            l.append(para['neuron_max'])

    l.append(para['neuron_max'])
    l = l[::-1]

    for i in range(para['layers']):
        neuron_count.append(l[i])

    return neuron_count


def rhombus(para, neuron_count):

    neuron_count.append(1)

    a = para['neuron_max'] * 2 - 1
    k = 0
    l = []

    if a < para['layers']:
        k = para['layers'] - a - 1
        val = para['layers'] - k

    else:
        val = para['layers']

    if (val % 2) == 0:

        # number of layers before or after middle layer
        n = (val - 2) / 2

        for i in range(n):
            neuron_count.append(int(para['neuron_max'] * (i+1) * 2 / val))

        l = neuron_count[::-1]
        neuron_count.append(para['neuron_max'])

        for i in range(n):
            neuron_count.append(l[i])

    else:
        n = (val - 1) / 2

        for i in range(n - 1):
            neuron_count.append(int(para['neuron_max'] * (3 + 2 * i) / val))

        l = neuron_count[::-1]
        neuron_count.append(para['neuron_max'])

        for i in range(n):
            neuron_count.append(l[i])

    if k != 0:
        for i in range(k):
            neuron_count.append(1)

    return neuron_count


def long_funnel(para, neuron_count):

    n = para['layers'] / 2
    l = []

    if (para['layers'] % 2 == 0):
        for i in range(n - 1):
            neuron_count.append(para['neuron_max'])

    elif (para['layers'] % 2 == 1):
        for i in range(n):
            neuron_count.append(para['neuron_max'])

    for x in [2, 3, 4]:
        l.append(x)

    for i in range(n - 2):
        n2 = 2 * l[i + 2] - l[i]
        l.append(n2)
    l = l[::-1]

    for i in range(n + 1):
        if l[i] >= para['neuron_max']:
            neuron_count.append(para['neuron_max'])
        else:
            neuron_count.append(l[i])

    return neuron_count


def diamond(para, neuron_count):

    n = para['layers'] / 2
    neuron_first = int(math.ceil(.5 * para['neuron_max']))
    l = []

    step = neuron_first / n

    if step is 0:
        step = 1

    if (para['layers'] % 2 == 0):
        for i in range(n - 1):
            n2 = neuron_first + i * step
            if n2 <= para['neuron_max']:
                neuron_count.append(n2)
            else:
                neuron_count.append(para['neuron_max'])

    else:
        for i in range(n):
            n2 = neuron_first + i * step
            if n2 <= para['neuron_max']:
                neuron_count.append(n2)
            else:
                neuron_count.append(para['neuron_max'])

    neuron_count.append(para['neuron_max'])

    step2 = (para['neuron_max'] - 2) / float(n)

    if int(step2) is 0:
        step2 = 1

    for i in range(n):
        n2 = int(round(2 + i * step2))
        if n2 <= para['neuron_max']:
            l.append(n2)
        else:
            l.append(para['neuron_max'])
    l = l[::-1]

    for i in range(n):
        neuron_count.append(l[i])

    return neuron_count


def hexagon(para, neuron_count):

    neuron_first = 2
    n = para['layers'] / 3
    step = int(math.ceil((para['neuron_max'] - neuron_first) / n))

    if step is 0:
        step = 1

    if (para['layers'] == 4):
        neuron_count.append(neuron_first)
        for i in range(para['layers'] - 1):
            neuron_count.append(para['neuron_max'])

    else:
        for i in range(n):
            n2 = neuron_first + i * step
            if n2 <= para['neuron_max']:
                neuron_count.append(n2)
            else:
                neuron_count.append(para['neuron_max'])
        temp = neuron_count[::-1]

        if (para['layers'] % 3 == 0):
            for i in range(n):
                neuron_count.append(para['neuron_max'])

        if (para['layers'] % 3 == 1):
            for i in range(n+1):
                neuron_count.append(para['neuron_max'])

        if (para['layers'] % 3 == 2):
            for i in range(n+2):
                neuron_count.append(para['neuron_max'])

        for i in range(n):
            neuron_count.append(temp[i])

    return neuron_count


def stairs(para, neuron_count):

    n = para['layers'] / 2
    step = (para['neuron_max'] - 2) / float(n)

    if para['layers'] % 2 == 0:
        for i in range(n):
            for j in range(2):
                n2 = int(para['neuron_max'] - i * step)
                neuron_count.append(n2)
    else:
        neuron_count.append(para['neuron_max'])
        for i in range(n):
            for j in range(2):
                n2 = int(para['neuron_max'] - i * step)
                neuron_count.append(n2)

    return neuron_count
