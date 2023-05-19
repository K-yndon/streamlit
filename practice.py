import streamlit as st   
import pandas as pd 

header = st.container()
intro = st.container()
inputs = st.container()

with header:
    st.title('Welcome to my project')

with intro:
    st.text('Here you can plan your race day as either a coach or athlete')
    st.markdown('* feature 1')
    
    data = pd.read_csv('cardiff.csv')
    st.write(data.head())
#hide streamlit style
"""hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
                
st.markdown(hide_st_style, unsafe_allow_html=True)
   """
with inputs:
    #creates 2 columns named col1 and col2. To put items in the columns you use the column name rather than st
    col1,col2 = st.columns(2)
    #this creates an input slider for the user, and the value they chose will be put into the variable you set it equal to
    noAthletes = col1.slider('How many athletes do you have?',min_value=0,max_value=10)
    #drop down box, the options acts like an array but list item types don't matter eg integer or string
    time = col2.selectbox('Time before each course walk',options=['10 min','20 min','30 min'])
    #text input box
    textinput = col1.text_input('Athlete search','enter name here')
    
    if time == '20 min':
        st.write('20 min')
