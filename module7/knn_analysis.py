"""KNN Analysis of Movies
"""
import pandas as pd
import numpy as np
import get_data as gt  # your package

# Constants
K = 10  # number of closest matches
BASE_CASE_ID = 88763  # IMDB_id for 'Back to the Future'


def metric_stub(base_case_value, comparator_value):
    return 0


def print_top_k(df, sorted_value, comparison_type):
    print(f'Top {K} closest matches by {comparison_type}')
    counter = 1
    for idx, row in df.head(K).iterrows():
        print(f"""Top {counter} match: [{idx}]:{row['year']} {
              row['title']}, {row['genres']}, {row[sorted_value]}""")
        counter += 1


def euclidean_distance(base_case_year: int, comparator_value: int):
    # return abs(base_case_year - comparator_year)
    pass


def jaccard_similarity_normal(base_case_genres: str, comparator_genres: str):
    base_case_genres = set(base_case_genres.split(';'))
    comparator_genres = set(comparator_genres.split(';'))
    numerator = len(base_case_genres.intersection(comparator_genres))
    denominator = len(base_case_genres.union(comparator_genres))
    return float(numerator)/float(denominator)


def knn_analysis_driver(data_df, base_case, comparison_type, metric_stub, sorted_value='metric'):
    df = data_df.copy()  # make a copy of dataframe
    # WIP: Create df of filter data
    df[sorted_value] = df[comparison_type].map(
        lambda x: metric_stub(base_case[comparison_type], x))
    # sort return values from function stub
    sorted_df = df.sort_values(by=sorted_value)
    sorted_df.drop(BASE_CASE_ID, inplace=True)
    print(sorted_df['title'].head(K))  # print top 10 values


def main():
    # TASK 1: Get dataset from server
    print(f'Task 1: Download dataset from server')
    dataset_file = 'movies.csv'
    gt.download_dataset(gt.ICARUS_CS4580_DATASET_URL, dataset_file)
    # TASK 2: Load  data_file into a DataFrame
    print(f'Task 2: Load movie data into a DataFrame')
    data_file = f'{gt.DATA_FOLDER}/{dataset_file}'
    data = gt.load_data(data_file, index_col='IMDB_id')
    print(f'Loaded {len(data)} records')
    print(f'Data set Columns {data.columns}')
    print(f'Data set description {data.describe()}')
    # TASK 3: KNN Analysis Driver
    print(f'KNN Simple Analysis')
    base_case = data.loc[BASE_CASE_ID]
    print(f"Comparing alll movies to our case: {base_case['title']}")
    knn_analysis_driver(df=data,  base_case=base_case,
                        comparison_type='genres', metric_func=metric_stub, sorted_value='metric')


if __name__ == '__main__':
    main()
