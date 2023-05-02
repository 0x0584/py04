# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid <archid-@student.1337.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/24 12:32:43 by archid-           #+#    #+#              #
#    Updated: 2023/05/02 16:34:46 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from MyPlotLib import MyPlotLib, pd, athlete_events_df


class Komparator:
    def __init__(self, df: pd.DataFrame):
        self.df = df.dropna()
        self.mpl = MyPlotLib()

    def compare_box_plots(self, categorical_var, numerical_var):
        if type(numerical_var) != list and type(numerical_var) != str:
            return None
        print("abc")
        if type(numerical_var) == str:
            numerical_var = [numerical_var]
        print("abc")
        if type(categorical_var) != str and type(categorical_var) != list:
            return None
        print("abc")
        if type(categorical_var) == str:
            categorical_var = [categorical_var]
        print("abc")
        for category in categorical_var:
            for value in self.df[category].unique():
                df = self.df[(self.df[category] == value)]
                for numerical in numerical_var:
                    print(df[numerical])
                    exit()
                    self.mpl.box_plot(df[numerical], [numerical])
        print("abc")


if __name__ == '__main__':
    df = athlete_events_df().dropna()
    print(df)

    mpl = MyPlotLib()
    mpl.box_plot(df, ['Weight', 'Height'])

    kmp = Komparator(df)
    kmp.compare_box_plots(['Sexe', 'Year'], ['Weight', 'Height'])
