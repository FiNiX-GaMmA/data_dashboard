import streamlit as st
from services.page_configuration import file_configuration,load_data
from services.dashboarding import plot_bottom_left

st.set_page_config(
    page_title="Data Visualization",
    page_icon=":bar_chart:",
    layout="wide"
)
file_configuration()

plot_bottom_left(file_configuration())

