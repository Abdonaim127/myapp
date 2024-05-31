import streamlit as st
import json
import pandas as pd

data = pd.read_json('results.json')
print(data.shape)
org_data = pd.read_json('listings.json')
print(org_data.shape)
def format_json(json_data):
    return json.dumps(json_data, indent=4)


# Streamlit app
st.title("Listing Information")

listing_id = st.selectbox("Select Listing ID", options=list(data.WEB_ID.unique()))

if listing_id:
    cols = st.columns([1, 1])

    with cols[0]:

        st.text_area("Chatgpt Output: ", format_json(data[data.WEB_ID == listing_id].results.iloc[0]), height=400)
        #st.json(data[data.WEB_ID == listing_id].results.iloc[0])
    with cols[1]:
        st.text_area("Listings Details: ", format_json(org_data[org_data.ID == listing_id].to_dict(orient='records')[0]), height=400)
        #st.json(org_data[org_data.ID == listing_id].to_dict(orient='records')[0])
    cols = st.columns([1, 1])

    with cols[0]:
        imgs = org_data[org_data.ID == listing_id].to_dict(orient='records')[0]['IMAGES']
        for i in imgs:
            st.image(i['src'], use_column_width=True)

    with cols[1]:
        imgs_res = data[data.WEB_ID == listing_id].results.iloc[0]['Image Analysis']
        for j,i in enumerate(imgs_res):
            print(i)
            st.text_area("Image Analysis " + str(j),
                         format_json(i), height=222)
            #st.json(data[i])

