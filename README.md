# Visa Requirements for 🇽🇰 Kosovo Passport Holders
This Python code generates a web app using **Streamlit** to display visa requirements for Kosovo passport holders based on data stored in an Excel file. The app also provides filters to allow users to easily search for specific countries or visa requirements.

The app layout includes a main title and a sidebar for filter options. The sidebar includes two filter options, "Visa Requirement" and "Country". The "Visa Requirement" filter allows the user to select from several options such as "Visa required", "Visa not required", "Admission refused", etc. The "Country" filter allows the user to select one or more countries from a list of options.

The code loads the data from an Excel file using the **pandas** library. The data is then filtered based on the user's selected filter options. If the user selects "All" as the visa requirement option, the data is not filtered by visa requirement. If the user selects one or more countries, the data is filtered to only show information for the selected countries.

Finally, the filtered data is displayed in a table using the **Streamlit** library. The table includes columns for the country name, visa requirement, and additional notes.

This code can be useful for anyone interested in traveling to different countries with a Kosovo passport. By providing visa requirement information in a user-friendly and accessible format, the app can help users make informed decisions about their travel plans.

## Libraries Used
**pandas**: for data manipulation and cleaning

**Streamlit**: to build interactive web app
