import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configure the page layout
st.set_page_config(page_title="Login Analytics", layout="wide")
st.title("System Access Dashboard")

# 2. Load the data using a relative path
csv_path = "daily_login_counts.csv"
try:
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 3. Create top-level summary metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Days Tracked", len(df))
    col2.metric("Highest Login Count", df['Count'].max())
    col3.metric("Average Daily Logins", round(df['Count'].mean(), 1))

    st.divider()

    # 4. Build the interactive Plotly graph
    fig = px.line(df, x='Date', y='Count', title="Daily Logins Over Time", markers=True)
    
    # Customize the graph's aesthetic
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="Total Logins",
        title_x=0.5,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    
    # Render the graph
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Data file not found. Ensure 'daily_login_counts.csv' is in the same folder as this script.")