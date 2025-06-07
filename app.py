import streamlit as st
from utils.data_loader import load_and_clean_excel
from utils.llm_utils import generate_analysis_code
from utils.safe_exec import execute_code
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Excel Insight Chatbot", layout="wide")
st.title("Excel Insight Chatbot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared!")


uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = load_and_clean_excel(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())


    if st.session_state.chat_history:
        st.subheader("Chat History")
        for i, chat in enumerate(st.session_state.chat_history):
            with st.expander(f"{i+1}. Question: {chat['question']}"):
                st.code(chat["code"], language="python")
                if chat["fig"]:
                    st.pyplot(chat["fig"])
                elif isinstance(chat["result"], pd.DataFrame):
                    st.dataframe(chat["result"])
                elif isinstance(chat["result"], (int, float)):
                    st.metric(label="Final Answer", value=chat["result"])
                else:
                    st.success(f"{chat['result']}")


    query = st.text_input("Ask a question about your data:")

    if query:
        with st.spinner("Thinking..."):
            code = generate_analysis_code(df, query)
            result, fig = execute_code(code, df)


            st.session_state.chat_history.append({
                "question": query,
                "code": code,
                "result": result,
                "fig": fig
            })


            st.subheader("Latest Answer")

            if st.checkbox("Show Generated Code"):
                st.code(code, language="python")

            if fig:
                st.pyplot(fig)
                plt.clf()
            elif isinstance(result, pd.DataFrame):
                st.dataframe(result)
            elif isinstance(result, (int, float)):
                st.metric(label="Final Answer", value=result)
            else:
                st.success(f"{result}")
