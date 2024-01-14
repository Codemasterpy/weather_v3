import numpy
import plotly as py
import plotly.graph_objs as go
import ipywidgets as widgets
import os
os.chdir(r'D:\Projects\Akhila_Sonali\Final_Project')
import streamlit as st
#from transformers import pipeline
import pandas as pd


st.title('Temperature Analysis')

df_Tab1=pd.read_csv('daily_date_temp.csv')
df_Tab2=pd.read_csv('date_temp_weekly.csv')
#df_Tab1

df_Tab1=df_Tab1.rename(columns={'Pune Temperature [2 m elevation corrected]':
                                'temperature'})
    
st.markdown('Daily Temperature Data')    
df_Tab1


st.markdown('Weekly Temperature Data')
df_Tab2    
   

option = st.selectbox('Select an Option',['Select an Option','Daily Analysis',
                                          'Weekly Analysis'])
if option == 'Daily Analysis':
    data=[go.Scatter(y=df_Tab1['temperature'])]
    st.write(data)
    
    
if option == 'Weekly Analysis':
    fig=go.Figure()
    fig.add_trace(go.Scatter(x = df_Tab2['date'],y=df_Tab2['Maximum']))
    fig.add_trace(go.Scatter(x = df_Tab2['date'],y=df_Tab2['Minimum']))
    fig.add_trace(go.Scatter(x = df_Tab2['date'], y=df_Tab2['Mean']))       
    st.write(fig)
