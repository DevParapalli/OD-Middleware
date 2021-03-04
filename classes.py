import importlib

class Query:
    def __init__(self, query_string, max_items=10, file_type="*", service="example", service_data={}):
        self.query_str = query_string
        self.max_items = max_items
        self.file_type = file_type
        self.service = service
        self.service_data = service_data
    
    def execute(self):
        ## Query Logic
        service = importlib.import_module(f"queries.{self.service}")
        ## then pass self to the service.process()
        ## the process should return a list iteratable or be a generator so
        # as to use its value directly in a list shorthand
        self.__raw_results = [result for result in service.process(self)]

    def get_results(self):
        return [ResultItem(**item) for item in self.__raw_results]
    

class ResultItem:
    def __init__(self, file_name, file_type, file_size, abs_path=""):
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size
        self.abs_path = abs_path
        
    

## Execute query by using Query.execute()
## Query.get_results() returns [ResultItem(), ...]
