# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 09:32:16 by archid-           #+#    #+#              #
#    Updated: 2023/04/22 16:56:57 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


class FileLoader:
    def load(self, path):
        if type(path) != str:
            return None
        try:
            df = pd.read_csv(path)
            print("Read dataset %ld x %ld" % df.shape)
            return df
        except Exception as e:
            print(
                f"Exception: {e.__class__.__name__} -- {e.strerror if hasattr(e, 'strerror') else e }")
            return None

    def display(self, df, n=10):
        if type(df) == pd.DataFrame and type(n) == int:
            if n > 0:
                print(df.head(n))
            else:
                print(df.tail(-n))


if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('athlete_events.csv')
    fl.display(df)
    fl.display(df, 1)
    fl.display(df, -1)
    fl.display(df, 0)
