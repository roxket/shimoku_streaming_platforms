#Libraries
from typing import Any
import pandas as pd
from shimoku_api_python import Client

#Utils
from utils.transform import filter_by_streaming_credits, human_format

#Constants
import layout.components.constants as constants
periodpath = constants.credit_periodpath

"""
Indicators: Indicators displaying the total actors 
and directors in the database.
"""

def credits_kpis(shimoku: Client, order: int, dfs: dict[str, pd.DataFrame], tabs_index, origin=""):
    """
    Indicators
    """
    def calculate_kpis(df: pd.DataFrame):
        """
        Select, filter, transform actors and directors data
        """
        data: pd.DataFrame = filter_by_streaming_credits(df, origin)

        # Select actors
        df_actors = data[data['role'] == 'ACTOR']
        df_actors_uniques = df_actors['person_id'].nunique()

        # Select directors
        df_directors = data[data['role'] == 'DIRECTOR']
        df_directors_uniques = df_directors['person_id'].nunique()

        return {
            'actors_total': df_actors_uniques,
            'directors_total': df_directors_uniques,
        }

    """
    Call inner data tranform function
    """
    titles_kpis = calculate_kpis(dfs)

    """
    Create the indicator component
    """
    def plot_indicator(data: dict[str, Any], kpi_name: str, order: int, options={}):

        title_kpi = titles_kpis[kpi_name]

        common_data = {
            'align': 'left',
            'value': human_format(title_kpi),
            'icon': '',
            'bigIcon': '',
            'footer': ""
        }

        indicator_opts={
            'cols_size': 6,
            'rows_size': 1,
            'value': 'value',
            'header': 'title',
            'align': 'align',
            'icon': 'icon',
            'big_icon': 'bigIcon',
            'tabs_index': tabs_index,
            'menu_path': periodpath,
            **options,
        }

        shimoku.plt.indicator(
            data={
                **data,
                **common_data,
            },
            order=order,
            **indicator_opts,
        )

    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    next_order = order
    """
    Setting the hmtl title component
    """
    title = f"{tabs_index[1]} platform(s) overview"
    shimoku.plt.html(
        order=next_order,
        html=shimoku.html_components.panel(
            text=title.capitalize(),
            href="",
        ),
        **html_opts,
    )

    """
    Total actors indicator
    """
    next_order+= 1
    plot_indicator(
        data={
            'title': "Total actors",
        },
        kpi_name='actors_total',
        order=next_order,
        options={
            'padding':'0, 0, 0, 0'
        },
    )

    """
    Total directors indicator
    """
    next_order+= 1
    plot_indicator(
        data={
            'title': "Total directors",
        },
        kpi_name='directors_total',
        order=next_order,
        options={
            'padding':'0, 1, 0, 0'
        },
    )

    return next_order