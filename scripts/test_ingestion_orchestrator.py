from app.ingestion.ingestion_orchestrator import run_ingestion_pipeline
from app.retrieval.vectorstore import add_to_vectorstore, create_vectorstore, debug_retrieval, get_retriever_from_vectorstore

source_md={"path":r"data\raw\TechNova_HR_Policy_Document.md"
        ,"type":"markdown"
        ,"source_name":"TechNova HR Policy Document"}

source_pdf={"path":r"data\raw\RBI circular.pdf"
           ,"type":"pdf"
           ,"source_name":"RBI Circular"}

chunks_md=run_ingestion_pipeline(source_md)
chunks_pdf=run_ingestion_pipeline(source_pdf)

#create vector db
vectorstore=create_vectorstore(chunks_md)

#add chunks from pdf to vector db
# add_to_vectorstore(vectorstore, chunks_pdf)

#get retriever from vector db
retriever=get_retriever_from_vectorstore(vectorstore)

#test retrieval
query_md="What are the employee leave rules at TechNova?"
query_pdf="What are RBI loan guidelines?"
# retrieved_chunks_md=retriever.invoke(query_md)
# retrieved_chunks_pdf=retriever.invoke(query_pdf)

debug_retrieval(vectorstore, query_md)

# print("Retrieved chunks for Markdown source:")
# for chunk in retrieved_chunks_md:
#     print(chunk.page_content)
#     print("------")
#     print(chunk.metadata)

# print("\nRetrieved chunks for PDF source:")
# for chunk in retrieved_chunks_pdf:
#     print(chunk.page_content)
#     print("------")
#     print(chunk.metadata)

