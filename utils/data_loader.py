import pandas as pd

def load_and_clean_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)  # loading the excel file 
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]   # cleaning the column names by replace spaces with underline, convert to lowercase and remove leading spaces
    return df
