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
Popular Movies: Horizontal bar chart 
displaying the most popular movies.
"""
def tmdb_popularity(shimoku: Client, order: int, df, tabs_index, origin=""):
    """
    Select, filter, transform and create dic of movies
    """
    def tranform_tmdb_popularity(data_):
        # Select data
        df_titles = pd.DataFrame(data_)
        # Sort values from max to min and select top 5
        sorted_df = df_titles[['title','tmdb_popularity']][df_titles['type'] == 'MOVIE'].nlargest(5, 'tmdb_popularity')
        # Convert the sorted DataFrame to a dictionary
        dict_data = sorted_df.to_dict('records')
        # Reverse the order of the dictionary based on tmdb_popularity
        reversed_dict_list = sorted(dict_data, key=lambda x: x['tmdb_popularity'], reverse=False)
        return reversed_dict_list


    """
    Call and filter all titles
    """
    data: pd.DataFrame = filter_by_streaming_titles(df['all_titles'], origin)

    """
    Call inner data tranform function
    """
    data_ = tranform_tmdb_popularity(data)

    """
    Setting the hmtl title component
    """
    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    title = f"TOP rated films based on TMDB popularity index in {tabs_index[1]} platform(s)"
    order += 1
    shimoku.plt.html(
        order=order,
        html=shimoku.html_components.panel(
            text=title.capitalize(),
            href="",
        ),
        **html_opts,
    )

    """
    Create the horizontal barchart component
    """
    order += 1
    shimoku.plt.horizontal_barchart(
            data=data_,
            x='title', y=['tmdb_popularity'],
            menu_path=periodpath,
            order=order,
            rows_size=2, cols_size=12,
            title='TMDB Popularity',
            tabs_index= tabs_index,)

    return order