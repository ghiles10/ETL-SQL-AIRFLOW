from utils import connection_object
from create_table import create_tables 
from table import user_info, tweet_info, activity_info
from write_table import write
import sys
sys.path.append('./')


# create tables
create_tables()

# write data to tables
for table in [tweet_info, user_info, activity_info]  :
    write(table()[0], table()[1],table()[2] )


