from pyhive import hive
import pandas as pd
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="log_data", auth="NOSASL")
#load database from hive
query = pd.read_sql('select * from user_log_data', conn)
#convert the data into the format of datetime
query['user_log_data.working_hours'] = pd.to_datetime(query['user_log_data.working_hours'])
#calculate the mean of total working_hours
averagehours = query[query['user_log_data.working_hours'] > query['user_log_data.working_hours'].mean()]
print(averagehours)
#print the user_name with highest average hours
highest_avg_hours =averagehours['user_log_data.user_name']
print(highest_avg_hours)