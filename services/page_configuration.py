import streamlit as st
import pandas as pd


@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    # cleaning process can be done here
    return data


def load_file():
    with st.sidebar:
        st.title("Configuration")
        uploaded_file = st.sidebar.file_uploader("Upload the file")
        return uploaded_file


def file_configuration():
    st.title("Data Dashboard")

    uploaded_file = load_file()

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        with st.expander("Data preview (Click to expand)"):
            st.dataframe(df)
    else:
        st.info("No file uploaded. Please upload the file")
        st.stop()

    return df
