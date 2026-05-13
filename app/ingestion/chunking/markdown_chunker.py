from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.settings import MARKDOWN_CHUNK_OVERLAP,MARKDOWN_CHUNK_SIZE
def recursive_markdown_chunker(docs):
    try:
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=MARKDOWN_CHUNK_SIZE,chunk_overlap=MARKDOWN_CHUNK_OVERLAP)
        chunks=text_splitter.split_documents(docs)
        return chunks
    except Exception as e:
        print("Could not perform recursive chunking")