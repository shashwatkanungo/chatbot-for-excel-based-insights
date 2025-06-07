from openai import OpenAI
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_analysis_code(df: pd.DataFrame, question: str) -> str:
    sample = df.head(3).to_markdown(index=False)

    context = f"""
You are a data analyst. A user has uploaded a DataFrame with the following structure:

{sample}

Write clean and executable Python code using pandas to answer the question:

"{question}"

Guidelines:
- The DataFrame is named `df`
- Handle missing (null) values gracefully using pandas (e.g., dropna(), fillna(), etc.) if relevant
- If a plot is appropriate, use matplotlib (already imported as plt)
- Do not use print() or markdown — just Python code
- The final line should be an expression to evaluate (e.g., a variable or a plot)

Only return plain Python code — no comments or formatting.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You write and analyze pandas code."},
            {"role": "user", "content": context}
        ],
        temperature=0,
    )

    # cleaning the output because of commas
    raw_code = response.choices[0].message.content.strip()

    if raw_code.startswith("```"):
        # Remove the first and last triple backticks
        raw_code = raw_code.strip("`")
        raw_code = raw_code.split("\n", 1)[1] if "\n" in raw_code else ""

    return raw_code.strip()
