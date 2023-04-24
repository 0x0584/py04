# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 14:27:21 by archid-           #+#    #+#              #
#    Updated: 2023/04/23 16:23:23 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pprint import pprint

import pandas as pd
from FileLoader import athlete_events_df

def how_many_medals_by_coutry(df: pd.DataFrame, team: str):
    
    try: 
        NOC = df[df.Team == team].iloc[0].NOC
    except IndexError:
        NOC = df[df.NOC == team].iloc[0].NOC

    df = df[(~df.Medal.isnull()) & (df.NOC == NOC)][['Year', 'Medal', 'ID']]
    medals = dict()
    for medal in df.groupby(['Year', 'Medal']).count().iloc:
        year, kind = medal.name
        if year not in medals.keys():
            medals[year] = dict(G=0, S=0, B=0)
        medals[year][kind[0]] = medal['ID']
    return medals


if __name__ == '__main__':
    df = athlete_events_df() 
    countries = df.NOC.unique()
    teams = df.Team.unique()
    
    for country in countries:
        pprint(how_many_medals_by_coutry(df, country))

    df = df[['NOC', 'Team']].drop_duplicates().sort_values(by=['NOC', 'Team'])

    pairs = set()
    current = df.iloc[0].NOC
    for row in df.iloc:
        if row.NOC != current:
            current = row.NOC
        pairs.add((current, row.Team))
        
    count = dict()
    for e in pairs:
        if e[0] in count.keys():
            count[e[0]] += 1
        else:
            count[e[0]] = 1

    keys=list()
    for p in pairs:
        if count[p[0]] == 1:
            keys.append(p)
            
    for k in keys:
        pairs.remove(k)

    pprint(pairs)
        