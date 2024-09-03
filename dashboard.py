import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)

# Upload data
fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(fl, encoding="ISO-8859-1") 
else:
    os.chdir(r"C:\Users\Izzah Alia\Documents\App develop\InteractiveDashboard")
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")

# New columns
col1, col2 = st.columns(2)  
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True) 

# Get the min and max date
startDate = df["Order Date"].min()
endDate = df["Order Date"].max()

with col1:
    date1 = st.date_input("Start Date", startDate)

with col2:
    date2 = st.date_input("End Date", endDate)

# Filter the DataFrame based on the selected date range
df = df[(df["Order Date"] >= pd.to_datetime(date1)) & (df["Order Date"] <= pd.to_datetime(date2))].copy()

# Side bar

# Region
st.sidebar.header("Choose filter:")
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())

if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# Create for state

state = st.sidebar.multiselect("Pick your state", df["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]
