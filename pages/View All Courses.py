import streamlit as st
import pandas as pd
import json
# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->
# st.title("View All Courses")
# st.write(" Course information")

# --- Load JSON file ---
with open("./data/courses-full.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Convert JSON to DataFrame ---
if isinstance(data, list):
    # JSON is a list of dicts
    df = pd.DataFrame(data)
else:
    # JSON is a dict of dicts
    df = pd.DataFrame.from_dict(data, orient="index")

# --- Display table ---
df = df.reset_index(drop=True)
st.dataframe(df, use_container_width=True)