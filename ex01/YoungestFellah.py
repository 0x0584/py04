# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 10:29:11 by archid-           #+#    #+#              #
#    Updated: 2023/04/20 12:34:43 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


def youngest_fellah(df: pd.DataFrame, year: int):
    min_w = df[df.Sex == 'F'][df.Year == year]['Age'].min()
    min_m = df[df.Sex == 'M'][df.Year == year]['Age'].min()
    return dict(f=min_w, m=min_m)
