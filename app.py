import streamlit as st
import replicate
import os
import requests
import json
import streamlit.components.v1 as components
from streamlit.components.v1 import html





st.header("Arctic & Hellosign Legal Contracts Documents AI")

st.write("An AI Tools that help **Businesses, Companies etc.** to easily **simplyfy, manage and analyze Documents and other Legal Contract Documents**")

st.info("It allow Users to easily analyze **Long Text Messages, Notes, PDF Documents, Legal Contracts Documents etc.** for Text **Translations, Summarisation, Sentiments ,Keywords, Topics and Entity Analysis** leveraging **Streamlit, Snowflake Arctic AI & Dropbox/Hellosign API**")

st.warning("You can also  Send Documents for Signing leveraging **Dropbox/Hellosign API**")





st.subheader("Arctic AI Sentiments Analysis")

st.write("The Applications leverages **Arctic AI Sentiments Analysis** to run sentimental analysis of data to  breakdown the Long Text Messages, Long Notes, Documents Contents etc. to more **easy, understandable and digest-able form**. It analyzes each Documents for sentiments **Positivity, negativity or neutrality statements**")

st.subheader("Arctic AI Entities Analysis")
st.write("The Applications leverages **Arctic AI Entity Analysis** to detect, analyze and list all the **People, Persons, Organizations, Companies and all the entities** involves in the Text Messages, Contracts Documents etc.")




st.subheader("Arctic AI Keyword Analysis")
st.write("The Applications leverages **Arctic AI Keyword Analysis** to pin-point all the **Keywords, keyphrases** involved in the Text Messages, Contracts Documents etc.")

st.subheader("Arctic AI Summary Analysis")
st.write("The Applications leverages **Arctic AI Summarizer Analysis** to ultimately provide the **Summary** of the  Long Text Messages, Notes, Contracts Documents etc. and thereby saving **Time and Energy** ")





st.subheader("Arctic AI Topic Analysis")
st.write("The Applications leverages **Arctic AI Topic Analysis** to provides insights into **Relevants  Topics** while analyzing  Long Text Messages, Notes, Contracts Documents etc. and thereby making Documents comprehension more easier.")

 

st.subheader("Arctic AI Language Translator")
st.write("Application leverages **Arctic AI Translate Option** to allow user to **translate** Long Text Messages, extracted text documents etc. from one language to another **to help mitigate language barrier** while analyzing the documents..")