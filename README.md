# 📊 Excel Insight Chatbot

A powerful Streamlit-based chatbot that lets you upload Excel files and ask analytical questions like *"What is the average income?"*, *"Show me a histogram of sales?"*, and more. The chatbot interprets your query, writes the required Python code using OpenAI’s API, and executes it—returning numerical answers, plots, or tables in response.

### 🚀 Live App
Check it out live here:  
🔗 [Excel Insight Chatbot on Streamlit Cloud](https://chatbot-for-excel-based-insightsgit-z6gzkmbsc2y6hyzhzcggcj.streamlit.app/)

---

## 📂 Features

- 📁 Upload any `.xlsx` Excel file.
- 💬 Ask natural language questions like:
  - "What is the average salary?"
  - "Plot the monthly revenue trend."
- 🧠 Uses OpenAI's GPT-4o to dynamically generate clean, executable `pandas` + `matplotlib` code.
- 🧼 Handles missing values gracefully.
- 📊 Returns charts, metrics, and data tables as appropriate.
- ♻️ Maintains chat history and allows you to clear it.
- 🔒 Keeps your API key private via `.env` file.

---

## 🛠️ Project Structure

├── app.py # Streamlit frontend
├── utils/
│ ├── data_loader.py # Excel file loading & cleaning
│ ├── llm_utils.py # Code generation using OpenAI
│ └── safe_exec.py # Secure code execution engine
├── .env.example # Example environment variables
├── requirements.txt # Python dependencies


---

## 📦 Installation

1. **Clone the Repository:**


git clone https://github.com/yourusername/excel-insight-chatbot.git

cd excel-insight-chatbot

2. Install Dependencies:

(Make sure you are using Python 3.8+)

pip install -r requirements.txt


3. Set up Environment Variables

   Rename .env.example to .env and add your OpenAI API key.

   cp .env.example .env
   
Edit  .env and paste your key:


OPENAI_API_KEY=sk-xxxxxx...


#### ▶️ Run Locally

#### streamlit run app.py

Then open http://localhost:8501 in your browser.



### 🤖 How It Works
Upload Excel File

Reads the file using pandas, and standardizes column names.

❓Ask a Question

 Converts your natural language question into Python code using GPT-4o.

🧠Code Execution

The code is safely executed to produce a result: text, plot, metric, or dataframe.

🧼 Handles Errors & Missing Values

Invalid or null data is gracefully managed.

🔐 Environment Variables

This project uses environment variables to keep your API keys secure.


###### # .env
OPENAI_API_KEY=your_openai_key_here

✅ Example Questions You Can Ask

“What is the average order value?”

“Show a bar chart of sales by category.”

“How many missing values are in each column?”

“Show the distribution of invoice amounts.”



All execution is done locally in memory and not stored.

