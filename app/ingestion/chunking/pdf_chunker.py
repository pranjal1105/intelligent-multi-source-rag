from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.settings import PDF_CHUNK_OVERLAP,PDF_CHUNK_SIZE
def recursive_pdf_chunker(docs):
    try:
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=PDF_CHUNK_SIZE,chunk_overlap=PDF_CHUNK_OVERLAP)
        chunks=text_splitter.split_documents(docs)
        return chunks
    except Exception as e:
        print("Could not perform recursive chunking")