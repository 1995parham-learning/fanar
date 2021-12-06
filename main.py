import time

from connections.elastic import Elastic

if __name__ == '__main__':
    client = Elastic('host', 'port')
    conn = client.connect()
    # print(conn.info())

    index = "index"
    res = conn.search(index=index, body={
        "query": {
            "bool": {
                "must": [
                    {"term": {"key":	"value"}},
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
