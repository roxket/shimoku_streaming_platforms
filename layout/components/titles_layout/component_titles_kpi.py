#Libraries
from typing import Any
import pandas as pd
from shimoku_api_python import Client

#Utils
from utils.transform import filter_by_streaming_titles, human_format

#Constants
import layout.components.constants as constants
periodpath = constants.title_periodpath

"""
Indicators: Indicators displaying the total movies
and shows in the database.
"""
def title_kpis(shimoku: Client, order: int, dfs: dict[str, pd.DataFrame], tabs_index, origin=""):
    """
    Indicators
    """
    def calculate_kpis(df: pd.DataFrame):
        """
        Select, filter, transform movies and shows data
        """
        data: pd.DataFrame = filter_by_streaming_titles(df, origin)

        # number of titles
        titles_total = data['id'].nunique()

        # runtime made
        titles_runtime = data['runtime'].sum()

        # Mean imdb score
        titles_mean_imdb_score = data['imdb_score'].mean()

        # Mean tmdb score
        titles_mean_tmdb_score = data['tmdb_score'].mean()

        return {
            'titles_total': titles_total,
            'titles_runtime': titles_runtime,
            'titles_mean_imdb_score': titles_mean_imdb_score,
            'titles_mean_tmdb_score': titles_mean_tmdb_score,
        }

    """
    Call inner data tranform function
    """
    titles_kpis = calculate_kpis(dfs['all_titles'])

    """
    Create the indicator component
    """
    def plot_indicator(data: dict[str, Any], kpi_name: str, order: int, options={}):
        """
        Plots the indicators to the dashboard
        """
        title_kpi = titles_kpis[kpi_name]

        # Put difference in the footer
        common_data = {
            'align': 'left',
            'value': human_format(title_kpi),
            'icon': '',
            'bigIcon': '',
            'footer': ""
        }

        indicator_opts={
            'cols_size': 3,
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

    """
    Setting the hmtl title component
    """
    title = f"{tabs_index[1]} platform(s) overview"
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
    Total title indicator
    """
    order+= 1
    plot_indicator(
        data={
            'title': "Total titles",
        },
        kpi_name='titles_total',
        order=order,
        options={
            'padding':'0, 0, 0, 0'
        },
    )

    """
    Total titles runtime
    """
    order+= 1
    plot_indicator(
        data={
            'title': "Total titles runtime",
        },
        kpi_name='titles_runtime',
        order=order,
    )

    """
    Total titles mean imbd score
    """
    order+= 1
    plot_indicator(
        data={
            'title': "Title mean imbd score",
        },
        kpi_name='titles_mean_imdb_score',
        order=order,
        options={
            'padding':'0, 1, 0, 0'
        },
    )

    """
    Total titles mean tmb score
    """
    order+= 1
    plot_indicator(
        data={
            'title': "Title mean tmb score",
        },
        kpi_name='titles_mean_tmdb_score',
        order=order,
        options={
            'padding':'0, 1, 0, 0'
        },
    )

    return order
