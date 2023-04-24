# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 10:29:11 by archid-           #+#    #+#              #
#    Updated: 2023/04/23 16:22:39 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import athlete_events_df


def youngest_fellah(df: pd.DataFrame, year: int):
    df = df[(df.Year == year)][["Age", "Sexe"]]
    return dict(f=int(df[df.Sexe == 'F'].Age.min()), m=int(df[df.Sexe == 'M'].Age.min()))


if __name__ == "__main__":
    df = athlete_events_df()
    for olympic_year in range(1960, 2000, 4):
        print(youngest_fellah(df, olympic_year))
