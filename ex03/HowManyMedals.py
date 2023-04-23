# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 12:35:57 by archid-           #+#    #+#              #
#    Updated: 2023/04/22 18:39:14 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def how_many_medals(df: pd.DataFrame, name: str):
    df = df[(~df.Medal.isnull()) & (df.Name == name)][['Year', 'Medal', 'ID']]
    medals = dict()
    for medal in df.groupby(['Year', 'Medal']).count().iloc:
        year, kind = medal.name
        if year not in medals.keys():
            medals[year] = dict(G=0, S=0, B=0)
        medals[year][kind[0]] = medal['ID']
    return medals


if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../athlete_events.csv')
    sample = df.sample(n=10)
    for name in sample['Name']:
        print("{}:".format(name), how_many_medals(df, name))