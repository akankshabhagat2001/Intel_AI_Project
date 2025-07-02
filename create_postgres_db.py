import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# PostgreSQL connection details
# Update these as needed

db_name = "flavi_dairy"
db_user = "postgres"
db_password = "admin@1"
db_host = "localhost"
db_port = "5432"

try:
    # Connect to the default 'postgres' database
    con = psycopg2.connect(
        dbname='postgres',
        user=db_user,
        host=db_host,
        password=db_password,
        port=db_port
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    # Create the new database
    cur.execute(f"CREATE DATABASE {db_name};")
    print(f"✅ Database '{db_name}' created successfully!")

    cur.close()
    con.close()
except psycopg2.errors.DuplicateDatabase:
    print(f"⚠️ Database '{db_name}' already exists.")
except Exception as e:
    print(f"❌ Error: {e}") 