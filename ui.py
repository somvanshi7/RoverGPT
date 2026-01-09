import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RoverGPT", layout="centered")

st.title("🤖 RoverGPT")
st.caption("Ask questions from your PDF knowledge base")

question = st.text_input("Ask a question:")

if st.button("Ask") and question.strip():
    with st.spinner("Thinking..."):
        response = requests.post(
            BACKEND_URL,
            json={"question": question},
            timeout=120
        )

        if response.status_code == 200:
            data = response.json()
            st.subheader("Answer")
            st.write(data["answer"])

            with st.expander("Retrieved Context"):
                for i, chunk in enumerate(data["context"], 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.write(chunk)
        else:
            st.error("Backend error")
