import pandas as pd
import numpy as np
import datetime

# Constants
str_platforms = ['amazon', 'disney', 'hbo', 'netflix', 'hulu']

"""
Reads csv in the data/ folder
"""
def get_data():
    all_credits = pd.read_csv('data/all_credits.csv')
    all_titles = pd.read_csv('data/all_titles.csv')
    return {
        # Current week data
        'all_credits': all_credits,
        # Last week data
        'all_titles': all_titles
    }

"""
Define tab index component 
"""
pt_tab_group = "ptgroup"
platform_tabs_map = {
    'all': {
        'tab_index': (pt_tab_group, "All")
    },
    'amazon': {
        'tab_index': (pt_tab_group, "Amazon")
    },
    'disney': {
        'tab_index': (pt_tab_group,"Disney")
    },
    'hbo': {
        'tab_index': (pt_tab_group, "HBO")
    },
    'netflix': {
        'tab_index': (pt_tab_group, "Netflix")
    },
    'hulu': {
        'tab_index': (pt_tab_group, "Hulu")
    }
}