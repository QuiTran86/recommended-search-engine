from decouple import config

ES_HOST = config('ES_HOST', default='localhost')
ES_PORT = config('ES_PORT', default=9200, cast=int)
ES_USERNAME = config('ES_USERNAME', default=None)
ES_PASSWORD = config('ES_PASSWORD', default=None)
