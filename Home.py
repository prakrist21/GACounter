import streamlit as st
import pandas as pd
import random
st.title("Welcome to GA counter")
st.subheader("All stats from 2024/25 season")
button=st.button("Reset")
if button:
    st.session_state["a_counter"]=0
    st.session_state["a_counter1"]={
            "one":4,
            "two":2,
            "three":1,
            "four":1,
        }
    st.session_state["displayed_team"]={
            "one":[],
            "two":[],
            "three":[],
            "four":[],
        }
    st.session_state["displayedAlready"]=[]
    st.session_state["crrteams"]=None
    st.session_state["lastteam"]=None
    st.session_state["CurrentValue"]=0
    st.session_state["Total"]=0

if "a_counter1" not in st.session_state:
        st.session_state["a_counter"]=0
        st.session_state["a_counter1"]={
            "one":4,
            "two":2,
            "three":1,
            "four":1,
        }
        st.session_state["displayed_team"]={
            "one":[],
            "two":[],
            "three":[],
            "four":[],
        }
        st.session_state["displayedAlready"]=[]
        st.session_state["crrteams"]=None
        st.session_state["lastteam"]=None
        st.session_state["CurrentValue"]=0
        st.session_state["Total"]=0

df=pd.read_csv("TopFiveLeagues.csv")
teams_lst=df["Squad"].to_list()

displayedteams=[]
def displayRandomTeam():
    remaining=list(set(teams_lst)-set(st.session_state["displayedAlready"]))
    team_picked=random.choice(remaining)
    st.html(f"<h1>{team_picked}</h1>")
    # displayedteams.append(team_picked)
    st.session_state["displayedAlready"].append(team_picked)
    return team_picked
        
# st.write(teams_lst[0])
st.divider()

# Buttons
b1,b2,b3,b4=st.columns(4)
# r1,r2,r3,r4=st.columns(4)


with b1:
    button1=st.button("Single")
with b2:
    button2=st.button("Double")
with b3:
    button3=st.button("Triple")
with b4:
    button4=st.button("x4")

# with r1:
#     st.text(st.session_state["a_counter1"]["one"])
# with r2:
#     st.text(st.session_state["a_counter1"]["two"])
# with r3:
#     st.text(st.session_state["a_counter1"]["three"])
# with r4:
#     st.text(st.session_state["a_counter1"]["four"])




if button1:
    if st.session_state["a_counter1"]["one"]<1:
        st.error("Maximum limit passed")
    else:
        st.session_state["a_counter1"]["one"]-=1
        st.session_state["displayed_team"]["one"].append(st.session_state["crrteams"])
        st.session_state["lastteam"]=st.session_state["crrteams"]
        value=df.loc[df["Squad"]== st.session_state["lastteam"],"G+A"].values[0]
        st.session_state["CurrentValue"]=value*1
        st.session_state["Total"]+=st.session_state["CurrentValue"]
        if (st.session_state["a_counter1"]["one"])+(st.session_state["a_counter1"]["two"])+(st.session_state["a_counter1"]["three"])+(st.session_state["a_counter1"]["four"])>0:
            st.session_state["crrteams"]=displayRandomTeam()

if button2:
    if st.session_state["a_counter1"]["two"]<1:
        st.error("Maximum limit passed")
    else:
        st.session_state["displayed_team"]["two"].append(st.session_state["crrteams"])
        st.session_state["a_counter1"]["two"]-=1
        st.session_state["lastteam"]=st.session_state["crrteams"]
        value=df.loc[df["Squad"]== st.session_state["lastteam"],"G+A"].values[0]
        st.session_state["CurrentValue"]=value*2
        st.session_state["Total"]+=st.session_state["CurrentValue"]
        if (st.session_state["a_counter1"]["one"])+(st.session_state["a_counter1"]["two"])+(st.session_state["a_counter1"]["three"])+(st.session_state["a_counter1"]["four"])>0:
            st.session_state["crrteams"] = displayRandomTeam()

if button3:
    if st.session_state["a_counter1"]["three"]<1:
        st.error("Maximum limit passed")
    else:
        st.session_state["displayed_team"]["three"].append(st.session_state["crrteams"])
        st.session_state["a_counter1"]["three"]-=1
        st.session_state["lastteam"]=st.session_state["crrteams"]

        value=df.loc[df["Squad"]== st.session_state["lastteam"],"G+A"].values[0]

        st.session_state["CurrentValue"]=value*3
        st.session_state["Total"]+=st.session_state["CurrentValue"]
        if (st.session_state["a_counter1"]["one"])+(st.session_state["a_counter1"]["two"])+(st.session_state["a_counter1"]["three"])+(st.session_state["a_counter1"]["four"])>0:
            st.session_state["crrteams"] = displayRandomTeam()

if button4:
    if st.session_state["a_counter1"]["four"]<1:
        st.error("Maximum limit passed")
    else:
        st.session_state["displayed_team"]["four"].append(st.session_state["crrteams"])
        st.session_state["a_counter1"]["four"]-=1
        st.session_state["lastteam"]=st.session_state["crrteams"]
        value=df.loc[df["Squad"]== st.session_state["lastteam"],"G+A"].values[0]
        st.session_state["CurrentValue"]=value*4
        st.session_state["Total"]+=st.session_state["CurrentValue"]
        if (st.session_state["a_counter1"]["one"])+(st.session_state["a_counter1"]["two"])+(st.session_state["a_counter1"]["three"])+(st.session_state["a_counter1"]["four"])>0:
            st.session_state["crrteams"] = displayRandomTeam()


if st.session_state["crrteams"] is None:
    st.session_state["crrteams"]=displayRandomTeam()
condition=(st.session_state["a_counter1"]["one"])+(st.session_state["a_counter1"]["two"])+(st.session_state["a_counter1"]["three"])+(st.session_state["a_counter1"]["four"])==0
if condition:
    st.warning(f"🎯 All chances used! Your final score is {st.session_state['Total']}. Reset to play again")


st.divider()
cGA,tGA=st.columns(2)

with cGA:
    # st.write(df["G+A"][df["Squad"]== st.session_state["lastteam"]])
    value=df.loc[df["Squad"]== st.session_state["lastteam"],"G+A"]
    if not value.empty:
        st.write(f"<h4>Current Score</h4><div style='border: 1px solid black;background-color:#ffff66;padding:10px;width:50%;text-align:center'>{st.session_state["CurrentValue"]}</div>",unsafe_allow_html=True)
    else:
        st.write(" ")
with tGA:
    # st.write(df["G+A"][df["Squad"]== st.session_state["lastteam"]])
    value=df.loc[df["Squad"]== st.session_state["lastteam"],"G+A"]
    if not value.empty:
        st.write(f"<h4>Total Score</h4><div style='border: 1px solid black;background-color:#ffff66;padding:10px;width:50%;text-align:center'>{st.session_state["Total"]}</div>",unsafe_allow_html=True)
    else:
        st.write(" ")
    
# st.session_state




