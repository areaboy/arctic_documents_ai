import streamlit as st
import replicate
import os
import requests
import json
import re
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from pdfminer.high_level import extract_text


st.header("Documents & Files Translation")
st.write("Easily Translate **PDF Legal Contract Documents, Long Text Messages, Lecture Notes etc.** to help prevent **Language Barrier**")
st.info("Translate from **English** to any other Languages in the World.....")

# Pass Text Data in a Session State
if "event_result" not in st.session_state:
    st.session_state.event_result = ""
    
# Pass Extracted PDF Text Data in a Session State
if "event_result_docs" not in st.session_state:
    st.session_state.event_result_docs = ""
    


# Replicate API Credentials
with st.sidebar:
    st.title('Snowflake Arctic  API Settings')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your Replicate API token.')
            st.markdown("**Don't have an API token?** Head over to [Replicate](https://replicate.com) to sign up for one.")

    os.environ['REPLICATE_API_TOKEN'] = replicate_api
    st.subheader("Adjust model parameters")
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.3, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)


# Pass texted data Session State
# if st.session_state.event_result != "":
   # data_session = st.text_input('.', st.session_state.event_result)



   

def clear_response_history():
    st.session_state.event_result =''



def clear_response_history_docs():
    st.session_state.event_result_docs =''


st.header(f" Text Translation ")
text_prompt_data= st.text_area('Enter Text to Translate' )
translate_to = st.selectbox('Select Language to Translate To: ', ['Arabic','Bengali','Bosnian','Chinese','Croatian','Czech','Danish','Dutch - Nederlands','Estonian','Finnish','French','Galician','Georgian','German','Greek'])


#  Process Text Data
def process_data(): 
 os.environ['REPLICATE_API_TOKEN'] = replicate_api
 if replicate_api =='':
     st.markdown("**Replicate API token is empty**")
 elif text_prompt_data == "":  
        st.error(f" Text to Translate cannot be empty....")
 elif translate_to == "":  
        st.error(f" Language to Translate to cannot be empty....")

 else:
    #   allow only alphanumeric characters, commas, dots, spaces
    data_regex = re.sub(r'[^A-Za-z0-9, .]', '', text_prompt_data)

    text_prompt_data_process = "translate this text '" + data_regex + "' to " + translate_to + " ."
    # text_prompt_data_process = "translate this text '" + data_regex + "'  "

    # st.write(f"{text_prompt_data_process}")
    os.environ['REPLICATE_API_TOKEN'] = replicate_api  
    # with st.spinner("please wait....."):      
    query = []
    for event in replicate.stream(
    "snowflake/snowflake-arctic-instruct",
    input={
        "top_k": 50,
        "top_p": top_p,
        "prompt": text_prompt_data_process,
        "temperature": temperature,
        "max_new_tokens": 512,
        "min_new_tokens": 0,
        "stop_sequences": "<|im_end|>",
        "prompt_template": "<|im_start|>system\nYou're a helpful assistant<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n\n<|im_start|>assistant\n",
        "presence_penalty": 1.15,
        "frequency_penalty": 0.2
    },
    ):
    
       # st.write(str(event), end="")
       # print(str(event), end="")
       query.append(event.data)
 

    for res in query:
     result_query = "".join(query)
     # result_query = "\n".join(query)
    st.session_state.event_result = result_query
    st.success(f" **Arctic AI Translation Result:** {st.session_state.event_result} ")
    # Update the session_state with the event result
    st.session_state.event_result = result_query
    data_regex2 = re.sub(r'[^A-Za-z0-9, .]', '', st.session_state.event_result)
    html_string = f'''
        
    <script language="javascript">
          alert('Arctic AI Translation Analysis Successful.. Please Scroll Up.');
        
    </script>
    
    '''
    components.html(html_string)
    st.button('Clear AI Response', on_click=clear_response_history)

st.button('Translate Text', on_click=process_data)




# Process PDF Text Documents

def process_data_docs(text_prompt_data_docs, translate_to_docs): 
 os.environ['REPLICATE_API_TOKEN'] = replicate_api
 if replicate_api =='':
     st.markdown("**Replicate API token is empty**")
 elif text_prompt_data_docs == "":  
        st.error(f" PDF Text Documents to Translate cannot be empty....")
 elif translate_to_docs == "":  
        st.error(f"  Language to Translate to cannot be empty....")

 else:
    #   allow only alphanumeric characters, commas, dots, spaces
    data_regex = re.sub(r'[^A-Za-z0-9, .]', '', text_prompt_data_docs)

    text_prompt_data_process = "translate this text '" + data_regex + "' to " + translate_to_docs + " ."
    # text_prompt_data_process = "translate this text '" + text_prompt_data_docs + "'  "
    os.environ['REPLICATE_API_TOKEN'] = replicate_api  
    # with st.spinner("please wait....."):      
    query = []
    for event in replicate.stream(
    "snowflake/snowflake-arctic-instruct",
    input={
        "top_k": 50,
        "top_p": top_p,
        "prompt": text_prompt_data_process,
        "temperature": temperature,
        "max_new_tokens": 512,
        "min_new_tokens": 0,
        "stop_sequences": "<|im_end|>",
        "prompt_template": "<|im_start|>system\nYou're a helpful assistant<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n\n<|im_start|>assistant\n",
        "presence_penalty": 1.15,
        "frequency_penalty": 0.2
    },
    ):
    
       # st.write(str(event), end="")
       # print(str(event), end="")
       query.append(event.data)
 

    for res in query:
     result_query = "".join(query)
     # result_query = "\n".join(query)
    st.session_state.event_result = result_query
    st.success(f" **Arctic AI Translation Response:** {st.session_state.event_result} ")
    # Update the session_state with the event result
    st.session_state.event_result = result_query
    html_string = f'''
        
   <script language="javascript">
          alert('Arctic AI Translation Analysis Successful.. Please Scroll Up.');
        
    </script>
    
    '''
    components.html(html_string)
    st.button('Clear AI Response..', on_click=clear_response_history_docs)









st.header(f" PDF Documents & Files Translation ")


uploaded_file = st.file_uploader("Choose a pdf file", "pdf")
if uploaded_file is not None:
    fx = extract_text(uploaded_file)
    st.success("PDF File Successfully Extracted. You Can Now Translate")
     # Update the session_state with the event result
    st.session_state.event_result_docs = fx
    text_prompt_data_docs= st.text_area('Extracted PDF Text to Translate', st.session_state.event_result_docs )
    translate_to_docs = st.selectbox('Select Language to Translate to: ', ['Arabic','Bengali','Bosnian','Chinese','Croatian','Czech','Danish','Dutch - Nederlands','Estonian','Finnish','French','Galician','Georgian','German','Greek'])

    
    st.button('Translate PDF Documents', on_click=process_data_docs, args=[text_prompt_data_docs, translate_to_docs])
    st.button('Clear AI Response.', on_click=clear_response_history_docs)
