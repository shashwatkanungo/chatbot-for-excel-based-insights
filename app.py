import streamlit as st
from utils.data_loader import load_and_clean_excel
from utils.llm_utils import generate_analysis_code
from utils.safe_exec import execute_code
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Excel Insight Chatbot", layout="wide")   # setting the page title and the layout 
st.title("Excel Insight Chatbot")


if "chat_history" not in st.session_state:  # initializing the chat history
    st.session_state.chat_history = []   

if st.button("Clear Chat History"):   # adding a clear history button 
    st.session_state.chat_history = []
    st.success("Chat history cleared!")


uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])   # used to upload the file

if uploaded_file:
    df = load_and_clean_excel(uploaded_file)   # if the file is uploaded, it passes through the data cleaners 
    st.subheader("Preview of Uploaded Data") # also this is for a little preview of top 5 
    st.dataframe(df.head())

    # Show chat history
    if st.session_state.chat_history:
        st.subheader("Chat History")  # if chat history is present it will display here
        for i, chat in enumerate(st.session_state.chat_history):
            with st.expander(f"{i+1}. Question: {chat['question']}"):
                st.code(chat["code"], language="python")
                if chat["fig"]:
                    st.pyplot(chat["fig"])
                elif isinstance(chat["result"], pd.DataFrame):
                    st.dataframe(chat["result"])
                elif isinstance(chat["result"], (int, float)):
                    st.metric(label="Final Answer", value=chat["result"])   # showing the chat history with everything like the prompt, the response the viz and the result
                else:
                    st.success(f"{chat['result']}")


    query = st.text_input("Ask a question about your data:")  

    if query:
        with st.spinner("Thinking..."):
            code = generate_analysis_code(df, query)  # sending data + question to the gpt prompt to generate python code
            result, fig = execute_code(code, df) # executing the code


            st.session_state.chat_history.append({
                "question": query,
                "code": code,
                "result": result,
                "fig": fig
            })  # adding to chat history

            # Show latest result
            st.subheader("Latest Answer")   # this here shows the answer 

            if st.checkbox("Show Generated Code"):  # option to see the generated code
                st.code(code, language="python")

            if fig:
                st.pyplot(fig)
                plt.clf()    # this displays the charts if they are generated
            elif isinstance(result, pd.DataFrame):
                st.dataframe(result)
            elif isinstance(result, (int, float)):
                st.metric(label="Final Answer", value=result)  # final result
            else:
                st.success(f"{result}")
