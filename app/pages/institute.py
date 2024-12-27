from pages.connection import CONTRACT, w3
import hashlib
import json
import os
from dotenv import load_dotenv
import requests
import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

load_dotenv()


def upload_to_ipfs(file_path):
    # Set up the IPFS API endpoint and headers
    api_url = 'http://127.0.0.1:5001/api/v0/add'


    # Prepare the file for upload
    with open(file_path, "rb") as file:
        file_name = os.path.basename(file_path)

        # Read the file content
        file_content = file.read()

        # Prepare the files dictionary
        files = {"file": (file_name, file_content)}

        # Make the request
        response = requests.post(api_url, files=files, timeout=100)

        # Parse the response
        result = json.loads(response.text)
        if "Hash" in result:
            hash = result["Hash"]
            print(f"File uploaded to IPFS. IPFS Hash: {hash}")
            return hash
        else:
            print(f"Error uploading to IPFS: {result.get('error', 'Unknown error')}")
            return None


form = st.form("Generate-Certificate")
candidate_name = form.text_input(label="Name")
speciality = form.text_input(label="Speciality")
school_name = form.text_input(label="School Name")

pdf = st.file_uploader("Upload Certificate")

submit = form.form_submit_button("Submit")
if submit and pdf:
    # Ensure the folder exists
    os.makedirs("pages\\uploaded_files", exist_ok=True)
    local_file_path = os.path.join("pages\\uploaded_files", pdf.name)

    with open(local_file_path, "wb") as file:
        file.write(pdf.getvalue())

    pdf_name = pdf.name
    # Upload the PDF to IPFS
    ipfs_hash = upload_to_ipfs(local_file_path)
    data_to_hash = f"{candidate_name}{speciality}{school_name}".encode('utf-8')
    uid = hashlib.sha256(data_to_hash).hexdigest()

    # Smart CONTRACT Call
    tx_hash = CONTRACT.functions.mintCertificate(uid, candidate_name, speciality, school_name, ipfs_hash).transact(
        {'from': w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Check the status of the transaction (1 = success, 0 = failure)
    if receipt.status == 1:
        st.success(f"Certificate successfully generated with IPFS Hash: {ipfs_hash}, {tx_hash}")
    else:
        st.error("Transaction failed. Please try again.")

