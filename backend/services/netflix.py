from backend.repositories.es import ESRepo


class NetflixService:

    def __init__(self):
        self.es_repo = ESRepo()

    def get_films_by_prefix_description_key(self, prefix_text):
        docs = self.es_repo.get_document_by_prefix_description_key(prefix_text)['hits']['hits']
        return [_['_source'] for _ in docs if _]
