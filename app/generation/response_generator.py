import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def format_context(retrieved_chunks):
    context=""
    for chunk in retrieved_chunks:
        context+=f"Source: {chunk.metadata['source']}\n"
        context+=f"Chunk Index: {chunk.metadata['chunk_index']}\n"
        context+=chunk.page_content
        context+="\n\n"
    return context

def build_prompt(question,context):
    prompt = f"""You are a helpful assistant that answers questions based on the provided context. 
    Answer ONLY using the provided context.
    If the answer cannot be found in the context, say:
    "I could not find enough information."
    Do not use any information that is not in the context. 
    If the question is not related to the context, say you don't know.

    Context:
    {context}

    Question: {question}
    Answer:"""
    return prompt

def generate_response(llm,question, retrieved_chunks):
    logger.info("Formatting context for response generation...")
    context = format_context(retrieved_chunks)
    logger.info("Building prompt for LLM...")
    prompt = build_prompt(question, context)
    response = llm.invoke(prompt)
    return response.content