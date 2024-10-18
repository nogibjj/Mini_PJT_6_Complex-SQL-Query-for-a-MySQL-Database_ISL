from databricks import sql
from dotenv import load_dotenv
import os

# Query module for the HR database
complex_query = """
SELECT 
    p.EmployeeNumber, 
    p.Age, 
    p.Gender, 
    a.Attrition, 
    a.Department
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
ORDER BY 
    p.EmployeeNumber ASC;
"""

# Load environment variables for Databricks connection
load_dotenv()
server_hostname = os.getenv("sql_server_host")
access_token = os.getenv("databricks_api_key")
http_path = os.getenv("sql_http")

def query():
    """Execute a SQL query on Databricks SQL Warehouse and print results."""
    # Connect to the Databricks SQL Warehouse
    with sql.connect(
        server_hostname=server_hostname, 
        http_path=http_path, 
        access_token=access_token
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(complex_query)
            query_result = cursor.fetchall()

            # Print each row from the result
            for row in query_result:
                print(row)

            # Print success message
            print("Query completed successfully.")
            return "success"  # Return success if query executes correctly

# Execute the complex query when the script runs
if __name__ == "__main__":
    result = query()
