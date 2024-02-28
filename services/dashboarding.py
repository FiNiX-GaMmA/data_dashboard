import plotly.express as px
import streamlit as st


def plot_bottom_left(df):
    fig = px.line(df, x="x", y="y", color="blue")
    st.plotly_chart(fig)


