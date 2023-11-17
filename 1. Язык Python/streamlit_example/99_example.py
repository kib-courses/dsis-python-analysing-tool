#!/usr/bin/env python
# coding: utf-8

# # example 
# 
# > example of using streamlit in a jupyter notebook
# 
# [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ddobrinskiy-jupyter.streamlit.app/)
# 
# 
# In this examle we use [nbdev](https://nbdev.fast.ai/) to export only the relevant cells of our notebook to `.py` file
# 
# - start the cells you want exported with the `#|export` or `#|exporti` directive
# 
# - run `nb_export` to convert the `.ipynb` to `.py`
# 
# ```python
# from nbdev.export import nb_export
# nb_export('99_example.ipynb', lib_path='.', name='example')
# ```
# 
# Alternatively you can use native `nbconvert` from bash, but nbdev is superior :)

# In[1]:


# %load_ext autoreload

# %autoreload 2


# In[2]:


# |exporti

from datetime import datetime

import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm


# In[3]:


sp = StreamlitPatcher()
sp.jupyter()  # register patcher with streamlit


# In[4]:


# |exporti

st.title("Example")


# In[5]:


# |exporti

st.markdown(
    """

This is a test page demonstrating the use of `streamlit_jupyter`.

If you're seeing this in jupyter, then it's working!

"""
)


# In[6]:


sp.registered_methods


# In[7]:


# |exporti

name = st.text_input("What's your name?", "John")


# In[8]:


# |exporti

date = st.date_input("Choose a date", datetime.now().date())


# In[9]:


# |exporti

st.markdown(f"## Hello {name}!\n## The date is {date.strftime('%Y-%m-%d')}")


# In[ ]:





# In[10]:


# |exporti

import time

import pandas as pd

st.subheader("A cached dataframe")

@st.cache_data()
def get_data(date):
    for i in tqdm(range(10)):
        time.sleep(0.1)
    return pd.DataFrame(
        {"date": pd.date_range(date, periods=3), "c": [7, 8, 5], "d": [10, 11, 7]}
    ).set_index("date")


df = get_data(date)
st.write(df)


# In[11]:


# |exporti

st.subheader("Data Editor")
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True, },
       {"command": "st.balloons", "rating": 5, "is_widget": False, },
       {"command": "st.time_input", "rating": 3, "is_widget": True,},
   ]
)
edited_df = st.experimental_data_editor(df)


# In[12]:


# |exporti


st.subheader("One more cache example")
@st.cache_resource(ttl=3600)
def get_resource():
    st.write("Getting resource...")
    for i in tqdm(range(5)):
        time.sleep(0.1)
    return {
        "foo": "bar",
        "baz": [1, 2, 3],
        "qux": {"a": 1, "b": 2, "c": 3},
    }


records = get_resource()
st.json(records)


# In[ ]:





# In[13]:


# |exporti

st.subheader("Ploting")

import plotly.express as px

df_daily = df.mean(axis="columns").rename("daily_average")
fig = px.line(df_daily, title="Daily mean", width=600)
st.write(fig)


# In[14]:


# | exporti

st.metric("Speed", 300, 210, delta_color="normal", label_visibility="visible")


# In[15]:


# | exporti

st.metric("Speed", 300, 210)


# In[16]:


# |exporti

st.code("print(1+1)", language="python")


# In[17]:


# |exporti

show_code = st.checkbox("Show code", value=True)


# In[18]:


# |exporti

if show_code:
    st.code("[i**2 for i in range(100)]")


# In[19]:


# |exporti

option = st.radio("Choose one option", options=["foo", "bar"], index=1)


# In[20]:


# |exporti

option = st.selectbox("Selectbox: ", options=["Jane", "Bob", "Alice"], index=0)


# In[21]:


# |exporti

options = st.multiselect("Multiselect: ", options=["python", "golang", "julia", "rust"])


# In[22]:


# |exporti

options = st.multiselect(
    "Multiselect with defaults: ",
    options=["nbdev", "streamlit", "jupyter", "fastcore"],
    default=["jupyter", "streamlit"],
)


# In[23]:


# | exporti
st.subheader("st.text:")
st.text("This is a text")
st.text("This is \n multiline text")
st.code("This is multiline \n code", language=None)


# In[24]:


# from nbdev.export import nb_export

# nb_export("99_example.ipynb", lib_path="./", name="example")


# In[ ]:




