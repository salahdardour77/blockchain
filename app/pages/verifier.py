import streamlit as st
from pages.connection import CONTRACT

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
#hide_icons()
#hide_sidebar()
#remove_whitespaces()


form = st.form("Validate-Certificate")
tx_hash = form.text_input("Enter the Trasaction Hash")
submit = form.form_submit_button("Validate")
if submit:
    try:
        # Smart CONTRACT Call
        result = CONTRACT.functions.isVerified(tx_hash).call()
        if result:
            st.success("Certificated validated successfully!")
        else:
            st.error("Invalid Certificate ID!")
    except Exception as e:
        st.error("Error: Invalid Certificate ID!")
