import matplotlib.pyplot as plt
import mpld3
import seaborn as sns

plt.style.use('bmh')

def distribution(data):

    plt.figure(figsize=(14, 4))
    plt.xlim(-0.005,1.0)
    sns.kdeplot(data,legend=False)
    sns.despine(right=False)

def accuracy(data):

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

    ax1.plot(data.history['acc'])
    ax1.plot(data.history['val_acc'])
    ax2.plot(data.history['loss'])
    ax2.plot(data.history['val_loss'])

    ax1.set_title('accuracy')
    ax1.set_xlabel('epoch')

    ax2.set_title('loss')
    ax2.set_xlabel('epoch')

    fig.set_size_inches(12,3)

    fig.show() 

def scatterz(x,y,data,labels,xscale='linear',yscale='linear',n=250):

    fig, ax = plt.subplots(subplot_kw=dict(axisbg='#FFFFFF'),figsize=(10, 10))
    fig.set_size_inches(8,8)
    data = data.head(n)

    scatter = ax.scatter(data[x], 
                         data[y],s=25,
                         alpha=0.5)

    ax.grid(color='white', linestyle='solid')

    if yscale == 'linear':
    
        yl = data[y].min()
        yh = data[y].max()
        yx = (yh - yl) * 0.035
        yl = yl - yx
        yh = yh + yx
        plt.ylim((yl,yh))

    elif yscale == 'log':

        plt.yscale("log")

    if xscale == 'linear':
        
        xl = data[x].min()
        xh = data[x].max()
        xx = (xh - xl) * 0.035 
        xl = xl - xx
        xh = xh + xx
        plt.xlim((xl,xh))
        
    elif xscale == 'log':

        plt.xscale("log")
    
    labels = [' {0}'.format(i + str(' ')) for i in data[labels]]
    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    #mpld3.display()

    return mpld3.display()