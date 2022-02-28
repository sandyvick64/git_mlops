import pandas as pd
import os
from get_data import read_params, get_data_s3
import argparse

# read the data from data source and save it in data/raw
def load_add_save_file(config_path):
    config = read_params(config_path)
    df = get_data_s3(config_path)

    # Replace 'space berween column name
    new_columns = [col.replace(' ','_') for col in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']

    # Save data
    df.to_csv(raw_data_path, sep=',', index=False, header=new_columns)


if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    print('parsed_args', parsed_args.config)
    load_add_save_file(config_path=parsed_args.config)