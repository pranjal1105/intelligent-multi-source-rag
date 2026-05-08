from langchain_text_splitters import RecursiveCharacterTextSplitter

def recursive_chunking(docs):
    try:
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
        chunks=text_splitter.split_documents(docs)
        return chunks
    except Exception as e:
        print("Could not perform recursive chunking")