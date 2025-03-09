
import streamlit as st
import pandas as pd

import time 

st.set_page_config(layout='wide',page_title='StartUp Analysis')


st.title('startup dashboard')
st.header('i m using STREAMLIT')
st.subheader('Hritik rosshan')
st.write('How ar u')
st.markdown("""
            Movies name
             Humshakal
            - Prince
            - Race
            """)
st.code("""
        def squ(input):
            return squ^2
        x=squ(2)    
            """)
st.latex("x^2+y^2=1")
df=pd.DataFrame({'name':['nitish','shubham','bharosi'],'work':['work','student','student']})
st.dataframe(df)
st.metric('revenue','$3L','-3%')
st.json({'name':['nitish','shubham','bharosi'],'work':['work','student','student']})
st.image("1329226.jpeg")
st.video("Panchayat S03E01 Hindi 720p WEB-DL.mkv")

st.sidebar.title('sidebar ka title')

colm1,colm2=st.columns(2)
with colm1:
    st.image("1329226.jpeg")
with colm2:
    st.image("1329226.jpeg")  
    
st.error('login failed')
st.success('login sucess')
st.info('login sucess')
st.warning('login sucess')

bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.01)
    bar.progress(i)
    
email = st.text_input('enter text')
number = st.number_input(' enter pass ')
date = st.date_input('ENTER DOB')
gender=st.selectbox('select gender',['male','female','others'])
 
 
button=st.button('Login Karo')
if button:
    if email == 'shu' and number == 1234:
        st.success('Login successfull')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')
    
    
    
file = st.file_uploader('upload csv file')
if file is not None:
    
    df=pd.read_csv(file)
    st.dataframe(df.describe())