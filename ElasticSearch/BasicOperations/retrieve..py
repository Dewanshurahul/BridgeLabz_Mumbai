from elasticsearch import Elasticsearch
try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
except:
    print("Connection not Established")

res = es.get(index="studentinfo",doc_type="user_log_data",id="rahulraman")
print(res)