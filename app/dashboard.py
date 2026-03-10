import streamlit as st
from data_loader import load_cloud_costs
from styles import apply_styles
from components import cost_spike_chart

from components import (
    cost_over_time_chart,
    cost_by_service_chart,
    cost_by_category_chart,
    cost_by_provider_chart
)

# ----------------------------
# Page config (skal være først)
# ----------------------------

st.set_page_config(
    page_title="Cloud Cost Intelligence",
    layout="wide"
)

# Custom styling
apply_styles()

# ----------------------------
# Load data
# ----------------------------

df = load_cloud_costs()

# ----------------------------
# Sidebar filters
# ----------------------------

st.sidebar.title("Cloud Filters")

provider_filter = st.sidebar.multiselect(
    "Cloud Provider",
    df["provider"].unique()
)

service_filter = st.sidebar.multiselect(
    "Service",
    df["service"].unique()
)

if provider_filter:
    df = df[df["provider"].isin(provider_filter)]

if service_filter:
    df = df[df["service"].isin(service_filter)]

# ----------------------------
# Header
# ----------------------------

st.title("☁ Cloud Cost Intelligence")
st.caption("Analyze and optimize your cloud spending")

# ----------------------------
# KPI CARDS
# ----------------------------

total_cost = df["cost"].sum()
top_service = df.groupby("service")["cost"].sum().idxmax()
num_services = df["service"].nunique()
num_providers = df["provider"].nunique()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("💰 Total Cloud Cost", f"${total_cost:,.2f}")
kpi2.metric("🔥 Top Service", top_service)
kpi3.metric("⚙ Active Services", num_services)
kpi4.metric("☁ Providers", num_providers)

st.divider()

# ----------------------------
# MAIN ANALYTICS
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    cost_over_time_chart(df)

with col2:
    cost_by_service_chart(df)

st.divider()

# ----------------------------
# SECONDARY ANALYTICS
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    cost_by_provider_chart(df)

with col2:
    cost_by_category_chart(df)


# ----------------------------
# SPIKE DETECTION
# ----------------------------


st.divider()

st.subheader("Cost Spike Detection")

cost_spike_chart(df)