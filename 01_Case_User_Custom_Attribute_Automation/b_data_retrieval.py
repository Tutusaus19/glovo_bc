# data_retrieval.py
# Create a function to get user data: We receive cursor as an argument
def get_user_data(cursor):
    try:
        # open and read the sql file.
        with open('a_sql_query.sql', 'r') as file:
            query = file.read()
        # Print the query to debug
        print("Executing query:", query)
        # Execute the SQL query of the file previously read
        cursor.execute(query)
        # Fetch and return the result
        results = cursor.fetchall()
        print("Results:", results)
        return results
    except Exception as e:
        print("Error:", e)
        return None