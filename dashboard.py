import streamlit as st
import pandas as pd

st.title("Store Intelligence Dashboard")

df = pd.read_csv("person_counts.csv")

camera = st.selectbox(
    "Select Camera",
    df["Camera"].unique()
)

cam_df = df[df["Camera"] == camera]

st.subheader(f"Analytics for {camera}")

st.metric(
    "Peak Occupancy",
    int(cam_df["PersonCount"].max())
)

st.metric(
    "Average Occupancy",
    round(cam_df["PersonCount"].mean(), 2)
)

st.line_chart(
    cam_df.set_index("Frame")["PersonCount"]
)