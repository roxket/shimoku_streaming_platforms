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
Director Analysis: 
Horizontal bar chart that compares the average 
ratings of different director by imdb_score.
"""

def director_influence(shimoku: Client, order: int, dfs: dict[str, pd.DataFrame], tabs_index, origin=""):
    """
    Select, filter, transform and create dic of directors
    """
    def director_influence(df: pd.DataFrame):
        # Select directors
        data: pd.DataFrame = filter_by_streaming_credits(df, origin)
        df_actors = data[data['role'] == 'DIRECTOR']
        # Select the top 5 by IDs
        grouped_df = df_actors.groupby('person_id')['imdb_score'].mean().reset_index()
        top_5_ids = grouped_df.head(5)
        # Join directors information for each ID
        top_5_data = pd.DataFrame({'id': top_5_ids.index, 'name': df_actors['name'].loc[df_actors['person_id'].isin(top_5_ids.person_id)].unique(), 'imdb_score': top_5_ids.imdb_score})
        # Convert the DataFrame to a dictionary
        dict_data = top_5_data.dropna().to_dict('records')
        # Reverse the order of the dictionary based on imdb_score
        reversed_dict_list = sorted(dict_data, key=lambda x: x['imdb_score'], reverse=False)
        return reversed_dict_list
    """
    Call inner data tranform function
    """
    top_5_directors = director_influence(dfs)

    """
    Setting the hmtl title component
    """
    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    title = f"most influential directors based on imdb movie scores in {tabs_index[1]} platform(s)"
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
            data=top_5_directors,
            x='name', y=['imdb_score'],
            menu_path=periodpath,
            order=order,
            rows_size=2, cols_size=12,
            title='Top Most Influential Directors',
            tabs_index= tabs_index,)

    return order