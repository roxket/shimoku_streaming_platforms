#Libraries
import pandas as pd
from shimoku_api_python import Client

#Utils
from utils.transform import filter_by_streaming_credits

#Constants
import layout.components.constants as constants
periodpath = constants.credit_periodpath

"""
Actor/Actress Influence: Horizontal bar chart that compares the average 
ratings of different actors by imdb_score.
"""

def actors_influence(shimoku: Client, order: int, dfs: dict[str, pd.DataFrame], tabs_index, origin=""):
    """
    Select, filter, transform and create dic of actors
    """
    def actors_influence(df: pd.DataFrame):
        # Select actors
        data: pd.DataFrame = filter_by_streaming_credits(df, origin)
        df_actors = data[data['role'] == 'ACTOR']
        # Select the top 5 by IDs
        grouped_df = df_actors.groupby('person_id')['imdb_score'].mean().reset_index()
        top_5_ids = grouped_df.head(5)
        # Join directors information for each ID
        top_5_data = pd.DataFrame({'id': top_5_ids.index, 'name': df_actors['name'].loc[df_actors['person_id'].isin(top_5_ids.person_id)].unique(), 'imdb_score': top_5_ids.imdb_score})
        # Convert the sorted DataFrame to a dictionary
        dict_data = top_5_data.to_dict('records')
        # Reverse the order of the dictionary based on imdb_score
        reversed_dict_list = sorted(dict_data, key=lambda x: x['imdb_score'], reverse=False)
        return reversed_dict_list

    """
    Call inner data tranform function
    """
    top_5_actors = actors_influence(dfs)

    """
    Setting the hmtl title component
    """
    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }
    title = f"most influential actors based on imdb movie scores in {tabs_index[1]} platform(s)"
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
            x='name', y=['imdb_score'],
            menu_path=periodpath,
            order=order,
            rows_size=2, cols_size=12,
            title='Top Most Influential Actors',
            tabs_index= tabs_index,)

    return order