import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Page One")


df=pd.read_csv("Data.csv")

tab1,tab2,tab3=st.tabs(["Filter Student","Individual Student","Comapre Students"])
with tab1:
    c1,c2,c3=st.columns(3)

    classLst=list(df["Class"].unique())
    classLst.append("All")
    Clas1=c1.selectbox("Select Class",classLst,index=3,placeholder="Select Class")

    sectionLst=list(df["Section"].unique())
    sectionLst.append("All")
    Section=c2.selectbox("Select Section",sectionLst,index=3,placeholder="Select Section")

    genderLst=list(df["Gender"].unique())
    genderLst.append("All")
    Gender=c3.selectbox("Select Gender",genderLst,index=2,placeholder="Select Gender")

    tempdf=df.copy()

    if Clas1 != "All":
        tempdf=tempdf[tempdf["Class"]==Clas1]


    if Section != "All":
        tempdf=tempdf[tempdf["Section"]==Section]
        
    if Gender != "All":
        tempdf=tempdf[tempdf["Gender"]==Gender]

    st.dataframe(tempdf)


    # tab1,tab2,tab3=st.tabs(["KPI","BarChart1","BarChart2"])

with tab2:
    t1,t2=st.tabs(["Data","Chart"])
    with t1:
        name=st.selectbox("Select the Student you want",list(df["Name"].unique()),index=0)
        newdf=df[df["Name"]==name].reset_index()
        newdf=newdf.drop("index",axis=1)
        st.dataframe(newdf)
    with t2:
        name=newdf.loc[0,"Name"]
        title=list(newdf.columns[4:8])
        values=list(newdf.iloc[0])[4:8]
        rdf=pd.DataFrame({"Title":title,"values":values})
        fig=px.line_polar(rdf,r="values",theta="Title",line_close=True)
        fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )))
        st.subheader(f"{name}'s Performance")
        st.plotly_chart(fig)
with tab3:
    ca1,ca2=st.columns(2)

    std1=ca1.selectbox("Select Student 1",list(df["Name"].unique()),index=0)
    std2=ca2.selectbox("Select Student 2",list(df["Name"].unique()),index=1)

    newdf=df[(df["Name"]==std1) | (df["Name"]==std2)]
    newdf=newdf[['Name', 'Class', 'Section', 'Gender', 'Math', 'Science', 'English',
       'History',  'Percentage','Total',]]
    st.dataframe(newdf)

    title=list(newdf.columns[4:-1])
    values=list(newdf.iloc[0])[4:-1]

    row1 = newdf[newdf["Name"] == std1].iloc[0]
    row2 = newdf[newdf["Name"] == std2].iloc[0]

    rdf=pd.DataFrame({"Title":title*2,"values":list(row1[title]) + list(row2[title]),"Name": [std1]*len(title) + [std2]*len(title)})
    fig=px.line_polar(rdf,r="values",theta="Title",line_close=True,color="Name",color_discrete_map={std1:"red",std2:"blue"})
    # fig.update_traces(fill='toself')
    # fig.update_layout(
    # polar=dict(
    #     radialaxis=dict(
    #         visible=True,
    #         range=[0, 100]
    #     )))
    st.plotly_chart(fig)

    