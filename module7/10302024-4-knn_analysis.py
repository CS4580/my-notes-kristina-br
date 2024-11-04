"""KNN Analysis of Movies
"""

import pandas as pd
import numpy as np
import get_data as gt # your package for downloading zips

# constants
k = 10 #numbr of closest matches
BASE_CASE_ID = 88763 #IMDB_id for 'Back to the Future'

def main():
    print(f'Task 1: Download data set from server')
    dataset_file = 'movies.csv'
    gt.download_dataset(gt.ICARUS_CS4580_DATASET_URL, dataset_file)
    # load into dataframe
    print(f'Task 2: Load movie data into a DataFrame')
    data_file = f'{gt.DATA_FOLDER}/{dataset_file}'
    data = gt.load_data(data_file, index_col='IMDB_id')
    print(f'Loaded {len(data)} records')
    


if __name__ == '__main__':
    main()