#Libraries
import pandas as pd
from shimoku_api_python import Client

#Utils
from utils.transform import filter_by_streaming_titles

#Constants
import layout.components.constants as constants
periodpath = constants.title_periodpath

"""
Series Trend: Line chart displaying the number of series production over time.
"""
def series_trend(shimoku: Client, order: int, df, tabs_index, origin=""):

    """
    Select, filter, transform and create dic of actors
    """
    def series_trend_transform(data_):
        df_titles = pd.DataFrame(data_)
        # Sort years
        sortedDF = df_titles[df_titles['type'] == 'SHOW'].sort_values('release_year', ascending=False)
        grouped = sortedDF.groupby('release_year').size().reset_index(name='shows')
        # Convert the sorted DataFrame to a dictionary
        dict_data = grouped.to_dict('records')
        return dict_data

    """
    Call and filter all titles
    """
    data: pd.DataFrame = filter_by_streaming_titles(df['all_titles'], origin)

    """
    Call inner data tranform function
    """
    data_ = series_trend_transform(data)

    """
    Setting the hmtl title component
    """
    html_opts = {
        'tabs_index': tabs_index,
        'cols_size': 12,
        'menu_path': periodpath,
    }

    title = f"TVSeries production trend by year in {tabs_index[1]} platform(s)"
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
    order+=1
    shimoku.plt.infographics_text_bubble(
        menu_path=periodpath, order=order, title='TVSeries production', bubble_location='left',
        text='Understanding production trends by year in data analysis is crucial for '
             'making informed business decisions, '
             'and gaining competitive advantage in industries reliant on production.',
        tabs_index=tabs_index,
        chart_function=shimoku.plt.line,
        chart_parameters={
            'data': data_, 'x': 'release_year', 'y': ['shows'],
            'padding': '1,0,0,1', 'cols_size': 20, 'rows_size': 34,
            'option_modifications': {
                'xAxis': {'nameLocation': 'middle', 'nameGap': 30, 'name': 'Release year'},
                'yAxis': {'nameLocation': 'middle', 'nameGap': 30, 'name': 'Total shows'},
                'grid': {'left': '5%', 'right': '0%', 'bottom': '5%', 'top': '2%', 'containLabel': True},
                'toolbox': {'show': True},
            },
        }
    )

    return order