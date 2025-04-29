import streamlit as st
import pandas as pd
import altair as alt
import math
from collections import namedtuple

st.title("Welcome to Streamlit")

# Sliders for spiral parameters
total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

Point = namedtuple('Point', 'x y')
data = []

points_per_turn = total_points / num_turns

for curr_point_num in range(total_points):
    # Determine which turn we're on, and the position within that turn
    curr_turn, i = divmod(curr_point_num, points_per_turn)
    
    # Calculate the angle for the current point
    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    
    # Scale the radius from 0 to 1
    radius = curr_point_num / total_points
    
    # Convert polar coordinates (radius, angle) to Cartesian (x, y)
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    data.append(Point(x, y))

# Convert the data list to a DataFrame
df = pd.DataFrame(data, columns=["x", "y"])

# Use Altair to render a scatter plot
chart = (
    alt.Chart(df, height=500, width=500)
    .mark_circle(color='#0068c9', opacity=0.5)
    .encode(
        x='x:Q',
        y='y:Q'
    )
)

st.altair_chart(chart)
