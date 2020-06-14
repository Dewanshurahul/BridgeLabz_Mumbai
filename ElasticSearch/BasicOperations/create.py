from elasticsearch import Elasticsearch
try :
    es = Elasticsearch([{'host':'localhost','port':9200}])
    print(es)
except:
    print("Connection not Established")

e1 = {
    "first_name": "Dewanshu",
    "last_name": "Rahul",
    "roll" : 15110617,
    "branch": "CSE",
}
print(e1)