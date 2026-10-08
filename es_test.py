from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
print(es.info()["version"]["number"])

docs = [
    {"title": "Intro to Python", "text": "Python is a popular language for AI and data science."},
    {"title": "What is Docker", "text": "Docker runs apps inside containers."},
    {"title": "Vector databases", "text": "Vector databases store embeddings for semantic search."},
]

for i, doc in enumerate(docs, start=1):
    es.index(index="my-docs", id=i, document=doc)

es.indices.refresh(index="my-docs")

res = es.search(index="my-docs", query={"match": {"text": "containers"}})

for hit in res["hits"]["hits"]:
    print(hit["_score"], hit["_source"]["title"])