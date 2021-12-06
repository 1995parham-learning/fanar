from elasticsearch import Elasticsearch


class Elastic:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        return Elasticsearch(hosts=self.host + ":" + self.port)
