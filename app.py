import streamlit as st
import re
from streamlit_app import inquiries_filler

pattern = re.compile(r'[a-zA-Zა-ჰ0-9]+')
st.sidebar.header("აპლიკაციის აღწერა")
st.sidebar.write("ეს აპლიკაცია შექმნილია ლმს-ზე კითხვარის ავტომატური შევსებისათვის, რისთვისაც საჭიროა მხოლოდ ლმს-ის ავტორიზაცია")
st.header("გაიარეთ ლმს-ის ავტორიზაცია")
with st.form('input'):
    user_name = st.text_input(
        "მომხმარებელი",
        max_chars=50
    )
    password = st.text_input(
        "პაროლი",
        max_chars=50,
        type="password"
    )
    submit_button = st.form_submit_button(label='დაწყება')

if submit_button:
    inquiries_filler(user_name, password)