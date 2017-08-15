import pandas as pd
import pkg_resources
from col_name_generator import col_name_generator

data_path = 'https://github.com/autonomio/datasets/raw/master/autonomio-datasets/'

def load_data(name, mode, sep, delimiter, header):

    try:

        if mode == 'default':
        
            if name == 'election_in_twitter':
                out = pd.read_msgpack(data_path+'election_in_twitter')
            if name == 'sites_category_and_vec':
                out = pd.read_msgpack(data_path+'sites_category_and_vec')
            if name == 'programmatic_ad_fraud':
                out = pd.read_msgpack(data_path+'programmatic_ad_fraud')
            if name == 'parties_and_employment':
                out = pd.read_msgpack(data_path+'parties_and_employment')
            if name == 'tweet_sentiment':
                out = pd.read_msgpack(data_path+'tweet_sentiment')
            if name == 'random_tweets':
                out = pd.read_msgpack(data_path+'random_tweets')
            if name == 'kaggle_titanic_train':
                out = pd.read_csv(data_path+'kaggle_titanic_train.csv')
            
            
            return out
                
        elif mode == 'file':
            
            if name.endswith('.csv') or name.endswith('.txt'):
                
                try:
                    out = pd.read_csv(name,sep,delimiter,header)
                except:
                    out = pd.read_csv(name,sep,delimiter,header,error_bad_lines=False)
            
            elif name.endswith('.msgpack'):
                out = pd.read_msgpack(name)
            
            elif name.endswith('.json'):
                out = pd.read_json(name)
            
            else: 

                out = ''
                print("MAYBE UNSUPPORTED? only csv/txt, json, and msgpack")
            
            # Convert number column names to alphabets

            if name.endswith('.csv') or name.endswith('.txt') and header == None:

                out = col_name_generator(out)

            return out

    except UnboundLocalError:

        print("ERROR: you've probably tried to use 'name' which is wrong. Or if you're trying to load from file, forgot to set mode to 'file' first.\n")
        print("USE: data('dataset_name') or data('filename.csv',mode='file')")

## Returns a Pandas dataframe 