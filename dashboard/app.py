import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
df_bike = pd.read_csv('dashboard/bike.csv')

# Mapping labels
season_labels = {
    1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'
}
weather_labels = {
    1: 'Clear/Few Clouds/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Light Rain',
    4: 'Heavy Rain/Ice Palletes'
}

# Apply mappings
df_bike['season'] = df_bike['season'].map(season_labels)
df_bike['weather'] = df_bike['weather'].map(weather_labels)

# Streamlit app
st.title('Bike Sharing Analysis Dashboard')

# Plot total rentals by season
st.subheader('Total Rentals by Season')
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='count_hour', data=df_bike, estimator=sum)
plt.title('Total Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure

# Plot average rentals by weather
st.subheader('Average Rentals by Weather')
plt.figure(figsize=(10, 6))
sns.barplot(x='weather', y='count_hour', data=df_bike)
plt.title('Average Rentals by Weather')
plt.xlabel('Weather Condition')
plt.ylabel('Average Rentals')
st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure

# Conclusions
st.subheader('Conclusions')
st.write('**Question 1:** What weather conditions have the highest bike rentals?')
st.write('**Answer 1:** Clear weather with few clouds has the highest bike rentals.')
st.write('**Question 2:** During which season are bike rentals the highest?')
st.write('**Answer 2:** Fall season has the highest average bike rentals.')