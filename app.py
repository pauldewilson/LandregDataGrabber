from models.urls_from_urls_txtfile import return_list_urls_from_txtfile
from connstrings.connstrings import msss_connstring
from models.ux_improvements import (ux_friendly_cols,
                                    ux_friendly_cols_relevant,
                                    ux_friendly_prop_type_names)
import pandas as pd

# iterate over all URLs/CSV files
# NOTE: only relevant columns for current project will be kept for optimisation. See ux_friendly_cols_relevant.
# ALSO NOTE: When sending to SQL it simply appends. Risk of duplication.
# Handling that specific issue was not required and therefore not coded in to save time
for url in return_list_urls_from_txtfile():
    # read csv to pandas DataFrame
    df = pd.read_csv(url)
    # rename columns
    df.columns = ux_friendly_cols()
    # optimise df
    df = df[ux_friendly_cols_relevant()]
    # change deed_date to datetime64 since parse_dates fails at read_csv
    df['deed_date'] = pd.to_datetime(df['deed_date'])
    # ux the property types
    df['property_type'].replace(ux_friendly_prop_type_names(), inplace=True)
    # insert date breakdowns and del irrelevant for optimisation
    day = df['deed_date'].dt.day
    df.insert(3, 'day', day)
    del day
    month = df['deed_date'].dt.month
    df.insert(4, 'month', month)
    del month
    year = df['deed_date'].dt.year
    df.insert(5, 'year', year)
    del year
    # breakdown and insert postcode chunks
    postal_sector = df['postcode'].str.extract('([^\s]+\s\d)')
    df.insert(loc=7, column='post_sect', value=postal_sector, allow_duplicates=True)
    del postal_sector
    postal_area = df['postcode'].str.extract('([^\s]+)')
    df.insert(loc=8, column='post_area', value=postal_area, allow_duplicates=True)
    del postal_area
    postal_region = df['post_area'].str.extract('([A-Z]+)')
    df.insert(loc=9, column='post_reg', value=postal_region, allow_duplicates=True)
    del postal_region
    df.to_sql('landreg_sm', if_exists='append', con=msss_connstring(host='host', database_name='dbname'), index=False)
