# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PropotionsBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 11:12:18 by archid-           #+#    #+#              #
#    Updated: 2023/04/20 12:34:30 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str):
    all_females = df[(df.Sex == 'F') & (df.Year == 2004)].groupby('ID')
    tennis_females = df[(df.Sex == 'F') & (df.Year == 2004)
                        & (df.Sport == 'Tennis')].groupby('ID')
    return len(tennis_females) / len(all_females)
