import pandas as pd

from vectorize_text import vectorize_text
from nan_handler import nan_dropper, nan_filler


def labels_to_ints(data, y, max_categories, starts_with_col, treshold, first_fill_cols, fill_with):
    
    if max_categories == 'auto':
        max_categories = len(data) / 50
    elif max_categories == 'max':
        max_categories = len(data) + 1
    elif type(max_categories) == int:
        max_categories = max_categories
    
    cols_before = data.shape[1]
    rows_before = len(data)

    if first_fill_cols != None:

        data[first_fill_cols] = nan_filler(data, first_fill_cols, fill_with)

    if treshold != 0:

        data = nan_dropper(data, treshold)
    
    for col in data.columns:
        try:
            data[col].astype('float')
        except ValueError:

            if len(data[col].unique()) < max_categories:
                data[col] = pd.Categorical(data[col]).codes            

            # initiates conversion to labels based on first character
            elif starts_with_col != 'none' and starts_with_col == col:
                data[col] = _starts_with_output(data,col)
                    
            else:
                data = data.drop(col,axis=1)
    if y is not 'none':
        temp_y = data[y]
        data = data.drop(y, axis=1)
        data.insert(0, y, temp_y)

    rows_before = len(data)
    rows_after = len(data)
    cols_after = data.shape[1]
    
    print(str(rows_before - rows_after) + " out of " + str(rows_before) + " rows dropped")
    print(str(cols_before - cols_after) + " out of " + str(cols_before) + " columns dropped")
    
    return data

def _category_starts_with(data,col):
    
    '''
    This is called from starts_with_output. 
    
    '''
    # filters out columns with long string values

    if data[col].str.len().mean() < 10:

        out = []
        c = len(data)

        for i in range(c):
            val = str(data[col][i])
            temp = []
            temp += val
            out += temp[0]

        return pd.DataFrame(pd.Series(out).unique()).reset_index()
    
def _starts_with_output(data,col):
    
    '''
    
    Helper function for to_integers in cases where
    the feature is categorized based on a common 
    first character of a string.
    
    '''

    data[col] = data[col].fillna('0')
    temp_df = _category_starts_with(data,col)
    temp_df['start_char'] = temp_df[0]
    temp_df = temp_df.drop(0,axis=1)
    reference_df = temp_df.set_index('start_char').transpose()
    temp_list = []
    for i in range(len(data[col])):
        for c in temp_df['start_char']:
            if data[col][i].startswith(c) == True:
                temp_list.append(reference_df[c][0])
    if len(data[col]) != len(temp_list):
        print "AUTONOMIO ERROR: length of input and output do not match"
    else: 
        return pd.Series(temp_list)

## Returns a dataframe
