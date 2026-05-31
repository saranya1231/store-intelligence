import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Store Intelligence Dashboard")

st.title("Store Intelligence Dashboard")

if os.path.exists("person_counts.csv"):
    df = pd.read_csv("person_counts.csv")
else:
    df = pd.DataFrame({
        "Camera": [
            "CAM1", "CAM1", "CAM1",
            "CAM2", "CAM2", "CAM2",
            "CAM3", "CAM3", "CAM3"
        ],
        "Frame": [
            30, 60, 90,
            30, 60, 90,
            30, 60, 90
        ],
        "PersonCount": [
            2, 4, 3,
            1, 3, 2,
            3, 5, 4
        ]
    })

    st.info(
        "Running with sample analytics data because person_counts.csv is not available."
    )

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