from app.ingestion.ingestion_orchestrator import run_ingestion_pipeline
from app.retrieval.vectorstore import add_to_vectorstore, create_vectorstore, save_vectorstore


source_technova={"path":r"data\raw\TechNova_HR_Policy_Document.md"
        ,"type":"markdown"
        ,"source_name":"TechNova HR Policy Document"}

source_rbi_circular={"path":r"data\raw\RBI circular.pdf"
           ,"type":"pdf"
           ,"source_name":"RBI Circular"}

chunks_md=run_ingestion_pipeline(source_technova)
chunks_pdf=run_ingestion_pipeline(source_rbi_circular)

#create vector db
vectorstore=create_vectorstore(chunks_md)
#add pdf chunks to vector db
add_to_vectorstore(vectorstore, chunks_pdf)

#save vectorstore to disk
save_vectorstore(vectorstore, r"data\vectorstores\faiss_index")