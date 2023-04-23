# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 13:46:34 by archid-           #+#    #+#              #
#    Updated: 2023/04/23 14:47:34 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

import matplotlib.pyplot as plt

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
    
    fl = FileLoader()
    df = fl.load('../athlete_events.csv')
    sp = SpatioTemporalData()
    
    for year in range(1960, 2000, 4):
        print(sp.where(year))

    cities = df.City.unique()
    for city in cities:
        print(sp.when(city))


    