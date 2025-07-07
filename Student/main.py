import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Main Page")


df=pd.read_csv("Data.csv")
tab1,tab2,tab3=st.tabs(["KPI","BarChart1","BarChart2"])
with tab1:
    c1,c2=st.columns(2)
    c3,c4=st.columns(2)

    c1.metric(label="Total Students",value=len(df),border=True)
    c2.metric(label="Average Percentage",value=f"{df['Percentage'].mean().round(2)}%",border=True)
    c3.metric(label="Topper",value=f"{df.loc[df['Percentage'].idxmax(),'Name']} - {df['Percentage'].max()}%",border=True)

    c4.metric(label="BackBencher",value=f"{df.loc[df['Percentage'].idxmin(),'Name']} - {df['Percentage'].min()}%",border=True)

# Class and num of students

with tab2:
    tab2.title("Number of Students per class")
    data=df.groupby('Class')['Name'].count().reset_index()
    data["Class"]=data["Class"].astype("str")
    fig=px.bar(data,x="Class",y="Name",color="Class",color_discrete_map={"6":"#ff0000","7":"blue","8":"green"})
    st.plotly_chart(fig)

# Average Scores per subject
with tab3:
    tab3.title("Average Marks per Subject")
    data=pd.DataFrame(df[["Math","Science","English","History"]].mean()).reset_index()
    data.columns=["Subject","Mean"]
    fig=px.bar(data,x="Subject",y="Mean",color="Subject")
    st.plotly_chart(fig)