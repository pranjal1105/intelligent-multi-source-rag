import re

AGGREGATION_KEYWORDS=[
    "highest",
    "lowest",
    "average",
    "count",
    "most",
    "least",
    "maximum",
    "minimum",
    "top",
    "sum"
]

DATABASE_KEYWORDS=[
    "salary",
    "employee",
    "department",
    "leave",
    "performance"
]

def route_query(question):

    q=question.lower()

    has_aggregation=any(
        keyword in q
        for keyword in AGGREGATION_KEYWORDS
    )

    has_database=any(
        keyword in q
        for keyword in DATABASE_KEYWORDS
    )

    if has_aggregation and has_database:
        return "sql"

    return "vector"