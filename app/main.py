import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, compute_summary

st.set_page_config(
    page_title="Solar Challenge Dashboard",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ Solar Challenge: Cross-Country Dashboard")
st.markdown(
    """
    Interactive visualization of solar metrics (GHI, DNI, DHI)
    for **Benin**, **Sierra Leone**, and **Togo**.
    """
)

# Sidebar – country and metric selection
st.sidebar.header("Filters")

countries = ["Benin", "SierraLeone", "Togo"]
metrics = ["GHI", "DNI", "DHI"]

selected_countries = st.sidebar.multiselect(
    "Select countries to compare:",
    countries,
    default=countries
)
selected_metric = st.sidebar.selectbox(
    "Select metric to visualize:",
    metrics
)

# Load and merge cleaned CSVs
data = load_data(selected_countries)
if data.empty:
    st.warning("No data loaded. Please ensure cleaned CSVs exist in the data/ folder.")
    st.stop()

# Boxplot
st.subheader(f"{selected_metric} Distribution by Country")
fig_box = px.box(
    data[data["country"].isin(selected_countries)],
    x="country",
    y=selected_metric,
    color="country",
    points="outliers",
    template="plotly_white"
)
st.plotly_chart(fig_box, use_container_width=True)

# Summary Table
st.subheader("Summary Statistics")
summary_df = compute_summary(data, selected_countries, metrics)
st.dataframe(summary_df.style.highlight_max(axis=0), use_container_width=True)

# Average GHI ranking
st.subheader("Ranking by Average GHI")
avg_ghi = (
    data[data["country"].isin(selected_countries)]
    .groupby("country")["GHI"]
    .mean()
    .sort_values(ascending=False)
)
fig_bar = px.bar(
    avg_ghi,
    x=avg_ghi.index,
    y=avg_ghi.values,
    text=avg_ghi.values.round(2),
    labels={"x": "Country", "y": "Mean GHI"},
    color=avg_ghi.index,
    template="plotly_white",
)
fig_bar.update_traces(textposition="outside")
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")
st.caption("Data source: Cleaned solar datasets (Benin, Sierra Leone, Togo).")
