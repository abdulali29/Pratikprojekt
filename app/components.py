import streamlit as st
import plotly.express as px


def cost_over_time_chart(df):

    data = df.groupby("date")["cost"].sum().reset_index()

    fig = px.line(
        data,
        x="date",
        y="cost",
        markers=True,
        title="Cloud Cost Trend"
    )

    st.plotly_chart(fig, use_container_width=True)


def cost_by_service_chart(df):

    data = (
        df.groupby("service")["cost"]
        .sum()
        .reset_index()
        .sort_values("cost", ascending=False)
    )

    fig = px.bar(
        data,
        x="service",
        y="cost",
        color="service",
        title="Cost by Service"
    )

    st.plotly_chart(fig, use_container_width=True)


def cost_by_category_chart(df):

    data = (
        df.groupby("category")["cost"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        data,
        values="cost",
        names="category",
        title="Cost Distribution by Category"
    )

    st.plotly_chart(fig, use_container_width=True)


def cost_by_provider_chart(df):

    data = (
        df.groupby("provider")["cost"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="provider",
        y="cost",
        color="provider",
        title="Cost by Cloud Provider"
    )

    st.plotly_chart(fig, use_container_width=True)

    def cost_spike_chart(df):

    daily = (
        df.groupby("date")["cost"]
        .sum()
        .reset_index()
    )

    mean_cost = daily["cost"].mean()
    std_cost = daily["cost"].std()

    threshold = mean_cost + 2 * std_cost

    daily["spike"] = daily["cost"] > threshold

    fig = px.scatter(
        daily,
        x="date",
        y="cost",
        color="spike",
        title="Cloud Cost Spikes Detection",
        color_discrete_map={
            True: "red",
            False: "blue"
        }
    )

    st.plotly_chart(fig, use_container_width=True)