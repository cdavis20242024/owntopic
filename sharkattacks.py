import streamlit as st
import pandas as pd

st.title('Shark Attacks')

df = pd.read_csv("attacks.csv", encoding="latin1")

rating_filter = (df['Case Number'].notna())

# Create unique list of countries
countries = list(pd.unique(df['Country'].values.ravel('K')))
countries = [str(country) for country in countries if country != '']

# Multiselect country
selected_countries = st.multiselect('Select countries', sorted(countries))

# Create unique list of types
types = list(pd.unique(df['Type'].values.ravel('K')))
types = [str(typee) for typee in types if typee != '']

# Multiselect type
selected_types = st.multiselect('Select type of attack', sorted(types))

# Columns
col1, col2 = st.columns(2)

with col1:
    # Radio button for selecting fatal incidents, non-fatal incidents, or both
    st.write("")
    st.write("")
    st.write("")
    fatal_filter = st.radio("Filter by Fatal Incidents:", ["Yes", "No", "Both"])

with col2:
    st.image("shark.jpg", width=340)

# Filtering logic based on selected options
if fatal_filter == "Yes":
    if selected_types and selected_countries:
        filtered_data = df[df['Type'].isin(selected_types) & df['Country'].isin(selected_countries) & (df['Fatal (Y/N)'] == 'Y')]
    elif selected_countries:
        filtered_data = df[df['Country'].isin(selected_countries) & (df['Fatal (Y/N)'] == 'Y')]
    elif selected_types:
        filtered_data = df[df['Type'].isin(selected_types) & (df['Fatal (Y/N)'] == 'Y')]
    else:
        filtered_data = df[df['Fatal (Y/N)'] == 'Y']
elif fatal_filter == "No":
    if selected_types and selected_countries:
        filtered_data = df[df['Type'].isin(selected_types) & df['Country'].isin(selected_countries) & (df['Fatal (Y/N)'] == 'N')]
    elif selected_countries:
        filtered_data = df[df['Country'].isin(selected_countries) & (df['Fatal (Y/N)'] == 'N')]
    elif selected_types:
        filtered_data = df[df['Type'].isin(selected_types) & (df['Fatal (Y/N)'] == 'N')]
    else:
        filtered_data = df[df['Fatal (Y/N)'] == 'N']
else:
    if selected_types and selected_countries:
        filtered_data = df[df['Type'].isin(selected_types) & df['Country'].isin(selected_countries)]
    elif selected_countries:
        filtered_data = df[df['Country'].isin(selected_countries)]
    elif selected_types:
        filtered_data = df[df['Type'].isin(selected_types)]
    else:
        filtered_data = df.copy()

# Display the filtered data
st.write(filtered_data[rating_filter] if selected_types or selected_countries else df[rating_filter])

st.write()
