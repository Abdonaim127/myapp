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
st.title("Chatgpt Model(β) - Results")

st.write("This app created to help us in evaluating the results of Model")
#listing_id = st.selectbox("Select Listing ID", options=list(data.WEB_ID.unique()))
listing_id = st.selectbox("Select Listing ID", options=[5104105,
5103889,
5103837,
5103958,
5104027,
5103925,
5103809,
5104048,
5104178])



if listing_id:

    cols = st.columns([1, 1])

    with cols[0]:

        st.text_area("Model Output: ", format_json(data[data.WEB_ID == listing_id].results.iloc[0]), height=400)
        st.json(data[data.WEB_ID == listing_id].results.iloc[0])
    with cols[1]:
        st.text_area("Listings Details: ", format_json(org_data[org_data.ID == listing_id].to_dict(orient='records')[0]), height=400)
        st.json(org_data[org_data.ID == listing_id].to_dict(orient='records')[0])

    st.title('Description')

    cols = st.columns([1, 1])

    with cols[0]:

        st.text_area("Generated Description: ", data[data.WEB_ID == listing_id].results.iloc[0]['Description Analysis']['friendly_description'], height=400)

    with cols[1]:
        st.text_area("Original Description: ", org_data[org_data.ID == listing_id].to_dict(orient='records')[0]['DESCRIPTION'], height=400)


    imgs = org_data[org_data.ID == listing_id].to_dict(orient='records')[0]['IMAGES']
    imgs_res = data[data.WEB_ID == listing_id].results.iloc[0]['Image Analysis']
    st.title('Images')
    for i in range(len(imgs)):  # Loop to create 10 rows


        st.write("Image Analysis " + str(i))
        cols = st.columns([1, 1])

        with cols[0]:


            st.markdown('#')
            st.image(imgs[i]['src'], use_column_width=True)

        with cols[1]:


            st.markdown('#')

            st.json(imgs_res[i])

