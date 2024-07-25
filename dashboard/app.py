import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
df_bike = pd.read_csv('bike.csv')

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

# Visualization 1: Total Rentals by Season
st.subheader('Total Rentals by Season')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='count_hour', data=df_bike, estimator=sum, ax=ax)
ax.set_title('Total Rentals by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Visualization 2: Average Rentals by Weather Condition
st.subheader('Average Rentals by Weather Condition')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weather', y='count_hour', data=df_bike, estimator=np.mean, ax=ax)
ax.set_title('Average Rentals by Weather Condition')
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Average Rentals')
st.pyplot(fig)

# Conclusions
st.subheader('Conclusions')
st.write('**Question 1:** What weather conditions have the highest bike rentals?')
st.write('**Answer 1:** Clear weather with few clouds has the highest bike rentals.')
st.write('**Question 2:** During which season are bike rentals the highest?')
st.write('**Answer 2:** Fall season has the highest average bike rentals.')