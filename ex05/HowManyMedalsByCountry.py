# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 14:27:21 by archid-           #+#    #+#              #
#    Updated: 2023/04/20 18:13:28 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


def how_many_medals_by_coutry(df: pd.DataFrame, country: str):
    NOC = df[df.Team == country].iloc[0].NOC
    df = df[(~df.Medal.isnull()) & (df.NOC == NOC)][['Year', 'Medal', 'ID']]
    medals = dict()
    for medal in df.groupby(['Year', 'Medal']).count().iloc:
        year, kind = medal.name
        if year not in medals.keys():
            medals[year] = dict(G=0, S=0, B=0)
        medals[year][kind[0]] = medal['ID']
    return medals
