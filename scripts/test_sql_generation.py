from app.generation.sql_generator import generate_sql_query
from app.llm.llm_initializer import initialize_llm
from app.retrieval.sql_retrieval import execute_sql_query


llm=initialize_llm()

question_1="Who has the highest salary?"
question_2="Which employee took the most leaves?"
question_3="Average salary by department?"
question_4="Employees with performance rating above 4.5"
question_5="Department with highest average salary?"

sql_1=generate_sql_query(llm,question_1)
sql_2=generate_sql_query(llm,question_2)
sql_3=generate_sql_query(llm,question_3)
sql_4=generate_sql_query(llm,question_4)
sql_5=generate_sql_query(llm,question_5)

# print(f"Question: {question_1}")
# print(f"SQL Query: {sql_1}")
# print(f"Question: {question_2}")
# print(f"SQL Query: {sql_2}")    
# print(f"Question: {question_3}")
# print(f"SQL Query: {sql_3}")
# print(f"Question: {question_4}")
# print(f"SQL Query: {sql_4}")
# print(f"Question: {question_5}")
# print(f"SQL Query: {sql_5}")

result=execute_sql_query(sql_1)
print(f"Result for Question 1: {result[0]}")

