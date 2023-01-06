import psycopg2

def postgres_connection(db_host, db_name, db_user, db_pass):

    connection = psycopg2.connect(f"dbname={db_name} user={db_user} host={db_host} password={db_pass}")

    return connection 

