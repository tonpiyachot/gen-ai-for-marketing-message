# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hyper-Personalized Marketing",
        page_icon="👋",
        layout='wide'
    )

    st.write("# Gen AI for Hyper-Personalized Marketing Messages 👋")

    # st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This Streamlit web app leverages Generative AI to create hyper-personalized marketing messages based on user data. 
        
        Users input their details, personality, and marketing engagement information, and the app generates tailored messages using OpenAI's API (GPT-3.5-Turbo).

        ### Want to learn more?
        - Check out [OpenAI](https://openai.com/)
        - Explore more about [LLMOps Dify.ai](https://dify.ai/)
        - Jump into our [presentation](https://www.canva.com/design/DAF1FagcDMo/wgBh4_G_Nvdpf5kn1UlbrA/view?utm_content=DAF1FagcDMo&utm_campaign=designshare&utm_medium=link&utm_source=editor)
        """
    )


    st.subheader("User Data")
    with st.container(border=True):
        st.write("Input Variables for Generative AI to create hyper-personalized marketing messages")
        Name = st.text_input('Name')
        Age =  st.text_input('Age')
        Gender =  st.selectbox('Gender', ('Male', 'Female', 'LGBTQ+'), index=None, placeholder='Choose an option')
        Education =  st.selectbox('Highest level of education', ("Bachelor's degree", "Master's degree", "Doctoral degree or equivalent"), index=None, placeholder='Choose an option')
        Platform1 =  st.selectbox("The most food delivery apps (Rank 1)", ('GrabFood', 'LINEMAN Wongnai', 'Robinhood', 'Foodpanda', 'ShopeeFood'), index=None, placeholder='Choose an option')
        Platform2 =  st.selectbox("The most food delivery apps (Rank 2)", ('GrabFood', 'LINEMAN Wongnai', 'Robinhood', 'Foodpanda', 'ShopeeFood'), index=None, placeholder='Choose an option')
        mbti =  st.selectbox("Myers-Briggs Type Indicator (MBTI) Personality type", ('ISTJ', 'ISFJ', 'INTJ', 'INFJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'), index=None, placeholder='Choose an option')
        Personality =  st.multiselect("Please select 3 sentences from the following that best describe you", ('You enjoy trying new things.', 'You are energetic and lively.', 'You are always prepared.', 'You are helpful and considerate.', 'You have a broad range of interests.', 'You are organized and efficient.', 'You are kind and compassionate.', 'You are talkative and outgoing.', 'You are easily worried.', 'You pay attention to details.', 'You are self-conscious and sensitive.'), max_selections=3, placeholder='Choose 3 options')
        # Personality = 
        OrderFrequency =  st.selectbox("Frequency of using food delivery apps", ('less than once a month', 'once a month', '2-3 times a month', '1-2 times a week', 'almost every day', 'only when having a promotion'), index=None, placeholder='Choose an option')
        aov =  st.selectbox('Average order value when ordering food delivery', ('less than 100 THB', '100 - 199 THB', '200 - 299 THB', '300 THB or more'), index=None, placeholder='Choose an option')
        PromoFrequency =  st.selectbox('How frequently do you use a promotion code or a special offer while placing an order?', ('always (100%)', 'often (75%)', 'sometimes (50%)', 'seldom (25%)', 'never (0%)'), index=None, placeholder='Choose an option')
        FoodDish =  st.multiselect('Favorite dishes or food categories when using food delivery apps', ('Cooked to Order', 'Chicken Rice', 'Japanese Food', 'Seafood', 'Salad & Healthy Food', 'Italian Food', 'Chinese Food', 'Somtum', 'Noodle', 'Burger & Fried Chicken', 'Coffee', 'Tea & Milk Tea', 'Sweets'), placeholder='Choose at least 3 options')
        TimeWeekday =  st.multiselect('When are you likely to order on weekdays?', ('in the morning', 'at noon', 'in the afternoon', 'in the evening', 'at night', 'no order'), placeholder='(You can choose more than one)')
        TimeWeekend =  st.multiselect('When are you likely to order on weekends?', ('in the morning', 'at noon', 'in the afternoon', 'in the evening', 'at night', 'no order'), placeholder='(You can choose more than one)')
        OpenReadMKTMsg =  st.selectbox('How likely are you to open and read marketing messages from food delivery apps?', ('very unlikely', 'somewhat unlikely', 'neutral', 'somewhat likely', 'very likely'), index=None, placeholder='Choose an option')
        FavoriteMKT =  st.selectbox('What type of marketing messages from food delivery apps are you most likely to respond to?', ('Special menu price offers', 'Special delivery price offers', 'Special discount promotion code offers', 'New menu promotion'), index=None, placeholder='Choose an option')
        MKTFactor =  st.multiselect('What factors influence your decision to act upon a marketing message from a food delivery app?', ('The attractiveness of the offer', 'The relevance of the menu or cuisine', 'The credibility of the app', 'The urgency of the offer'), placeholder='(You can choose more than one)')

    st.subheader("Auto Gen-AI Message")
    with st.container(border=True):
        st.write("Here is an output from Generative AI")
        st.write(st.secrets["dify_key"])

if __name__ == "__main__":
    run()
