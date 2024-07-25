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

# Plot total rentals by season
st.subheader('Total Rentals by Season')
rentals_by_season_df = create_total_rentals_by_season_df(df_bike)
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='total_rentals', data=rentals_by_season_df)
plt.title('Total Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
st.pyplot(plt.gcf())

# Plot average rentals by weather
st.subheader('Average Rentals by Weather')
avg_rentals_by_weather_df = create_avg_rentals_by_weather_df(df_bike)
plt.figure(figsize=(10, 6))
sns.barplot(x='weather', y='average_rentals', data=avg_rentals_by_weather_df)
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