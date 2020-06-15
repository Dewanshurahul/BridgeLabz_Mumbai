from elasticsearch import Elasticsearch
try:
    es = Elasticsearch([{"host":"localhost","port":9200}])
    print(es)
    res = es.search(index="studentinfo", body={'query': {
        'bool': {
            'must': [{
                'match': {
                    'first_name': 'Dewanshu'
                }
            }]
        }
    }})
    print(res)
except:
    print("Connection not Established")
