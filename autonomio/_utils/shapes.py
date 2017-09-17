import math


def shapes(para):

    layers = para['layers']
    shape = para['shape']
    neuron_max = para['neuron_max']
    neuron_last = para['neuron_last']

    neuron_previous = neuron_max
    neuron_count = []
    l = []

    if shape == 'funnel':

        l = []
        for x in [2, 3, 4]:
            l.append(x)

        for i in range(layers - 3):
            n = 2 * l[i + 2] - l[i]
            l.append(n)
        l = l[::-1]

        for i in range(layers):
            neuron_count.append(l[i])

    if shape == 'rhombus':

        neuron_count.append(1)

        a = neuron_max * 2 - 1
        k = 0

        if a < layers:
            k = layers - a
            val = layers - k

        else:
            val = layers

        if (val % 2) == 0:

            n = (val - 2) / 2  # number of layers before or after middle layer

            for i in range(n):
                neuron_count.append(int(neuron_max * (i+1) * 2 / val))

            l = neuron_count[::-1]
            neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(l[i])

        else:
            n = (val - 1) / 2

            for i in range(n - 1):
                neuron_count.append(int(neuron_max * (3 + 2 * i) / val))

            l = neuron_count[::-1]
            neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(l[i])

        if k != 0:
            for i in range(k):
                neuron_count.append(1)

    if shape == 'long_funnel':

        n = layers / 2
        l = []

        if (layers % 2 == 0):
            for i in range(n - 1):
                neuron_count.append(neuron_max)

        elif (layers % 2 == 1):
            for i in range(n):
                neuron_count.append(neuron_max)

        for x in [2, 3, 4]:
            l.append(x)

        for i in range(n - 2):
            n2 = 2 * l[i + 2] - l[i]
            l.append(n2)
        l = l[::-1]

        for i in range(n + 1):
            if l[i] >= neuron_max:
                neuron_count.append(neuron_max)
            else:
                neuron_count.append(l[i])

    if shape == 'brick':

        for i in range(layers):
            neuron_count.append(neuron_max)

    if shape == 'diamond':

        n = layers / 2
        neuron_first = int(math.ceil(.5 * neuron_max))
        l = []

        step = neuron_first / n

        if step is 0:
            step = 1

        if (layers % 2 == 0):
            for i in range(n - 1):
                n2 = neuron_first + i * step
                if n2 <= neuron_max:
                    neuron_count.append(n2)
                else:
                    neuron_count.append(neuron_max)

        else:
            for i in range(n):
                n2 = neuron_first + i * step
                if n2 <= neuron_max:
                    neuron_count.append(n2)
                else:
                    neuron_count.append(neuron_max)

        neuron_count.append(neuron_max)

        step2 = (neuron_max - 2) / float(n)

        if int(step2) is 0:
            step2 = 1

        for i in range(n):
            n2 = int(round(2 + i * step2))
            if n2 <= neuron_max:
                l.append(n2)
            else:
                l.append(neuron_max)
        l = l[::-1]

        for i in range(n):
            neuron_count.append(l[i])

    if shape == 'hexagon':

        neuron_first = 2
        n = layers / 3
        step = int(math.ceil((neuron_max - neuron_first) / n))

        if step is 0:
            step = 1

        if (layers == 4):
            neuron_count.append(neuron_first)
            for i in range(layers - 1):
                neuron_count.append(neuron_max)

        else:
            for i in range(n):
                n2 = neuron_first + i * step
                if n2 <= neuron_max:
                    neuron_count.append(n2)
                else:
                    neuron_count.append(neuron_max)
            temp = neuron_count[::-1]

            if (layers % 3 == 0):
                for i in range(n):
                    neuron_count.append(neuron_max)

            if (layers % 3 == 1):
                for i in range(n+1):
                    neuron_count.append(neuron_max)

            if (layers % 3 == 2):
                for i in range(n+2):
                    neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(temp[i])

    if shape == 'triangle':

        neuron_first = 2
        step = (neuron_max - neuron_first) / float(layers)

        if int(step) is 0:
            step = 1

        for i in range(layers - 1):
            n2 = int(round(neuron_first + i * step))
            if n2 <= neuron_max:
                neuron_count.append(n2)
            else:
                neuron_count.append(neuron_max)

        neuron_count.append(neuron_max)

    if shape == 'pyramid':

        neuron_first = 2
        step = (neuron_max - neuron_first) / float(layers)
        l = []

        if int(step) is 0:
            step = 1

        for i in range(layers - 1):
            n2 = int(round(neuron_first + i * step))
            if n2 <= neuron_max:
                l.append(n2)
            else:
                l.append(neuron_max)

        l.append(neuron_max)
        l = l[::-1]

        for i in range(layers):
            neuron_count.append(l[i])

    if shape == 'stairs':

        n = layers / 2
        step = (neuron_max - 2) / float(n)

        if layers % 2 == 0:
            for i in range(n):
                for j in range(2):
                    n2 = int(neuron_max - i * step)
                    neuron_count.append(n2)
        else:
            neuron_count.append(neuron_max)
            for i in range(n):
                for j in range(2):
                    n2 = int(neuron_max - i * step)
                    neuron_count.append(n2)

    for i in range(len(neuron_count)):
        if neuron_count[i] is 1:
            neuron_count[i] = 2

    return neuron_count

# Returns a List
