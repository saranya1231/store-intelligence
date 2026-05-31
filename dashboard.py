import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st.title("Store Intelligence Dashboard")

if os.path.exists("person_counts.csv"):
    df = pd.read_csv("person_counts.csv")
else:
    df = pd.DataFrame({
        "Camera": [
            "CAM1", "CAM1", "CAM1",
            "CAM2", "CAM2", "CAM2",
            "CAM3", "CAM3", "CAM3",
            "CAM4", "CAM4", "CAM4",
            "CAM5", "CAM5", "CAM5"
        ],
        "Frame": [
            30, 60, 90,
            30, 60, 90,
            30, 60, 90,
            30, 60, 90,
            30, 60, 90
        ],
        "PersonCount": [
            2, 4, 3,
            1, 3, 2,
            3, 5, 4,
            2, 3, 1,
            4, 2, 3
        ]
    })

    st.info(
        "Demo environment loaded successfully."
    )

camera = st.selectbox(
    "Select Camera",
    sorted(df["Camera"].unique())
)

cam_df = df[df["Camera"] == camera]

st.subheader(f"Analytics for {camera}")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Peak Occupancy",
        int(cam_df["PersonCount"].max())
    )

with col2:
    st.metric(
        "Average Occupancy",
        round(cam_df["PersonCount"].mean(), 2)
    )

st.line_chart(
    cam_df.set_index("Frame")["PersonCount"]
)

st.dataframe(
    cam_df,
    use_container_width=True
)