# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 18:08:06 by archid-           #+#    #+#              #
#    Updated: 2023/04/22 15:48:29 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

from typing import List

class MyPlotLib:
    def histogram(self, data: pd.DataFrame, features: List[str]):
        n_features = len(features)
        fig, ax = plt.subplots(ncols=n_features)
        for i in range(n_features):
            ax[i].set_title(features[i])
            ax[i].hist(data[features[i]].dropna())
            ax[i].grid()
        plt.show()
        
    def density(self, data: pd.DataFrame, features: List[str]):
        sb.kdeplot(data=data[features].dropna())
        plt.show()
        
    def pair_plot(self, data: pd.DataFrame, features: List[str]):
        pd.plotting.scatter_matrix(data[features].dropna())
    
    def box_plot(self, data: pd.DataFrame, features: List[str]):
        fig, ax = plt.subplots()
        ax.boxplot(data[features].dropna(), labels=features)
        plt.show()
