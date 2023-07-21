#Libraries
from typing import Any
import pandas as pd
from shimoku_api_python import Client

#Utils
from utils.transform import filter_by_streaming_titles

#Constants
import layout.components.constants as constants
periodpath = constants.title_periodpath
"""
Popular Genres: Rose chart displaying the popular genres.
"""
def popular_genres(shimoku: Client, order: int, df, tabs_index, origin=""):
    """
    Select, filter, transform data
    """
    def tranform_genre_data(data_):
        import ast
        genres_by_platform = data_['genres']
        list_one = []
        for element in genres_by_platform:
            list = ast.literal_eval(element)
            list_one.extend(list)

        df_genres = pd.DataFrame(list_one, columns=['name'])
        groupedDF = df_genres.groupby('name',sort=True).size().reset_index(name='value')
        sortedDF = groupedDF.sort_values('value', ascending=False)

        return sortedDF.to_dict('records')

    data: pd.DataFrame = filter_by_streaming_titles(df['all_titles'], origin)

    """
    Call inner data tranform function
    """
    data_ = tranform_genre_data(data)

    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    """
    Setting the hmtl title component
    """
    title = f"popular genres in {tabs_index[1]} platform(s)"
    
    order += 1
    shimoku.plt.html(
        order=order,
        html=shimoku.html_components.panel(
            text=title.capitalize(),
            href="",
        ),
        **html_opts,
    )

    order+=1

    """
    Create the rose chart component
    """
    shimoku.plt.rose(data_, 
                    menu_path=periodpath, 
                    order=order,
                    rows_size=2, 
                    cols_size=12,
                    tabs_index= tabs_index,)
    
    return order