from memory_profiler import profile
from autonomio.commands import train, data

%load_ext memory_profiler


def train_peak_memory(cycles,hyperscan=True):

    '''Peak Memory Profiler

    Performs a peak memory test in a loop for the
    train() function.

    OPTIONS: hyperscan mode is 'True' (default) or 'False'

    '''
    
    temp = data('parties_and_employment')

    for i in range(cycles):
        if hyperscan is True:
            %memit train([1,7],'PERUSS', temp, epoch=50, hyperscan=True)
        else:
            %memit train([1,7],'PERUSS', temp, epoch=50, hyperscan=False)
