import math as m


def shapes(para):

    layers = para['layers']
    shape = para['shape']
    neuron_max = para['neuron_max']
    neuron_last = para['neuron_last']

    neuron_previous = neuron_max
    neuron_count = []
    l = []
    
    if shape == 'funnel':

        neuron_count.append(neuron_max)

        for i in range(layers - 1):
            neuron_count.append((neuron_previous + neuron_last) / 2)
            neuron_previous = neuron_count[i+1]

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

        if (layers % 2 == 0):

            for i in range(n):
                neuron_count.append(neuron_max)

        elif (layers % 2 == 1):

            for i in range(n + 1):
                neuron_count.append(neuron_max)

        for i in range(n):
            neuron_count.append((neuron_previous + neuron_last) / 2)
            neuron_previous = neuron_count[i + n]

    if shape == 'brick':

        for i in range(layers):
            neuron_count.append(neuron_max)

    if shape == 'diamond':

        n = layers / 2

        if (layers % 2 == 0):

            for i in range(n - 1):
                neuron_count.append(int(m.ceil(neuron_max * layers + i) / 2.0) / (layers - 1))
            neuron_count.append(neuron_max)

        else:

            for i in range(n):
                neuron_count.append(int(m.ceil(neuron_max * layers + i) / 2.0) / (layers - 1))
            for i in range(1):
                neuron_count.append(neuron_max)

        for i in range(n):
            neuron_count.append((neuron_previous + neuron_last) / 2)
            neuron_previous = neuron_count[i + n]

    if shape == 'hexagon':

        neuron_count.append(1)

        if (layers == 4):
            for i in range(layers - 1):
                neuron_count.append(neuron_max)

        else:

            n = layers / 3

            for i in range(n):
                l.append((neuron_previous + neuron_last) / 2)
                neuron_previous = l[i]

            l = l[::-1]

            if (layers % 3 == 0):

                for i in range(n - 1):
                    neuron_count.append(l[i])

            if (layers % 3 == 1):

                for i in range(n):
                    neuron_count.append(l[i])

            if (layers % 3 == 2):

                for i in range(n):
                    neuron_count.append(l[i])

                neuron_count.append(neuron_max)

            l = l[::-1]

            for i in range(n):
                neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(l[i])

    if shape == 'triangle':

        neuron_count.append(1)

        for i in range(layers - 2):
            l.append((neuron_previous + neuron_last) / 2)
            neuron_previous = l[i]

        l = l[::-1]

        for i in range(layers - 2):
            neuron_count.append(l[i])

        neuron_count.append(neuron_max)

    if shape == 'stairs':

        if (layers >= 5):
            if (layers % 2 == 1):
                neuron_count.append(neuron_max)

            else:
                for i in range(2):
                    neuron_count.append(neuron_max)

            n = layers / 2

            for i in range(n):
                if neuron_previous >= 3:
                    neuron_previous -= 2
                for j in range(2):
                    neuron_count.append(neuron_previous)

        else:
            for i in range(layers):
                neuron_count.append(neuron_previous)
                neuron_previous -= 1

    return neuron_count

# Returns a List