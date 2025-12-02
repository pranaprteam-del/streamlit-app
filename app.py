import streamlit as st
import pandas as pd

# Title of the app
st.title('Excel File Reader')

# Upload the Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

if uploaded_file is not None:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Display the first few rows of the dataframe
    st.write(df.head())

    # Optionally, show the entire dataframe in case it's not too large
    if st.checkbox('Show full data'):
        st.write(df)
