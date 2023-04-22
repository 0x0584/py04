# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 13:46:34 by archid-           #+#    #+#              #
#    Updated: 2023/04/20 14:17:54 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def when(self, location: str):
        df = self.df[self.df['City'] == location]
        return [year.name for year in df.groupby('Year').count().iloc]

    def where(self, date: int):
        df = self.df[self.df['Year'] == date].groupby('City').count()
        return None if len(df) == 0 else df.iloc[0].name

if __name__ == '__main__':
    sp = SpatioTemporalData(pd.read_csv('../ex00/athlete_events.csv'))
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))