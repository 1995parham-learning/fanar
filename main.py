from dataclasses import dataclass, asdict
from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch.helpers import scan

INDEX = "students"


@dataclass
class Student:
    name: str
    family: str


if __name__ == "__main__":
    conn = Elasticsearch("tcp://127.0.0.1:9200", basic_auth=("elastic", "password"))
    print(conn.info())

    try:
        conn.get(index=INDEX, id="9231058")
    except NotFoundError:
        conn.create(
            index=INDEX,
            id="9231058",
            document=asdict(
                Student(
                    name="Parham",
                    family="Alvani",
                )
            ),
        )

    for res in scan(
        conn,
        index=INDEX,
        query={
            "query": {
                "match": {
                    "name": "Parham",
                }
            }
        },
    ):
        print(res)
        print(Student(**res["_source"]))
