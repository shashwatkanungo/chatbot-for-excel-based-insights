import pandas as pd

def load_and_clean_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    return df
