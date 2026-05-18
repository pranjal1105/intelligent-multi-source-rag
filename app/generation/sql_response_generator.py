def build_sql_result_generation_prompt(question, sql_query, sql_result):
    prompt = f"""
    You are an assistant that helps to answer questions based on SQL query results. 
    The user has asked the following question: "{question}"
    
    The SQL query generated to answer this question is: "{sql_query}"
    
    The result of executing the SQL query is: "{sql_result}"
    
    Please provide a clear and concise answer to the user's question based on the SQL query result.
    """
    return prompt
def generate_sql_response(question,sql_query, sql_result ,llm, retriever):
    prompt=build_sql_result_generation_prompt(question,sql_query, sql_result)
    response=llm.invoke(prompt)
    return response.content.strip()

    