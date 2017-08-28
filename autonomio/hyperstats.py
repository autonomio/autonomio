def hyper_descriptive(data, tiers, metric, mode='median', ascending=False):

    '''
    data = the datafile with the results from hyperscan()

    tiers = a string or a list where first tier is first and so

    metric = the metric that will be measured against

    mode = 'mean', 'median', 'std', 'min', or 'max'

    ascending = default is 'False' (can also be True)
    '''

    data[metric] = data[metric].astype(float)
    
    if type(tiers) is str:
        cols = [tiers, metric]
        tiers = [tiers]
    else:
        cols = tiers + [metric]

    temp = data[cols]
    temp = temp.groupby(tiers)

    if mode is 'mean':
        temp = temp.mean()
    if mode is 'median':
        temp = temp.median()
    if mode is 'std':
        temp = temp.std()
    if mode is 'min':
        temp = temp.min()
    if mode is 'max':
        temp = temp.max()

    out = temp.sort_values(metric, ascending=ascending)

    return out
