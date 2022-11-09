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
    country_list = [i for i in raw_data["country_code"].unique()]
    country_sel = st.selectbox("Choose Your Country:", pd.DataFrame([""]+country_list).sort_values(0))

    if country_sel != "":

        region_list = raw_data.drop_duplicates(subset="region")
        filtered_region_list = []
        investor_data = []
        for row in region_list.iterrows():
            if row[1][14] == country_sel:
                raw_investor = []
                raw_investor.append(pd.DataFrame([row[1][1]]))
                raw_investor.append(pd.DataFrame([row[1][15]]))
                raw_investor.append(pd.DataFrame([row[1][13]]))
                raw_investor = pd.concat(raw_investor, axis=1)
                investor_data.append(raw_investor)
                filtered_region_list.append(row[1][13])
               
        filtered_region_list = pd.DataFrame(filtered_region_list)
        filtered_region_list.sort_values(0)
        
        region_sel = st.selectbox("Choose Your Region:", filtered_region_list)
        investor_data = pd.concat(investor_data)
        investor_data.columns = ["name", "short_description", "region"]
        
        if industry_sel == "Technology":
            industry_sel = ["tech", "technologies", "technology"]
        elif industry_sel == "Renewable Energy":
            industry_sel = ["renewable", "renewable energy", "sustainable"]

        for row in investor_data.head().iterrows():
            for keyword in industry_sel:
                if keyword in row[1][1]:
                    st.code(row, "java")
            
            

        # display_data = investor_data[investor_data["short_description"]].str.contains(industry_sel).head()
        # print(investor_data)

        # for i in display_data.iloc[0:display_data.shape[0]-16,:].iterrows():
        #     if i[1][0] != np.NaN:
        #         st.code(i[1], "java")
        #         st.table(i[1])
        #         st.dataframe(i[1])

        # investor_data = raw_data[raw_data["short_description"].str.contains(industry_sel)].head()
        # num_investments = pd.DataFrame([i for i in range(investor_data.shape[1])], columns=["# of Investments"])
        # total_investments = pd.DataFrame([i for i in range(investor_data.shape[1])], columns=["Total Invested"])
        # display_data = [investor_data["name"], investor_data["short_description"], num_investments, total_investments]
        # display_data = pd.concat(display_data, axis=1)
        # st.write("Investors You Might Be Interested In:")
        # for i in display_data.iloc[0:display_data.shape[0]-16,:].iterrows():
        #     if i[1][0] != np.NaN:
                # st.code(i[1], "java")
                # st.table(i[1])
                # st.dataframe(i[1])
            


          
            # st.dataframe(display_data)
            
            # AgGrid(display_data)
           
            #Pass the selected rows to a new dataframe df
            # for i in display_data.iterrows():
            #     st.code(i[1], "python")
            # st.dataframe(display_data)

#-----------------------------------------------------#



#-----------------------------------------------------#

