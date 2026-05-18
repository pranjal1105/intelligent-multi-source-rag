from app.database.schema import DATABASE_NAME, TABLES
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_sql_prompt(question):
    logger.info("Building SQL prompt for the question.")
    prompt = f"""You are a helpful assistant who specialises in database engineering and generating SQL queries based on the provided question. 
    Generate a SQL query that answers the question.
    
    Generate ONLY valid PostgreSQL SQL.

    Return executable SQL only.

    Do not explain.

    Do not use markdown.

    Use only tables and columns present in the schema.

    If the question cannot be answered from the schema, return:

    "I could not generate a SQL query for this question." 

    Following are the database tables and their columns:
    Database name: {DATABASE_NAME}
    """
    for table_name, table_info in TABLES.items():
        prompt += f"Table: {table_name}\n"
        prompt += "Columns:\n"
        for column_name, column_type in table_info['columns'].items():
            prompt += f"  - {column_name}: {column_type}\n"
        prompt += "\n"
        prompt += "Relationships:\n"
        for column_name, relationship in table_info['relationships'].items():
            prompt += f"  - {column_name} → {relationship}\n"
        prompt += "\n"
    prompt += f"""
    Question: {question}
    SQL Query:"""
    logger.info("SQL prompt built successfully.")
    return prompt

def generate_sql_query(llm, question):
    logger.info("Generating SQL query for the question.")
    prompt = build_sql_prompt(question)
    logger.info("Invoking LLM")
    response = llm.invoke(prompt)
    logger.info("SQL query generated successfully.")
    return response.content
