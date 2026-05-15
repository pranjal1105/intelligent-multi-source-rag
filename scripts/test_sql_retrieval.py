#test sql retrieval
from app.retrieval.sql_retrieval import execute_sql_query
query="""WITH CTE AS (
    SELECT EMPLOYEE_ID, SUM(DAYS_TAKEN) AS TOTAL_LEAVES
    FROM LEAVE_RECORDS
    GROUP BY EMPLOYEE_ID
)
SELECT C.EMPLOYEE_ID, E.EMPLOYEE_NAME, C.TOTAL_LEAVES
FROM CTE AS C
JOIN EMPLOYEES AS E ON C.EMPLOYEE_ID = E.EMPLOYEE_ID
WHERE C.TOTAL_LEAVES IN (
    SELECT MAX(TOTAL_LEAVES)
    FROM CTE)"""
result=execute_sql_query(query)
print("Top employees with the most leaves:")

for row in result:
    print(row)
    