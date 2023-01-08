# SQL-AIRFLOW

This is a simple ETL using Airflow. first, I fetch data from the twitter api. then create a databse on postgres that stores these data by creating 3 tables. I validate the data (transform). Finally, I convert the tables into csv files with the specific dates at the time of the conversion. 

## Prerequisites

1. Create a .env file : 

```
access_key=''
access_secret='' 
consumer_key=''
consumer_secret=''
db_name=database
db_user=user
db_pass=password
```
