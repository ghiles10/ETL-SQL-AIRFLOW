from utils import connection_object
from extract import extract_tweet 
from config import USER_NAME
from table import user_info, tweet_info, activity_info

def query(table_name, column_names):
    
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    column_values_string = ', '.join(column_values)
    query = (f'''
        INSERT INTO {table_name} ({column_names_string}) VALUES ({column_values_string})
    ''')

    return query

def insert(conn, query, cursor, table_data, batch=20):

    records = [] 
    count = 1 

    for raw in table_data:

        records.append(raw)

        if count % batch == 0:
            cursor.executemany(query, records)
            conn.commit()
            records = []

        count = count + 1


    cursor.executemany(query, records)
    conn.commit()


def write(table_name, column_names, table_data) : 

    conn = connection_object()
    cursor = conn.cursor()

    query_insert = query(table_name, column_names)

    insert(conn,query_insert,  cursor, table_data)

    conn.close()
    cursor.close()

if __name__ == '__main__' : 
    
    write(user_info())
    write(tweet_info())
    write(activity_info())