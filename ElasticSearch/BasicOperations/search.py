from elasticsearch import Elasticsearch
try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
except:
    print("Connection not Established")
