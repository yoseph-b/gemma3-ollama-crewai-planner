import streamlit as st
import os
from crew_config import crew

st.set_page_config(page_title="AI App Generator", layout="wide")
st.title("🤖 Autonomous AI App Builder")

with st.form("app_builder_form"):
    prompt = st.text_area("🧠 Describe the app you want to build:", height=200,
                          placeholder="E.g., A blogging platform with user login and commenting...")
    submitted = st.form_submit_button("🚀 Build App")

if submitted and prompt:
    st.info("⚙️ Generating your app... please wait ⏳")
    crew.kickoff(inputs={"user_prompt": prompt})
    st.success("✅ App generation complete!")

    st.header("📂 Generated Code Outputs")

    base_path = "./generated"
    categories = ["planner", "frontend", "backend", "database", "deploy"]

    for category in categories:
        file_path = os.path.join(base_path, category, "output.txt")
        if os.path.exists(file_path):
            with st.expander(f"📁 {category.capitalize()} Output"):
                with open(file_path, "r", encoding="utf-8") as f:
                    st.code(f.read(), language="markdown")
        else:
            st.warning(f"No output yet for {category}")
