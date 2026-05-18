import os
import sys
import streamlit as st

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

sys.path.insert(0, project_root)


from app.retrieval.vectorstore import (
    load_vectorstore,
    get_retriever_from_vectorstore
)

from app.llm.llm_initializer import initialize_llm
from app.routing.query_orchestrator import orchestrate_query
from app.routing.query_router import route_query


##########################################
# PAGE CONFIG
##########################################

st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="wide"
)


##########################################
# CACHE RESOURCES
##########################################

@st.cache_resource
def load_resources():

    llm = initialize_llm()

    vector_db = load_vectorstore(
        r"data\vectorstores\faiss_index"
    )

    retriever = get_retriever_from_vectorstore(
        vector_db
    )

    return llm, retriever


llm, retriever = load_resources()


##########################################
# SIDEBAR
##########################################

with st.sidebar:

    st.title("Enterprise AI")

    st.write("""
    Hybrid AI Assistant supporting:

    ✅ Document Question Answering (RAG)

    ✅ SQL Query Generation

    ✅ PostgreSQL Retrieval

    ✅ Hybrid Routing

    Built using:
    - LangChain
    - FAISS
    - PostgreSQL
    - OpenAI
    - Streamlit
    """)

    st.subheader("Example Questions")

    st.write("""
    • What are RBI KYC limits?

    • Explain TechNova leave policy

    • Who has highest salary?

    • Average salary by department?

    • Which employee took most leaves?
    """)


##########################################
# MAIN UI
##########################################

st.title(
    "🤖 Enterprise AI Assistant"
)

st.subheader(
    "Hybrid RAG + SQL Agent"
)

st.write(
    "Ask questions from documents or structured databases."
)


question = st.text_input(
    "Enter your question:"
)


##########################################
# SUBMIT BUTTON
##########################################

if st.button("Submit"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Thinking..."
        ):

            try:

                route = route_query(
                    question
                )

                response = orchestrate_query(
                    question,
                    llm,
                    retriever
                )


                st.success(
                    "Answer generated successfully"
                )


                st.markdown(
                    f"**Route Used:** `{route.upper()}`"
                )


                st.markdown(
                    "### Answer"
                )

                st.write(
                    response
                )


            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )