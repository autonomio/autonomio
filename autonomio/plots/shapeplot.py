import matplotlib
matplotlib.use('Agg')  # this needs to be here exceptionslly
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from autonomio.transforms.rescale import max_rescale

plt.style.use('bmh')


def shapeplot(shape, model='mlp'):

    '''Network Topology Graph

    WHAT: visualises the topology of a network together with
    labels and neuron counts for each layer.

    HOW: shapeplot(shape_object,model_name)

    INPUT: Autonomio shape object from train() which is a list of ints.

    OUTPUT: a graphical presentation of the shape of the network.

    '''

    if model == 'mlp':
        layer_type = 'Dense'

    if model == 'lstm':
        layer_type = 'lstm'

    if model == 'regression':
        layer_type = 'Dense'

    dot_size = .1
    max_dots = 12
    dot_pad = .4
    fig_height = 4
    shape.reverse()
    org_values = shape
    shape = max_rescale(shape, scale=max_dots, to_int=True)

    font_size = 15 - (len(shape) / 4)

    fig1 = plt.figure(1, figsize=(10, 4))

    ax = fig1.add_axes([0, 0, 1, 1], frameon=False, aspect=1.)

    height_multiplier = len(shape) / 10.0

    ax.set_xlim(-0.1, fig_height * 2)
    ax.set_ylim(-0.3, fig_height * height_multiplier)

    # whole structure level loop
    for layer in range(len(shape)):
        if layer == 0:
            layer_pos = layer
        else:
            layer_pos += dot_pad

        # layer level loop
        for i in range(shape[layer]):
            if i == 0:
                circle_pos = i + ((max_dots - shape[layer]) * dot_pad / 2)
            else:
                circle_pos += dot_pad

            # adding the circle elmement in to the plot
            ax.add_patch(mpatches.Circle((circle_pos, layer_pos),
                         dot_size, alpha=.6,))

            # input and connected layers
            if layer != len(shape)-(len(shape)):
                ax.annotate(layer_type + " " + str(org_values[layer]),
                            (6, layer_pos),
                            color='grey',
                            size=font_size)
            # output layer
            else:
                ax.annotate('Dense' + " " + str(org_values[layer]),
                            (6, layer_pos),
                            color='grey',
                            size=font_size)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    plt.draw()
    plt.show()
