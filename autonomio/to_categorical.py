import pandas as pd
from vectorize_text import vectorize_text

def labels_to_int(df,y,max_categories,starts_with_col):
    
    if max_categories == 'auto':
        max_categories = len(df) / 50
    elif max_categories == 'max':
        max_categories = len(df) + 1
    elif type(max_categories) == int:
        max_categories = max_categories
    
    cols_before = df.shape[1]
    
    for col in df.columns:
        try:
            df[col].astype('float')
        except:
            if len(df[col].unique()) < max_categories:
                df[col] = pd.Categorical(df[col]).codes            
            elif starts_with_col != 'none' and starts_with_col == col:
                df[col] = _starts_with_output(df,col)
                    
            else:
                df = df.drop(col,axis=1)
    temp_y = df[y]
    df = df.drop(y,axis=1)
    df.insert(0,y,temp_y)
    
    rows_before = len(df)
    df = df.dropna()
    rows_after = len(df)
    cols_after = df.shape[1]
    
    print str(rows_before - rows_after) + " out of " + str(rows_before) + " rows dropped"
    print str(cols_before - cols_after) + " out of " + str(cols_before) + " columns dropped"
    
    return df

def _category_starts_with(df,col):
    
    '''
    This is called from starts_with_output. 
    
    '''

    if df[col].str.len().mean() < 10:

        out = []
        c = len(df)

        for i in range(c):
            val = str(df[col][i])
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