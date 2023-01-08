# SQL-AIRFLOW

This is a simple ETL using Airflow. first, I fetch data from the twitter api. then create a databse on postgres that stores these data by creating 3 tables. I validate the data (transform). Finally, I convert the tables into csv files with the specific dates at the time of the conversion. 

## Prerequisites

1. Setup PostgreSQL
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Create a new user 
sudo -u postgres createuser --login --pwprompt user_name
sudo -u postgres createdb --owner=user_name database_name
```
2. Create a .env file : 

```
# connecting to api
access_key=''
access_secret='' 
consumer_key=''
consumer_secret=''
# postgres 
db_name=database
db_user=user
db_pass=password
```

3. Set Airflow Home Directory (local run) : 
 ```
 export AIRFLOW_HOME=$pwd
 ```
 
4. Set VirtualEnv : 
 ``` 
python3 -m venv etl
source etl/bin/activate
``` 

5. Install Dependency : 
```
pip install -r requirements.txt
```
