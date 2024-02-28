import plotly.express as px
import streamlit as st


def plot_bottom_left(df, columnA, columnB, type_of_graph):
    try:
        if not columnA or not columnB and type_of_graph != 'pie':  # Pie charts typically need only one column
            st.warning('Please select columns for both the X-axis and Y-axis.')
            st.stop()
        else:
            # Use a dictionary to map user input to actual Plotly Express functions
            graph_functions = {
                'scatter': px.scatter,
                'line': px.line,
                'bar': px.bar,
                'histogram': px.histogram,
                'box': px.box,
                'violin': px.violin,
                'area': px.area,
                'pie': px.pie
            }

            # Get the function based on user input
            graph_function = graph_functions.get(type_of_graph)

            # Check if the function exists (i.e., if the user has selected a valid graph type)
            if graph_function:
                # Special handling for pie charts as they generally require a different set of parameters
                if type_of_graph == 'pie':
                    if not columnA:  # Ensure there's at least one column selected for pie charts
                        st.warning('Please select a column for the values.')
                        st.stop()
                    fig = graph_function(df, names=columnA)
                else:
                    fig = graph_function(df, x=columnA, y=columnB, color="District")
                st.plotly_chart(fig)
            else:
                st.error("Invalid graph type selected!")
    except Exception as e:
        print(f"{e.args}")
