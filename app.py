import streamlit as st
from services.page_configuration import file_configuration
from services.dashboarding import plot_bottom_left

st.set_page_config(
    page_title="Data Visualization",
    page_icon=":bar_chart:",
    layout="wide"
)
df = file_configuration()

columnA = st.selectbox('Choose your X-axis column:', df.columns)
columnB = st.selectbox('Choose your y-axis column:', df.columns)
type_of_graph = st.selectbox('Choose the type of graph:', [
    'scatter', 'line', 'bar', 'histogram', 'box', 'violin', 'area', 'pie'
])
st.button(label="Submit")
plot_bottom_left(df,columnA,columnB,type_of_graph)

