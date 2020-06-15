from elasticsearch import Elasticsearch

try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
    try:
        print(es.search(index="elasticsearch", body={"_source": ["username", "starttime"], "query": {"range": {"starttime": {"gt":"2019-10-24T08:30:00.000Z"}}}}))
    except:
        print("Data not Found")
except:
    print("Connection not Established")