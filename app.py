import streamlit as st
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype

st.title('CSV Data Visualizer')
st.write('Upload your CSV files and visualize your data using our amazing site!')

uploaded_file = st.sidebar.file_uploader("Choose a file", type ='csv')


if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # split into two columns
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.header("Data")
        st.write(df)

    with col2:
        st.subheader("Draw Line Graph")
        draw1 = st.selectbox('Select first column', df.columns, index = 0)
        draw2 = st.selectbox('Select second column', df.columns, index = 1)

        if is_numeric_dtype(df[draw1]) and is_numeric_dtype(df[draw2]):
            plot_df = df[[draw1, draw2]]
            plot_df.set_index(draw1, inplace=True)
            st.line_chart(plot_df)
        elif is_string_dtype(df[draw1]) and is_numeric_dtype(df[draw2]):
            st.write ("The first column is not a numerical column.")
        elif is_numeric_dtype(df[draw1]) and is_string_dtype(df[draw2]):
            st.write ("The second column is not a numerical column.")
        else:
            st.write ("Please select numerical columns.")
else:
    st.write("Please upload a file")