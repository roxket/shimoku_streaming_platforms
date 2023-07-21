#Libraries
import pandas as pd
from shimoku_api_python import Client

#Components 
import layout.components.constants as constants

#Utils
from utils.transform import filter_by_streaming_credits

#Constants
periodpath = constants.credit_periodpath

"""
Top 5 actors: Horizontal bar chart displaying the most frequent actors.
"""
def top_actors(shimoku: Client, order: int, dfs: dict[str, pd.DataFrame], tabs_index, origin=""):
    """
    Select, filter, transform and create dic of actors
    """
    def top_actors(df: pd.DataFrame):
        # Select actors
        data: pd.DataFrame = filter_by_streaming_credits(df, origin)
        df_actors = data[data['role'] == 'ACTOR']
        # Select the top 5 by IDs
        df_actors_total = df_actors['person_id'].value_counts()
        top_5_ids = df_actors_total.head(5)
        # Join directors information for each ID
        top_5_data = pd.DataFrame({'id': top_5_ids.index, 'name': df_actors['name'].loc[df_actors['person_id'].isin(top_5_ids.index)].unique(), 'movies': top_5_ids.values})
        # Convert the sorted DataFrame to a dictionary
        dict_data = top_5_data.to_dict('records')
        # Reverse the order of the dictionary based on imdb_score
        reversed_dict_list = sorted(dict_data, key=lambda x: x['movies'], reverse=False)
        return reversed_dict_list

    """
    Call inner data tranform function
    """
    top_5_actors = top_actors(dfs)

    """
    Setting the hmtl title component
    """
    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    title = f"top actors based on number of participation in {tabs_index[1]} platform(s)"
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
            data=top_5_actors,
            x='name', y=['movies'],
            menu_path=periodpath,
            order=order,
            rows_size=2, cols_size=12,
            title='Top Actors',
            tabs_index= tabs_index,)

    return order