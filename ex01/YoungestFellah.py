# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid <archid-@student.1337.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 10:29:11 by archid-           #+#    #+#              #
#    Updated: 2023/05/03 16:56:39 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import athlete_events_df


def youngest_fellah(df: pd.DataFrame, year: int):
    df = df[(df.Year == year)][["Age", "Sexe"]].dropna()
    result = dict(f=0,m=0)
    df_f = df[df.Sexe == 'F']
    if len(df_f) != 0:
        result['f'] = int(df_f.Age.min())
    df_m = df[df.Sexe == 'M']
    if len(df_m) != 0:
        result['m'] = int(df_m.Age.min())
    return result


if __name__ == "__main__":
    df = athlete_events_df()
    for olympic_year in range(1960, 2020, 4):
        print(olympic_year, youngest_fellah(df, olympic_year))
