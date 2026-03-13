import streamlit as st
import requests

API = "https://smart-legal-document-manager-production.up.railway.app"

st.title("Smart Legal Document Manager")

menu = st.sidebar.selectbox(
    "Choose Action",
    ["Create Document", "Update Document", "Compare Versions"]
)

if menu == "Create Document":

    st.header("Create Document")

    title = st.text_input("Title")
    content = st.text_area("Content")
    user = st.text_input("User")

    if st.button("Create"):
        res = requests.post(
            f"{API}/documents/",
            json={
                "title": title,
                "content": content,
                "user": user
            }
        )
        st.json(res.json())


elif menu == "Update Document":

    st.header("Update Document")

    doc_id = st.number_input("Document ID", step=1)
    content = st.text_area("New Content")
    user = st.text_input("User")

    if st.button("Update"):
        res = requests.put(
            f"{API}/documents/{doc_id}",
            json={
                "content": content,
                "user": user
            }
        )
        st.json(res.json())


elif menu == "Compare Versions":

    st.header("Compare Versions")

    doc_id = st.number_input("Document ID", step=1)
    v1 = st.number_input("Version 1", step=1)
    v2 = st.number_input("Version 2", step=1)

    if st.button("Compare"):
        res = requests.get(
            f"{API}/documents/{doc_id}/compare?v1={v1}&v2={v2}"
        )
        st.json(res.json())