from __future__ import annotations
import importlib

class Query:
    def __init__(self, query_string:str, max_items:int=10, file_type:str="*", service:str="example", service_data=None):
        self.query_str = query_string
        self.max_items = max_items
        self.file_type = file_type
        self.service = service
        self.state = 'init'
        self.service_data = service_data or {}
    
    def _resolve(self, results:list):
        self._results = [ResultItem(**x) for x in results]
    
    def get_results(self):
        return self._results
    
    def __repr__(self):
        return f"Query('{self.query_str}', {self.max_items}, '{self.file_type}', '{self.service}', {self.service_data})"

class ResultItem:
    def __init__(self, file_name: str = "Example Webpage", file_title: str = "Example Webpage", file_type: str = "type/html", file_size: int = -1, abs_path: str = "https://example.com"):
        self.file_name = file_name
        self.file_title = file_title
        self.file_type = file_type
        self.file_size = file_size
        self.abs_path = abs_path
    def __repr__(self):
        return f"ResultItem('{self.file_name}', '{self.file_type}', '{self.file_size}', '{self.abs_path}')"
    def __str__(self):
        return f"""[RESULT] \"{self.file_name}\" \"{self.file_type}\" \"{self.file_size}\" \"{self.abs_path}\" """
    
class BaseQueryResolver:
    def __init__(self):
        # Use this function to initialize the QueryResolver
        # This function can be used to setup a resolver with API_KEYS and stuff like that.
        # Use the settings.py to setup the resolver
        pass

    def process(self, query: Query):
        # Use this function to process a query.
        # Process the logic and use the query._resolve method to add data to the query.
        # There is a Query.service_data where custom things are kept
        query._resolve([self._format(x) for x in range(1, 10)]) # Place holder
        query.state = 'resolved'


    def _format(self, item):
        # Custom logic for each separate search tool or indexer.
        # Process the file if needed to get more data
        return {
            "file_name": "example.dev",
            "file_type": "type/text",  # MIME Type
            "file_size": 31242,  # Leave it at -1 if not known, else size in Bytes
            "abs_path": f"{item}"  # Absolute Path to the resource. Sort of like click this to download resource or input into downloader directly
        }
