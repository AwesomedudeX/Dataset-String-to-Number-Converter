import streamlit as st

import numpy as np
import pandas as pd

def isNum(val):
    
    try:
        val = int(val)
        return True

    except:
        
        try:
            val = float(val)
            return True

        except:
            return False

@st.cache_data
def convert(data):

    key = {}

    for col in data.columns:

        if isNum(data.loc[0, col]):
            pass
        
        else:

            key[col] = {}
            valnum = 0

            for val in data[col].unique():
                key[col][val] = valnum
                valnum += 1

            for i in range(len(data)):
                data.loc[i, col] = key[col][data.loc[i, col]]

    return df, key

st.set_page_config("Dataset String to Number Converter", page_icon="📰", layout="wide")

st.title("Dataset String to Number Converter")

path = st.text_input("**Enter the dataset download URL here:**")
    
if path != "":
    
    st.sidebar.header("Download Files:")

    try:

        df = pd.read_csv(path)

        c1, c2 = st.columns(2)

        with c1:

            st.write("---")
            st.header("Before:")
            st.dataframe(df)

        df, key = convert(df)

        with c2:

            st.write("---")
            st.header("After:")
            st.dataframe(df)
            st.write("---")

        write = f"Dataset URL: {path}"

        if len(list(key.keys())) > 0:
            
            st.header("Value Key")

            for k in key:

                st.subheader(f"`{k}` Column:")
                write += f"\n\n\n{k} Column"

                for val in key[k]:
                    st.write(f"**{val}**: `{key[k][val]}`")
                    write += f"\n\n{val}: {key[k][val]}"

        try:

            if st.sidebar.download_button("Download Converted File", df.to_csv(), "data.csv"):
                st.sidebar.success("Data downloaded successfully.")

            if st.sidebar.download_button("Download Conversion Key", data=write, file_name="conversion_key.txt"):
                st.sidebar.success("Key downloaded successfully.")

        except:
            st.sidebar.error("There was an error in downloading the file.")

    except:

        st.error("Please enter a valid dataset download URL.")

else:
    st.sidebar.header("Please enter a file download URL")
