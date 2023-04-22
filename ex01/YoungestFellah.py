# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 10:29:11 by archid-           #+#    #+#              #
#    Updated: 2023/04/22 16:06:11 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def youngest_fellah(df: pd.DataFrame, year: int):
    df = df[(df.Year == year)][["Age", "Sex"]]
    return dict(f=int(df[df.Sex == 'F'].Age.min()), m=int(df[df.Sex == 'M'].Age.min()))

if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load('../athlete_events.csv')
    for olympic_year in range(1960, 2000, 4):
        print(youngest_fellah(df, olympic_year))
