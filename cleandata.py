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

st.set_page_config("Dataset String to Number Converter", page_icon="📰", layout="wide")

st.title("Dataset String to Number Converter")

path = st.text_input("**Enter the dataset download URL here:**")
    
if path != "":
    
    df = pd.read_csv(path)
    key = {}

    c1, c2 = st.columns(2)

    with c1:

        st.write("---")
        st.header("Before:")
        st.dataframe(df)

    for col in df.columns:

        if isNum(df.loc[0, col]):
            pass
        
        else:

            key[col] = {}
            valnum = 0

            for val in df[col].unique():
                key[col][val] = valnum
                valnum += 1

            for i in range(len(df)):
                df.loc[i, col] = key[col][df.loc[i, col]]

    with c2:

        st.write("---")
        st.header("After:")
        st.dataframe(df)
        st.write("---")

    if len(list(key.keys())) > 0:
        
        st.header("Value Key")

        for k in key:

            st.subheader(f"`{k}` Column")

            for val in key[k]:
                st.write(f"**{val}**: `{key[k][val]}`")