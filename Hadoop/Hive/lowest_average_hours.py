from pyhive import hive
import pandas as pd
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="log_data", auth="NOSASL")
#load database into hive
query = pd.read_sql('select * from user_log_data', conn)
#convert the data into the format of datetime
query['user_log_data.working_hours'] = pd.to_datetime(query['user_log_data.working_hours'])
#calculate the mean of total working_hours
avghour = query[query['user_log_data.working_hours'] < query['user_log_data.working_hours'].mean()]
print(avghour)
#print the user_name with lowest average hours
lowest_average_hours = avghour['user_log_data.user_name']
print(lowest_average_hours)