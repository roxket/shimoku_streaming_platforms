#Libraries
import pandas as pd
from shimoku_api_python import Client

#Utils
from utils.transform import filter_by_streaming_credits

#Constants
import layout.components.constants as constants
periodpath = constants.credit_periodpath

"""
Total directors: Indicator displaying the total directors in the database.
"""
def top_directors(shimoku: Client, order: int, dfs: dict[str, pd.DataFrame], tabs_index, origin=""):
    """
    Select, filter, transform and create dic of actors
    """
    def top_directors(df: pd.DataFrame):
        # Select directors
        data: pd.DataFrame = filter_by_streaming_credits(df, origin)
        df_directors = data[data['role'] == 'DIRECTOR']
        # Select the top 5 by IDs
        df_directors_total = df_directors['person_id'].value_counts()
        top_5_ids = df_directors_total.head(5)
        # Join directors information for each ID
        top_5_data = pd.DataFrame({'id': top_5_ids.index, 'name': df_directors['name'].loc[df_directors['person_id'].isin(top_5_ids.index)].unique(), 'movies': top_5_ids.values})
        # Convert the sorted DataFrame to a dictionary
        dict_data = top_5_data.to_dict('records')
        # Reverse the order of the dictionary based on imdb_score
        reversed_dict_list = sorted(dict_data, key=lambda x: x['movies'], reverse=False)
        return reversed_dict_list

    """
    Call inner data tranform function
    """
    top_5_directors = top_directors(dfs)

    """
    Setting the hmtl title component
    """
    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    title = f"top directors based on number of participation in {tabs_index[1]} platform(s)"
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
            x='name', y=['movies'],
            menu_path=periodpath,
            order=order,
            rows_size=2, cols_size=12,
            title='Top Directors',
            tabs_index= tabs_index,)

    return order