import streamlit as st
import pandas as pd

# Load data from Excel file
data = pd.read_excel('pass.xlsx')

# Set up Streamlit app layout
st.set_page_config(page_title="Visa Requirements for 🇽🇰 Kosovo Passport Holders", page_icon=":earth_africa:")
st.title("Visa Requirements for Kosovo Passport Holders")
st.sidebar.title("Filters")
st.sidebar.write("Select options to filter countries")

# Create filter options for visa requirements
visa_req_options = ['All', 'Visa required', 'Visa not required', 'Admission refused', 'Visa on arrival', 'eVisa', 'Travel certificate required', 'Freedom of movement']

# Create sidebar widgets for filter options
st.sidebar.subheader("Visa Requirement")
visa_req_filter = st.sidebar.selectbox("", visa_req_options, key='visa_req_filter')
st.sidebar.subheader("Country")
country_options = data['Country'].unique()
selected_countries = st.sidebar.multiselect('', country_options, key='selected_countries')

# Filter data based on selected options
if visa_req_filter != 'All':
    data = data[data['Visa requirement'] == visa_req_filter]

if selected_countries:
    data = data[data['Country'].isin(selected_countries)]

# Display filtered data in table format
st.write(data.style.set_properties(**{'font-family': 'Arial', 'font-size': '12pt', 'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('font-weight', 'bold'), ('border-radius', '5px')]}, {'selector': 'td', 'props': [('border-radius', '5px')]}]))
