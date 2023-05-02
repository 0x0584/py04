# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 18:08:06 by archid-           #+#    #+#              #
#    Updated: 2023/04/24 22:54:37 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from typing import List

class MyPlotLib:
    def histogram(self, data: pd.DataFrame, features):
        def plot(ax, title, data):
            ax.set_title(title)
            ax.hist(data)
            ax.grid()
        n_features = len(features)
        fig, ax = plt.subplots(ncols=n_features, nrows=1, sharey='row')
        if len(features) == 1:
            plot(ax, features[0], data[features[0]])
        else:
            for i in range(n_features):
                plot(ax[i], features[i], data[features[i]])
        plt.show()

    def density(self, data: pd.DataFrame, features):
        sns.kdeplot(data=data[features])
        plt.show()

    def pair_plot(self, data: pd.DataFrame, features):
        pd.plotting.scatter_matrix(data[features])

    def box_plot(self, data: pd.DataFrame, features: List[str]):
        fig, ax = plt.subplots(ncols=len(features))
        print(features)
        print(data[features])
        for i in range(len(features)):   
            ax[i].boxplot(data[features[i]], labels=[features[i]])
        plt.show()

def athlete_events_df():
    df = pd.read_csv('../athlete_events.csv')
    
    df['Sexe'] = df['Sex']
    df = df.drop('Sex', axis=1)
    
    return df

if __name__ == '__main__':
    df = athlete_events_df().dropna().drop(columns=['ID'])
    df[['Age', 'Year']] = df[['Age', 'Year']].astype(int)

    def myplot(cols):
        mpl = MyPlotLib()
        # mpl.histogram(df, cols)
        # mpl.pair_plot(df, cols)
        mpl.box_plot(df, cols)
        # for col in cols:
        #     mpl.density(df, [col])

    myplot(['Height', 'Weight'])
    # myplot(['Age', 'Weight'])
    # myplot(['Age', 'Height'])
