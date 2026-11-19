import streamlit as st

st.set_page_config(page_title="Add Two Numbers", page_icon="➕")

st.title("Add Two Numbers")
st.write("Enter two numbers and click Add.")

with st.form("addition_form"):
    first_number = st.number_input(
        "Enter the first number",
        value=0.0,
        format="%.2f"
    )

    second_number = st.number_input(
        "Enter the second number",
        value=0.0,
        format="%.2f"
    )

    submitted = st.form_submit_button("Add")

if submitted:
    total = first_number + second_number
    st.success(f"Result: {first_number:g} + {second_number:g} = {total:g}")
