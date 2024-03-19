import psycopg 

# Define the connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': 5432
}

def connect():
    """ Connect to the PostgreSQL database server and return a connection object
    """
    try:
        conn = psycopg.connect(**db_params)
        print('Connected to the PostgreSQL server.')
        return conn
    except psycopg.OperationalError as e:
        print(f'Error: {e}')
        exit(1)

def selectAll(conn, table_name):
    """ Select all rows from the table
    """
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM " + table_name)
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except (psycopg.DatabaseError, Exception) as error:
        print(error)

def insert(conn, table_name, columns, values):
    """ Insert a new row into the table
    """
    try:
        with conn.cursor() as cur:  
            cur.execute("INSERT INTO " + table_name + " (" + columns + ") VALUES (" + values + ")") 
            conn.commit()           # Commit the changes to the database
    except (psycopg.DatabaseError, Exception) as error:
        print(error)

def update(conn, table_name, column, value, condition):
    """ Update a row in the table
    """
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE " + table_name + " SET " + column + " = " + value + " WHERE " + condition)
            conn.commit()
    except (psycopg.DatabaseError, Exception) as error:
        print(error)

def delete(conn, table_name, condition):
    """ Delete a row from the table
    """
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM " + table_name + " WHERE " + condition)
            conn.commit()
    except (psycopg.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    # Connect to the PostgreSQL database server
    conn = connect()

    selectAll(conn, "students")