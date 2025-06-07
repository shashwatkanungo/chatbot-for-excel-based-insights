# Excel Insight Chatbot

[![Streamlit](https://img.shields.io/badge/streamlit-cloud-blue?logo=streamlit)](https://chatbot-for-excel-based-insightsgit-z6gzkmbsc2y6hyzhzcggcj.streamlit.app/)

## Project Overview

The **Excel Insight Chatbot** is an interactive web app that allows users to upload Excel files and ask natural language questions about their data. Leveraging OpenAI GPT-4 for code generation, Pandas for data handling, and Matplotlib for visualization, the chatbot dynamically analyzes the uploaded dataset and returns insightful answers, tables, and detailed visualizations.

The project is deployed on [Streamlit Cloud](https://chatbot-for-excel-based-insightsgit-z6gzkmbsc2y6hyzhzcggcj.streamlit.app/).

---

## Live Demo

👉 [Try the Excel Insight Chatbot here](https://chatbot-for-excel-based-insightsgit-z6gzkmbsc2y6hyzhzcggcj.streamlit.app/)

---

## Features

- Upload Excel (.xlsx) files with automatic cleaning of column names.
- Ask any question in natural language about your dataset.
- AI-powered Python code generation to analyze data dynamically.
- Thorough visualization support using Matplotlib for insightful charts.
- Display of results as text, DataFrames, or rich plots.
- Interactive chat history to keep track of queries and answers.
- Safe and sandboxed execution of generated Python code.
- Clear error handling with detailed feedback.

---

## How It Works

1. **Upload Excel File:** User uploads an Excel file, which is read into a cleaned Pandas DataFrame.
2. **Ask Questions:** User inputs natural language questions about the data.
3. **Code Generation:** The app uses OpenAI GPT-4 to generate executable Python code tailored to answer the question using the DataFrame.
4. **Execute & Visualize:** The generated code runs safely in a sandboxed environment, producing numerical answers, data tables, or Matplotlib visualizations.
5. **Display Results:** The chatbot presents the output below the query input. Plots are rendered inline.
6. **Chat History:** All previous questions, generated code, and results are stored and displayed in session state.

---

## Project Structure

├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── utils/
│ ├── data_loader.py # Excel file loading and cleaning
│ ├── llm_utils.py # OpenAI GPT-4 code generation logic
│ └── safe_exec.py # Safe execution of Python code with matplotlib support
├── README.md # This documentation file

---

## Installation & Setup (Local Development)

1. Clone this repository:
   
   git clone <your-repo-url>
   cd chatbot-for-excel-based-insights
   
3. Create and activate a python virtual environment:
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate

4. Installing dependencies:
   pip install -r requirements.txt

5. Run the Streamlit app locally:
   streamlit run app.py


Dependencies
Streamlit: Web app framework for interactive data apps

OpenAI Python SDK: For GPT-4 API calls

Pandas: Data manipulation and cleaning

Matplotlib: Visualization and plotting support

python-dotenv: Load environment variables from .env file

Usage Instructions
Visit the deployed app or run locally.

Upload an Excel .xlsx file using the file uploader.

Ask questions in plain English about your data (e.g., "Show me the average sales by region").

View the AI-generated Python code and its output—results can be tables, numeric metrics, or charts.

Scroll through your chat history with previous questions and answers.

Use the Clear Chat History button to reset the session anytime.

Visualization Capabilities
This chatbot goes beyond simple textual answers and can generate thorough visualizations to help you understand your data better.

It dynamically generates matplotlib plots such as bar charts, line plots, histograms, scatter plots, and more based on your query.

Visualizations are displayed inline beneath the relevant question.

This makes data exploration intuitive and visually rich without writing any code yourself.

Code Safety & Execution
The app executes the generated Python code in a sandboxed environment limited to df (your DataFrame), pd (Pandas), and plt (Matplotlib).

Errors during code execution are captured and shown clearly, so you get meaningful feedback.

Generated plots are automatically captured and rendered in Streamlit.
