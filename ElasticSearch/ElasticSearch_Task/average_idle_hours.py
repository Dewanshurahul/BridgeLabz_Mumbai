from elasticsearch import Elasticsearch

try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
    try:
        res = es.search(index="elasticsearch",body={"from":0, "size": 0,"query": {"match_all": {}}, "aggs": {"avg_hours":{"avg":{"field": "idle_hours"}}}})
        print(res)
        print(es.search(index="elasticsearch", body={"_source": ["user_name"], "query": {"range": {"idle_time": {"gt":"2019-10-24T02:01:52.500Z"}}}}))
    except:
        print("Data not Found")
except:
    print("Connection not Established")