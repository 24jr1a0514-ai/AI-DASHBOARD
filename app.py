import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Placement Dashboard", layout="wide")

st.title("🎓 Student Placement & Career Success Dashboard")

# Load Dataset
df = pd.read_csv("student_placement_career_success_dataset.csv")

# Sidebar Filters
st.sidebar.header("Filters")

branch = st.sidebar.selectbox(
    "Select Branch",
    ["All"] + list(df["branch"].unique())
)

gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df["gender"].unique())
)

# Apply Filters
filtered_df = df.copy()

if branch != "All":
    filtered_df = filtered_df[filtered_df["branch"] == branch]

if gender != "All":
    filtered_df = filtered_df[filtered_df["gender"] == gender]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", len(filtered_df))
col2.metric("Average CGPA", round(filtered_df["cgpa"].mean(), 2))
col3.metric("Average Salary", round(filtered_df["salary_lpa"].mean(), 2))
col4.metric("Highest Salary", round(filtered_df["salary_lpa"].max(), 2))

# Dataset Preview
st.subheader("Dataset Overview")
st.dataframe(filtered_df.head())

# Chart 1
fig1 = px.histogram(filtered_df, x="cgpa", title="CGPA Distribution")
st.plotly_chart(fig1, use_container_width=True)

# Chart 2
fig2 = px.histogram(filtered_df, x="salary_lpa", title="Salary Distribution")
st.plotly_chart(fig2, use_container_width=True)

# Chart 3
branch_salary = filtered_df.groupby("branch")["salary_lpa"].mean().reset_index()

fig3 = px.bar(
    branch_salary,
    x="branch",
    y="salary_lpa",
    title="Average Salary by Branch"
)

st.plotly_chart(fig3, use_container_width=True)

# Chart 4
fig4 = px.scatter(
    filtered_df,
    x="cgpa",
    y="salary_lpa",
    color="gender",
    title="CGPA vs Salary"
)

st.plotly_chart(fig4, use_container_width=True)

# Chart 5
fig5 = px.box(
    filtered_df,
    x="gender",
    y="salary_lpa",
    title="Salary by Gender"
)

st.plotly_chart(fig5, use_container_width=True)