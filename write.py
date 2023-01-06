def insert_query(table_name, column_names):
    
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    column_values_string = ', '.join(column_values)
    query = (f'''
        INSERT INTO {table_name} ({column_names_string}) VALUES ({column_values_string})
    ''')

    return query

def insert_data(conn, query, data, batch_size=20):

    recs = [] 
    count = 1 

    for rec in data:

        recs.append(rec)

        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            recs = []

        count = count + 1

    cursor.executemany(query, recs)
    connection.commit()
