#-----------------------------------------------------#

import streamlit as st
import pandas as pd
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

industry_sel = st.selectbox("Choose Your Industry:", ["", "Renewable Energy", "Technology", "Healthcare", "Industrial"])

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
                raw_investor.append(pd.DataFrame([row[1][4]]))
                raw_investor.append(pd.DataFrame([row[1][6]]))
                raw_investor = pd.concat(raw_investor, axis=1)
                investor_data.append(raw_investor)
                filtered_region_list.append(row[1][13])
               
        filtered_region_list = pd.DataFrame(filtered_region_list)
        filtered_region_list.sort_values(0)
        
        region_sel = st.selectbox("Choose Your Region:", filtered_region_list)
        investor_data = pd.concat(investor_data)
        investor_data.columns = ["name", "short_description", "region", "cruchbase", "homepage"]
        
        if industry_sel == "Technology":
            industry_sel = ["tech", "technologies", "technology", "software", "internet", "innovation", "innovative", "develop"]
        elif industry_sel == "Renewable Energy":
            industry_sel = ["renewable", "renewable energy", "sustainable", "energy", "climate", "solar", "wind", "hydropower", "hydro", "natural"]
        elif industry_sel == "Healthcare":
            industry_sel = ["health", "healthcare", "hospital"]
        elif industry_sel == "Industrial":
            industry_sel = ["industrial", "manufacturing", "machine", "machining", "factory", "production", "supply"]

        for row in investor_data.iterrows():
            for keyword in industry_sel:
                if keyword in row[1][1]:
                    display_data = [row[1][0], row[1][1], row[1][2], row[1][3], row[1][4]]
                    display_df = pd.DataFrame(display_data, columns=["Data"], index=["Investor", "Description", "Region", "Crunchbase", "Homepage"])
                    st.dataframe(display_df)
                break

#-----------------------------------------------------#