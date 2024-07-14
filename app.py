import streamlit as st
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

st.title('CSV File Uploader and Viewer')
st.write('Upload your CSV files and visualize your data using our amazing site!')

uploaded_file = st.sidebar.file_uploader("Choose a file", type ='csv')


if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # split into two columns
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.header("Full Data")
        st.write(df)
    
        data = np.random.randn(10, 1)

        col1.subheader("A wide column with a chart")
        col1.line_chart(data)
    with col2:
        st.subheader("Line Graph 1")
        draw1 = st.selectbox('Select the first column', df.columns)
        if is_numeric_dtype(df[draw1]):
            col2.line_chart(df[draw1])
        else:
            st.write ("Please choose a numerical column.")

        draw2 = st.selectbox('Select the second column', df.columns)
        if is_numeric_dtype(df[draw2]):
            data = df[draw2]
            col2.line_chart(data)
        else:
            st.write ("Please choose a numerical column.")
else:
    st.write("Please upload a file")