#-----------------------------------------------------#

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import base64

#-----------------------------------------------------#

st.set_page_config(page_title="SpiderMark", page_icon='images/spidermark_icon.png')

with open("images/spidermark_background.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
st.markdown(f""" <style>
.stApp {{
    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    background-size: cover
}}
</style> """, unsafe_allow_html=True)

st.markdown(""" <style>
# MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

spidermark_logo = Image.open("images/spidermark_logo.png")
spidermark_logo = spidermark_logo.resize((1000,250))

col1, col2, col3 = st.columns(3)
with col2:
    st.image(spidermark_logo)

#-----------------------------------------------------#

raw_data = pd.read_csv("investor_data.csv", index_col=False)

#-----------------------------------------------------#

industry_sel = st.selectbox("Choose Your Industry:", ["", "Renewable Energy", "Technology"])

if industry_sel != "":
    country_sel = st.selectbox("Choose Your Country:", [""]+[i for i in raw_data["country_code"].unique()])
    if country_sel != "":
        region_list = [""]+[i for i in raw_data["region"].unique()]
        region_sel = st.selectbox("Choose Your Region:", region_list)
        if region_sel != "":

            investor_data = raw_data[raw_data["short_description"].str.contains(industry_sel)].head()
            num_investments = pd.DataFrame([i for i in range(investor_data.shape[1])], columns=["# of Investments"])
            total_investments = pd.DataFrame([i for i in range(investor_data.shape[1])], columns=["Total Invested"])
            display_data = [investor_data["name"], investor_data["short_description"], num_investments, total_investments]
            display_data = pd.concat(display_data, axis=1)
            st.write("Investors You Might Be Interested In:")
            for i in display_data.iloc[0:display_data.shape[0]-16,:].iterrows():
                if i[1][0] != np.NaN:
                    st.code(i[1], "java")
               


          
            # st.dataframe(display_data)
            
            # AgGrid(display_data)
           
            #Pass the selected rows to a new dataframe df
            # for i in display_data.iterrows():
            #     st.code(i[1], "python")
            # st.dataframe(display_data)

#-----------------------------------------------------#



#-----------------------------------------------------#

