# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 18:08:06 by archid-           #+#    #+#              #
#    Updated: 2023/04/24 03:37:45 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import wraps

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from typing import List

from FileLoader import athlete_events_df


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(str(func.__name__), list(*args), list(**kwargs))
        return func
    return wrapper


def integral_type(func):
    @wraps(func)
    def wrapper(self, df: pd.DataFrame, features):
        if type(features) != str and type(features) != list:
            return None
        if type(features) == str:
            features = [features]
        print("foo")
        for featuer in df[features].dtypes:
            if featuer != int:
                return None
        print("foo")
        print(func.__name__)
        func(self, df, features)
    return wrapper


def float_type(func):
    print("t2", func.__name__)
    @wraps(func)
    def wrapper(self, df: pd.DataFrame, features):
        if type(features) != str and type(features) != list:
            return None
        if type(features) == str:
            features = [features]
        for featuer in df[features].dtypes:
            if featuer != float:
                return None
        func(self, df, features)
    return wrapper


class MyPlotLib:
    # @composed(integral_type float_type)
    def histogram(self, data: pd.DataFrame, features):
        def plot(ax, title, data):
            ax.set_title(title)
            ax.hist(data)
            ax.grid()
        print("here")
        exit()
        n_features = len(features)
        fig, ax = plt.subplots(ncols=n_features, nrows=1, sharey='row')
        if len(features) == 1:
            plot(ax, features[0], data[features[0]])
        else:
            for i in range(n_features):
                plot(ax[i], features[i], data[features[i]])
        plt.show()

    # @float_type
    # @integral_type
    def density(self, data: pd.DataFrame, features):
        print(">>", features)
        sns.kdeplot(data=data[features])
        plt.show()

    # @float_type
    @integral_type
    def pair_plot(self, data: pd.DataFrame, features):
        pd.plotting.scatter_matrix(data[features])

    def box_plot(self, data: pd.DataFrame, features: List[str]):
        fig, ax = plt.subplots()
        ax.boxplot(data[features], labels=features)
        plt.show()


if __name__ == '__main__':
    df = athlete_events_df().dropna().drop(columns=['ID'])
    df[['Age', 'Year']] = df[['Age', 'Year']].astype(int)

    mpl = MyPlotLib()

    cols = list()
    for col in df.dtypes.index:
        if df.dtypes[col] == int:
            cols.append(col)
    mpl.histogram(df, cols)
    # mpl.pair_plot(df, cols)
    # for col in cols:
    #     print(col)
    #     mpl.density(df, col)

    # cols = list()
    # for col in df.dtypes.index:
    #     if df.dtypes[col] == float:
    #         cols.append(col)

    # mpl.histogram(df, cols)
    # mpl.pair_plot(df, cols)
    # for col in cols:
    #     mpl.density(df, col)
