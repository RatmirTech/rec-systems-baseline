import pandas as pd
import os


def load_movielens_ml100k(data_dir="../data/ml-100k"):
    # Загружаем оценки
    path_data = os.path.join(data_dir, "u.data")
    cols = ["user_id", "item_id", "rating", "timestamp"]
    ratings = pd.read_csv(path_data, sep='\t', names=cols, engine='python')

    # Загружаем инфо о фильмах
    path_item = os.path.join(data_dir, "u.item")
    movie_cols = ["item_id", "title", "release_date", "video_release_date", "IMDb_url"] + \
                 ["genre_" + str(g) for g in range(19)]
    movies = pd.read_csv(path_item, sep='|', names=movie_cols, engine='python', encoding='latin-1')

    return ratings, movies
