from pyhive import hive
import pandas as pd
conn = hive.Connection(host="localhost", port=10000, database="log_data", auth="NOSASL")
query= pd.read_sql('select * from user_log_data', conn)
# Getting dataframe whose start time is above 9:30 AM
late_commers = query[query['user_log_data.start_time'] > '2019-10-24 09:30:00']
# Getting user names only
late_commers_usernames = late_commers['user_log_data.user_name']
print(late_commers_usernames)