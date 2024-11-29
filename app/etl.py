import os
import psycopg2

# Fetch database connection details from environment variables
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')

def connect_db():
    """Establish connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_data(conn):
    """Insert sample data into the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO users (name, age) VALUES
        ('Alice', 30),
        ('Bob', 25),
        ('Charlie', 35);
        """)
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")

def fetch_data(conn):
    """Fetch and print data from the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        print("Fetched data:")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        insert_data(conn)
        fetch_data(conn)
        conn.close()
