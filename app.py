import pandas as pd
import streamlit as st
import plotly.express as px

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv('segmented_customers.csv')

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

st.title("📊 Customer Segmentation Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
segments = st.sidebar.multiselect("Select Segments:", options=df['Segment'].unique(), default=df['Segment'].unique())
channels = st.sidebar.multiselect("Select Channels:", options=df['PreferredChannel'].unique(), default=df['PreferredChannel'].unique())

# Apply filters
filtered_df = df[(df['Segment'].isin(segments)) & (df['PreferredChannel'].isin(channels))]

st.write(f"### Showing {len(filtered_df)} customers")

# -----------------------------
# Segment Distribution (Pie Chart)
# -----------------------------
st.subheader("Segment Distribution")
segment_counts = filtered_df['Segment'].value_counts()
fig_pie = px.pie(values=segment_counts.values, names=segment_counts.index, title="Segment Share")
st.plotly_chart(fig_pie, use_container_width=True)

# -----------------------------
# Recency vs Monetary (Bubble Chart)
# -----------------------------
st.subheader("Recency vs Monetary (Bubble by Frequency)")
fig_scatter = px.scatter(filtered_df, x='Recency', y='Monetary', color='Segment',
                         size='Frequency', hover_data=['Age','Tenure'],
                         title="Customer Segments Distribution")
st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------
# Cluster Summary Table
# -----------------------------
st.subheader("Cluster Summary")
cluster_summary = filtered_df.groupby('Segment')[['Age','Recency','Frequency','Monetary','Tenure']].mean().round(1)
st.dataframe(cluster_summary)

# -----------------------------
# Download Filtered Data
# -----------------------------
st.subheader("Download Data")
st.download_button("Download Filtered Customers (CSV)", data=filtered_df.to_csv(index=False), file_name='filtered_customers.csv')
