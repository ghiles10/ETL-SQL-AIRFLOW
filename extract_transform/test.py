from utils import connection_object
conn = connection_object() 
cur = conn.cursor()

cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    """)

# Store the list of tables
tables = cur.fetchall()
# Iterate through the list of tables and drop each one
for table in tables:
    cur.execute(f"DROP TABLE {table[0]}")
    print(table)
    
conn.commit()
conn.close()

# cur.execute("""
#     SELECT *
#     FROM TWEET_INFO
#     """)

# # Store the list of tables
# tables = cur.fetchall()
# # Iterate through the list of tables and drop each one
# for table in tables:
#     # cur.execute(f"DROP TABLE {table[0]}")
#     print(table)
    
# conn.commit()
# conn.close()
