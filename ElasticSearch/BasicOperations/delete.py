from elasticsearch import Elasticsearch
try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
except:
    print("Connection not Established")
try:
    res = es.delete(index="studentinfo",doc_type="user_log_data",id="rahulraman")
    print(res)
    print("Document Sucessfully Deleted")
except:
    print("Element does not exist")