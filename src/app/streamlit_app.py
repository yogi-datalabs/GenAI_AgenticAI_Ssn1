import os
from dotenv import load_dotenv

import streamlit as st
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Initialize embedding model
embedding_model = OpenAIEmbeddings()

# Load existing vector database
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

st.set_page_config(page_title="RAG Question Answering Assistant", layout="wide")

st.title("RAG Question Answering Assistant")
st.write("Ask a question based on the uploaded documents.")

query = st.text_input("Enter your question:")

if st.button("Get Answer") and query:

    # Retrieve relevant chunks
    #retrieved_docs = vector_db.similarity_search(query, k=3)
    retrieved_docs = vector_db.max_marginal_relevance_search(query, k=10, fetch_k=20)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    rag_prompt = f"""
    You are a document-based assistant.

    Use ONLY the context provided below.

    If the question asks for a list, extract and present the list clearly from the context.
    If the answer is not available in the context, say: "The information is not available in the provided documents."

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a reliable document assistant."},
            {"role": "user", "content": rag_prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    st.subheader("Answer")
    st.write(answer)

    with st.expander("Retrieved Context"):
        for i, doc in enumerate(retrieved_docs, 1):
            st.markdown(f"**Chunk {i}**")
            st.write(doc.page_content[:1000])
            st.write("Metadata:", doc.metadata)
            st.markdown("---")