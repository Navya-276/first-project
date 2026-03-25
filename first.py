
import streamlit as st
with st.form("Form"):
    st.title("Regestration form")
    col1,col2=st.columns(2)
    fname=col1.text_input("First Name")
    lname=col2.text_input("Last Name")
    email=st.text_input("Enter your email")
    password=st.text_input("Enter Password",type="password")
    confirm_pwd=st.text_input("Confirm Password",type="password")
    address=st.text_area("enetr your address")
    c1,c2=st.columns(2)
    sdate=c1.date_input("Start date")
    ldate=c2.date_input("Last date")
    submit=st.form_submit_button("Submit")
if submit:
    st.write(email)

