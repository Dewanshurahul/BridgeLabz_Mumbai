from elasticsearch import Elasticsearch

try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
    try:
        res = es.search(index="elasticsearch",body={"from":0, "size": 0,"query": {"match_all": {}}, "aggs": {"avg_hours":{"avg":{"field": "working_hours"}}}})
        print(res)
        print(es.search(index="elasticsearch",body={"_source": ["username"], "query": {"range": {"workhours": {"gt": "2019-10-24T01:38:14.818Z"}}}}))
    except:
        print("Data not Found")
except:
    print("Connection not Established")