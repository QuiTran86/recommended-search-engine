import json

from elasticsearch import Elasticsearch, helpers

from backend.config import ES_HOST, ES_PORT, ES_USERNAME, ES_PASSWORD


class ESRepo:
    DESCRIPTION_PREFIX_QUERY = """
    {
    "query": {
        "bool": {
            "must": [
                {
                    "match_phrase_prefix": {
                        "description": {
                            "query": "%s"
                        }
                    }
                }
            ]
        }
    },
    "aggs": {
        "susgested_results": {
            "terms": {
                "size": 10,
                "field": "description.keyword",
                "order": {
                    "_count": "asc"
                }
            }
        }
    }
   }
   """
    NEFLIX_INDEX = 'netflix'

    def __init__(self):
        self.es_client = Elasticsearch(
            hosts=[{'host': ES_HOST, 'port': ES_PORT, 'scheme': 'https'}],
            verify_certs=False, basic_auth=(ES_USERNAME, ES_PASSWORD),
            ssl_show_warn=False)

    def prepare_query(self, prefix_text):
        return json.loads(self.DESCRIPTION_PREFIX_QUERY % prefix_text) if prefix_text else {}

    def get_document_by_prefix_description_key(self, prefix_text):
        query = self.prepare_query(prefix_text)
        return self.es_client.search(index=self.NEFLIX_INDEX, body=query)

    def index_document(self, index, document):
        return self.es_client.index(index=index, document=document)

    def bulk_index(self, index, documents):
        return helpers.bulk(self.es_client, documents, index=index)
