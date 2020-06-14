from elasticsearch import Elasticsearch
try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
except:
    print("Connection not Established")
element = {
    "first_name": "Rahul",
    "last_name": "Raman",
    "roll": 12110617,
    "branch": "Royal Mech"
}
try:
    res = es.index(index="studentinfo",doc_type="user_log_data",id="rahulraman",body=element)
    print("Document Inserted Sucessfully")
except:
    print("Document did not get Inserted")