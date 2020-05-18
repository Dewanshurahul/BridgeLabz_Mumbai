
from pyhive import hive
import pandas as pd
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="log_data", auth="NOSASL")
#load database into hive
query = pd.read_sql('select * from user_log_data', conn)
#convert the data into the format of datetime
query['user_log_data.idle_time'] = pd.to_datetime(query['user_log_data.idle_time'])
#calculate total idle_hours mean
idledata =query[query['user_log_data.idle_time'] > query['user_log_data.idle_time'].mean()]
print(idledata)
#print user_name with HIGHEST_IDLE_HOURS
HIGHEST_IDLE_HOURS=idledata['user_log_data.user_name']
print(HIGHEST_IDLE_HOURS)