from elasticsearch import Elasticsearch
try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
    try:
        res = es.search(index="studentinfo",body={"query":
                                                      {"bool":{
                                                          "filter": {
                                                              "range": {
                                                                  "roll": {
                                                                      "gt": 15110545
                                                                  }
                                                              }
                                                          }
                                                      }}})
        print(res)
    except:
        print("Data didn't fetched")
except:
    print("Connection not Established")