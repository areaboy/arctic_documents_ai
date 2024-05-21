import streamlit as st
import replicate
import os
import requests
import json
import re
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from pdfminer.high_level import extract_text

import tempfile

st.header("Send Documents for Signing with Hellosign")
st.write("Easily Send and Sign **PDF Legal Contract Documents** leveraging **Hellosign API**")
st.caption('To obtain Hellosign API Key [Sgnup Here](https://developers.hellosign.com/)')



# Pass Text Data in a Session State
if "event_result" not in st.session_state:
    st.session_state.event_result = ""
   
def clear_response_history():
    st.session_state.event_result =''


# Process Documents for Sending Via Hellosign API

def process_data(filename_docs,hellosign_api,document_title,document_subject,document_message,signer_name,signer_email): 
 if hellosign_api =='':
     st.error("**Hellosign API token is empty**")
 elif filename_docs == "":  
        st.error(f"Documents Filename cannot be empty....")
 elif document_title == "":  
        st.error(f"Documents Title cannot be empty....")
 elif document_subject == "":  
        st.error(f"Documents Subject cannot be empty....")
 elif document_message == "":  
        st.error(f"Documents Message cannot be empty....")
 elif signer_name == "":  
        st.error(f"Documents Signer Name cannot be empty....")
 elif signer_email == "":  
        st.error(f"Documents Signer Email cannot be empty....")

 else:
    temp_dir ='temp_dir'
    file_pathx = temp_dir + "/" + filename_docs 
    
    files = [
    ('files[0]', open(file_pathx, 'rb')),
    ('title', (None, document_title)),
    ('subject', (None, document_subject)),
    ('message', (None, document_message)),
    ('signers[0][email_address]', (None, signer_email)),
    ('signers[0][name]', (None, signer_name)),
    ('signers[0][order]', (None, '0')),
   
    ('metadata[custom_id]', (None, '1234')),
    ('metadata[custom_text]', (None, 'NDA #9')),
    ('signing_options[draw]', (None, '1')),
    ('signing_options[type]', (None, '1')),
    ('signing_options[upload]', (None, '1')),
    ('signing_options[phone]', (None, '1')),
    ('signing_options[default_type]', (None, 'draw')),
    ('test_mode', (None, '1')),
    ]

    response = requests.post('https://api.hellosign.com/v3/signature_request/send', files=files, auth=(hellosign_api, ':'))
    if response.status_code == 400:
     st.error("**Hellosign API Bad Request**")
    elif response.status_code == 401:  
        st.error(f"Hellosign API Unauthorized")
    elif response.status_code == 402:  
        st.error(f"Hellosign Payment Required....")
    elif response.status_code == 403:  
        st.error(f" Access to Hellosign API Forbidden..")
    elif response.status_code == 409:  
        st.error(f" Hellosign API Conflicts....")
    elif response.status_code == 429:  
        st.error(f"Exceeds Hellosign API Call Rate Limit....")
    else:  
        st.success(f" Documents Successfully Sent to Recipients/Signers Email Address")
 
        html_string = f'''
        <script language="javascript">
          alert('Documents Successfully Sent to Recipients/Signers Email Address.');
        </script>
        '''
        components.html(html_string)
        st.button('Clear Response..', on_click=clear_response_history)



uploaded_file = st.file_uploader("Upload PDF Documents for Signing & **Hellosign Details Will be Displayed..**", type="pdf")
if uploaded_file:

        # temp_dir = tempfile.mkdtemp()
        temp_dir ='temp_dir'
        path = os.path.join(temp_dir, uploaded_file.name)
        with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())

        st.info(f"Documents Files Initialized. You can now Send Documents for Signing. Fill Information Below...")
        html_string = f'''
        <script language="javascript">
          alert('Documents Files Initialized. You can now Send Documents for Signing. Fill Information Below...');
        </script>
    
        '''

        filename_docs = uploaded_file.name
        hellosign_api = st.text_input('Enter Hellosign API token:',  type='password')
        document_title = st.text_input('Enter Document Title:', 'Eg. NDA with Acme Co.')
        document_subject = st.text_input('Enter Document Subject:', 'Eg. The NDA we talked about')
        document_message = st.text_area('Enter Document Message:', 'Eg. Please sign this NDA and then we can discuss more. Let me know if you have any questions')

         
        st.info(f" Enter Documents Signers Details")
        signer_name = st.text_input('Enter Signer Name:')
        signer_email = st.text_input('Enter Signer Email:')
        st.button('Send Documents for Signing.', on_click=process_data, args=[filename_docs,hellosign_api,document_title,document_subject,document_message,signer_name,signer_email])
 
        

