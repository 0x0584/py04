# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PropotionsBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 11:12:18 by archid-           #+#    #+#              #
#    Updated: 2023/04/23 16:22:21 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import athlete_events_df


def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str):
    df = df[(df.Sexe == gender) & (df.Year == year)]
    return len(df[df.Sport == sport].groupby('ID')) / len(df.groupby('ID'))


if __name__ == '__main__':
    df = athlete_events_df()
    sports = df['Sport'].unique()
    year = 1964
    males = 0.0
    females = 0.0
    for sport in sports:
        f = proportion_by_sport(df, year, sport, 'F')
        females += f
        m = proportion_by_sport(df, year, sport, 'M')
        males += m
        print("{}: {}F {}M".format(sport, f, m))

    assert 0.99 < females
    assert 0.99 < males
