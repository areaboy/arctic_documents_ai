
# Arctic & Hellosign Legal Contracts Documents AI

An AI tools that allow Businesses to analyze Legal Contract Documents for data Translation, Summarisation, Sentiments ,Keywords, Topics and Entity Analysis leveraging **Streamlit, Snowflake Arctic & Hellosign API**

# How we built it

 Built in Python leveraging **Streamlit, Hellosign API and Snowflake Arctic AI Models**
 
# Technology Used

**1.) Streamlit**

**2.) Snowflake Arctic AI Model**

**3.) Dropbox Hellosign API ( https://www.hellosign.com/ and https://developers.hellosign.com/)**

**4.) Pdf Text Extraction tools(PDFMiner): https://github.com/pdfminer/pdfminer.six**


# Deploying the Application Online

visit **https://share.streamlit.io/** to deploy your application online from github.

Click Create App and select the app from Github.

Very important, When deploying the application online, at **Advance Settings** select **Python version 3.8**

and at **Secrets**, enter your **replicate api** token like **REPLICATE_API_TOKEN = "your replicate api token goes here"**

and then click on **Save** Button. Finally click on **Deploy** button and you are done.


# Running the Application Locally.

Am using using **window 7 OS** and I utilize this tutorial link: **https://docs.streamlit.io/get-started/installation/command-line**

1.) Download the Application from Github and unzip it. then locate **arctic_documents_ai/.streamlit/secrets.toml** files to update your

**Replicate API Token.** You can obtain it from **https://replicate.com**

2.) on windows, open **command prompt** and cd into the application directory eg. **cd arctic_documents_ai**

3.) Next In your terminal, type: **python -m venv .venv** and A folder named **.venv** will appear in your project. This directory is where your virtual environment and its dependencies are installed.

4.) next In your terminal, activate your environment with one of the following commands, depending on your operating system.

**Windows command prompt**

.venv\Scripts\activate.bat

**Windows PowerShell**

.venv\Scripts\Activate.ps1

**macOS and Linux**

source .venv/bin/activate

Now since am using **windows**, you will have to type in your terminal **.venv\Scripts\activate.bat**

Once activated, you will see your environment name in parentheses before your prompt. **"(.venv)"**

It is time to Install all the dependencies

5.) still in your activated command prompt terminal run one after another

**pip install streamlit**

**pip install replicate**

**pip install pdfminer.six** 

6.) To start the application, still in your activated command prompt terminal run

**streamlit run app.py**

