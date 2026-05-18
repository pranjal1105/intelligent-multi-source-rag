DATABASE_NAME="enterprise_ai_rag"

TABLES={
    "employees": {
        "columns": {
            "employee_id": "INTEGER PRIMARY KEY",
            "employee_name": "VARCHAR(100)",
            "department_id": "INTEGER FOREIGN KEY → departments.department_id",
            "joining_date": "DATE",
            "salary": "NUMERIC(10,2)",
            "performance_rating": "NUMERIC(3,1)"
        },
        "relationships": {
            "department_id": "departments.department_id"
        }
    },
    "departments": {
        "columns": {
            "department_id": "INTEGER PRIMARY KEY",
            "department_name": "VARCHAR(100)"
        },
        "relationships": {}
    },
    "leave_records": {
        "columns": {
            "leave_id": "INTEGER PRIMARY KEY",
            "employee_id": "INTEGER FOREIGN KEY → employees.employee_id",
            "leave_type": "VARCHAR(50)",
            "days_taken": "INTEGER",
            "start_date": "DATE",
            "end_date": "DATE"
        },
        "relationships": {
            "employee_id": "employees.employee_id"
        }
    }
}