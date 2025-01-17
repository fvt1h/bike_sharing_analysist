import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
df_bike = pd.read_csv('dashboard/bike.csv')

def create_avg_rentals_by_weather_df(df):
    avg_rentals_by_weather_df = df.groupby('weather').agg({'count_hour': 'mean'}).reset_index()
    avg_rentals_by_weather_df.rename(columns={'count_hour': 'average_rentals'}, inplace=True)
    return avg_rentals_by_weather_df

def create_total_rentals_by_season_df(df):
    rentals_by_season_df = df.groupby('season').agg({'count_hour': 'sum'}).reset_index()
    rentals_by_season_df.rename(columns={'count_hour': 'total_rentals'}, inplace=True)
    return rentals_by_season_df

# Streamlit app
st.title('Bike Sharing Analysis Dashboard')

# Sidebar untuk filter
st.sidebar.header('Filter Data')
weather_options = st.sidebar.multiselect('Select Weather Conditions', df_bike['weather'].unique(), df_bike['weather'].unique())
season_options = st.sidebar.multiselect('Select Seasons', df_bike['season'].unique(), df_bike['season'].unique())

# Filter dataframe berdasarkan pilihan di sidebar
filtered_df = df_bike[(df_bike['season'].isin(season_options)) & (df_bike['weather'].isin(weather_options))]

# Create average rentals by weather plot
st.subheader('Average Rentals by Weather')
with st.container():
    avg_rentals_by_weather_df = create_avg_rentals_by_weather_df(filtered_df)
    fig_weather, ax_weather = plt.subplots(figsize=(14, 8))  # Adjust size to fit screen
    sns.barplot(x='weather', y='average_rentals', data=avg_rentals_by_weather_df, palette='viridis', ax=ax_weather)
    ax_weather.set_title('Average Rentals by Weather')
    ax_weather.set_xlabel('Weather Condition')
    ax_weather.set_ylabel('Average Rentals')
    st.pyplot(fig_weather)

# Create total rentals by season plot
st.subheader('Total Rentals by Season')
with st.container():
    rentals_by_season_df = create_total_rentals_by_season_df(filtered_df)
    fig_season, ax_season = plt.subplots(figsize=(14, 8))  # Adjust size to fit screen
    sns.barplot(x='season', y='total_rentals', data=rentals_by_season_df, palette='viridis', ax=ax_season)
    ax_season.set_title('Total Rentals by Season')
    ax_season.set_xlabel('Season')
    ax_season.set_ylabel('Total Rentals')
    st.pyplot(fig_season)
    
# Enhanced Conclusions
st.subheader('Conclusions')

# Use Markdown for better visual appeal
st.markdown(
    """
    <div style="padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
        <h3 style="color: #007BFF;">Question 1:</h3>
        <p><strong>What weather conditions have the highest bike rentals?</strong></p>
        <p><em>Answer 1:</em> Clear weather with few clouds has the highest bike rentals.</p>
        <br>
        <h3 style="color: #007BFF;">Question 2:</h3>
        <p><strong>During which season are bike rentals the highest?</strong></p>
        <p><em>Answer 2:</em> Fall season has the highest average bike rentals.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('---')  # Horizontal line for separation