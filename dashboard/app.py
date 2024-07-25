import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
df_bike = pd.read_csv('dashboard/bike.csv')

def create_total_rentals_by_season_df(df):
    rentals_by_season_df = df.groupby('season').agg({'count_hour': 'sum'}).reset_index()
    rentals_by_season_df.rename(columns={'count_hour': 'total_rentals'}, inplace=True)
    return rentals_by_season_df

def create_avg_rentals_by_weather_df(df):
    avg_rentals_by_weather_df = df.groupby('weather').agg({'count_hour': 'mean'}).reset_index()
    avg_rentals_by_weather_df.rename(columns={'count_hour': 'average_rentals'}, inplace=True)
    return avg_rentals_by_weather_df

# Streamlit app
st.title('Bike Sharing Analysis Dashboard')

# Sidebar untuk filter
st.sidebar.header('Filter Data')
season_options = st.sidebar.multiselect('Select Seasons', df_bike['season'].unique(), df_bike['season'].unique())
weather_options = st.sidebar.multiselect('Select Weather Conditions', df_bike['weather'].unique(), df_bike['weather'].unique())

# Filter dataframe berdasarkan pilihan di sidebar
filtered_df = df_bike[(df_bike['season'].isin(season_options)) & (df_bike['weather'].isin(weather_options))]

# Layout grafik 
col1, col2 = st.columns(2)

# Plot total rentals by season
with col1:
    st.subheader('Total Rentals by Season')
    rentals_by_season_df = create_total_rentals_by_season_df(filtered_df)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='total_rentals', data=rentals_by_season_df, palette='viridis')
    plt.title('Total Rentals by Season')
    plt.xlabel('Season')
    plt.ylabel('Total Rentals')
    st.pyplot(plt.gcf())

# Plot average rentals by weather
with col2:
    st.subheader('Average Rentals by Weather')
    avg_rentals_by_weather_df = create_avg_rentals_by_weather_df(filtered_df)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weather', y='average_rentals', data=avg_rentals_by_weather_df, palette='viridis')
    plt.title('Average Rentals by Weather')
    plt.xlabel('Weather Condition')
    plt.ylabel('Average Rentals')
    st.pyplot(plt.gcf())

# Conclusions
st.subheader('Conclusions')
st.write('**Question 1:** What weather conditions have the highest bike rentals?')
st.write('**Answer 1:** Clear weather with few clouds has the highest bike rentals.')
st.write('**Question 2:** During which season are bike rentals the highest?')
st.write('**Answer 2:** Fall season has the highest average bike rentals.')