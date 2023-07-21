# Core python libraries
from typing import Any
# Third party
import pandas as pd
import numpy as np
from shimoku_api_python import Client

# Local imports
from utils.utils import str_platforms, get_data, platform_tabs_map

# Title components
from layout.components.titles_layout.component_titles_kpi import title_kpis
from layout.components.titles_layout.component_titles_popular_genres import popular_genres
from layout.components.titles_layout.component_title_tmdb_popularity import tmdb_popularity
from layout.components.titles_layout.component_titles_series_trend import series_trend

# Credits components 
from layout.components.credits_layout.component_credits_kpi import credits_kpis
from layout.components.credits_layout.component_credits_top_actors import top_actors
from layout.components.credits_layout.component_credits_top_directors import top_directors
from layout.components.credits_layout.component_credits_actors_influence import actors_influence
from layout.components.credits_layout.component_credits_directors_influence import director_influence

"""
Main layout function, plots the dashboard
"""
def plot_dashboard(shimoku: Client):

    # Get the two dataframes we will be working
    dfs = get_data()

    # Get origins including the special 'all'
    streaming_platforms = ['all'] + str_platforms


    """
    APP Title Analysis
    """
    order = 0
    for streaming_platform in streaming_platforms:
        tabs_index = platform_tabs_map[streaming_platform]['tab_index']
        """
        plot the title_kpis component
        """
        order += title_kpis(shimoku, order, dfs, tabs_index, streaming_platform)

        """
        plot the popular_genres component
        """
        order += popular_genres(shimoku, order, dfs, tabs_index, streaming_platform)

        """
        plot the tmdb_popularity component
        """
        order += tmdb_popularity(shimoku, order, dfs, tabs_index, streaming_platform)
    
        """
        plot the series_trend component
        """
        order += series_trend(shimoku, order, dfs, tabs_index, streaming_platform)
        
        order += 1


    """
    APP Credits Analysis
    """
    order = 0
    for streaming_platform in streaming_platforms:
        tabs_index = platform_tabs_map[streaming_platform]['tab_index']
        """
        plot the credits_kpis component
        """
        order += credits_kpis(shimoku, order, dfs, tabs_index, streaming_platform)

        """
        plot the top_actors component
        """
        order += top_actors(shimoku, order, dfs, tabs_index, streaming_platform)

        """
        plot the top_directors component
        """
        order += top_directors(shimoku, order, dfs, tabs_index, streaming_platform)
    
        """
        plot the actors_influence component
        """
        order += actors_influence(shimoku, order, dfs, tabs_index, streaming_platform)
        
        """
        plot the director_influence component
        """
        order += director_influence(shimoku, order, dfs, tabs_index, streaming_platform)

        order += 1


