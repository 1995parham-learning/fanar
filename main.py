from elasticsearch import Elasticsearch

if __name__ == '__main__':
    conn = Elasticsearch('tcp://127.0.0.1:9200')
    print(conn.info())

    index = "index"
    res = conn.search(index=index, query={
        "query": {
            "bool": {
                "must": [
                    {"term": {"key": "value"}},
                    {
                        "range": {
                            "key": {
                                "gte": "leat value",
                                "lte": "most value"
                            }
                        }
                    }
                ]
            }
        }
    })

    print(res)
    print(res['hits']['hits'][0]['_source'])
