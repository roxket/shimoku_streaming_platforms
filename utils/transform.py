#Libraries
import pandas as pd

"""
Format long nombers with letter exponentials
Ex: 999999 -> 999K
"""
def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

"""
Filter by streaming
- streaming: 'amazon', 'disney', 'hbo', 'netflix', 'hulu'
"""
def filter_by_streaming_titles(data: pd.DataFrame, origin=""):

    if origin == "amazon":
        return data.query(f"streaming == 'amazon'")
    if origin == "disney":
        return data.query(f"streaming == 'disney'")
    if origin == "hbo":
        return data.query(f"streaming == 'hbo'")
    if origin == "netflix":
            return data.query(f"streaming == 'netflix'")
    if origin == "hulu":
            return data.query(f"streaming == 'hulu'")

    # origin == all
    return data

"""
Filter by streaming
- streaming: 'amazon', 'disney', 'hbo', 'netflix', 'hulu'
"""
def filter_by_streaming_credits(data: pd.DataFrame, origin=""):

    # Merge dataframes based on the 'ID' column
    df_titles = pd.DataFrame(data['all_titles'])
    df_credits = pd.DataFrame(data['all_credits'])
    merged_df = pd.merge(df_titles, df_credits, on='id')
    
    if origin == "amazon":
        return merged_df.query(f"streaming == 'amazon'")
    if origin == "disney":
        return merged_df.query(f"streaming == 'disney'")
    if origin == "hbo":
        return merged_df.query(f"streaming == 'hbo'")
    if origin == "netflix":
            return merged_df.query(f"streaming == 'netflix'")
    if origin == "hulu":
            return merged_df.query(f"streaming == 'hulu'")

    # origin == all
    return merged_df
