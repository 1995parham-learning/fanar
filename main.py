from connections.elastic import Elastic

if __name__ == '__main__':
    conn = Elastic('host', 'port').connect()
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
