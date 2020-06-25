import pandas as pd
import numpy as np
import math

def info():
    data = pd.read_csv('/Users/natchanonwongsawaddiwattana/Documents/Doc_Non/Visualize/covid_19_data.csv')
    country_ls = data['Country/Region'].unique()

    ### แยก data แต่ละประเทศ เป็น DICT ####
    dict_data = {}
    avg = {}
    for country in country_ls:
        data_country = data[data['Country/Region'] == country]
        date = data_country.groupby(['ObservationDate']).sum()
        
        dict_data[country] = {}
        dict_data[country]['Corona Infect'] = date['Confirmed'].max()
        dict_data[country]['Deaths'] = date['Deaths'].max()
        dict_data[country]['Recovered'] = date['Recovered'].max()

        con = list(date['Confirmed'])
        avg[country] = np.mean(np.diff(con))
    
    return dict_data, avg

data = pd.read_csv('/Users/natchanonwongsawaddiwattana/Documents/Doc_Non/Visualize/covid_19_data.csv')
country_ls = data['Country/Region'].unique()

print(data)
