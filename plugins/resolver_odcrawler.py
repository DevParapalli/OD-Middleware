from classes import Query, BaseQueryResolver
from requests import post
from mimetypes import guess_type, guess_extension

META = {
    '__version__': "0.0.1",
    'author': "Dev",
    'author_email': "devparapalli@gmail.com",
    'description': "Plugin for https://odcrawler.xyz"
}


class ODCrawlerResolver(BaseQueryResolver):
    def __init__(self):
        # super().__init__() # Does nothing atm
        from settings import ODCRAWLER
        self.endpoint = ODCRAWLER['search-endpoint']

    def process(self, query: Query):
        post_data = {
            "size": query.max_items,
            "from": 0,
            "highlight": {"fields": {"url": {}, "filename": {}}},
            "query": {
                "bool": {
                    "must": [{"match_phrase": {"url": query.query_str}}],
                    "should": [{"match_phrase": {"filename": query.query_str}}],
                    #"must_not": [{"terms": {"extension": []}}]
                }
            }
        }
        response = post(self.endpoint, json=post_data)
        query._resolve([self._format(x) for x in response.json()['hits']['hits']])
        query.state = 'resolved'
        
    def _format(self, item):
        return {
            "file_name": f"{item['_source']['filename']}",
            "file_title": f"{item['_source']['filename']}",
            "file_type": f"{guess_type(item['_source']['filename'])}",  # MIME Type
            "file_size": -1,  # Leave it at -1 if not known, else size in Bytes
            "abs_path": f"{item['_source']['url']}"  # Absolute Path to the resource. Sort of like click this to download resource or input into downloader directly
        }

# Instantiate the class and export in in the EXPORTS dict
EXPORTS = {
    'resolver': ODCrawlerResolver(),
    'metadata': META,
    'enabled': True
}
