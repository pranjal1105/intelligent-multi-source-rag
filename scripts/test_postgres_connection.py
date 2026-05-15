import logging
from app.database.postgres_connection import connect_to_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


conn=connect_to_db()

cursor=conn.cursor()
query= "SELECT version();"
cursor.execute(query)
result=cursor.fetchone()

cursor.close()
conn.close()
print("PostgreSQL version:", result[0])

