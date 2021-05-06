from classes import Query, BaseQueryResolver

META = {
    '__version__':"0.0.1",
    'author':"Dev",
    'author_email':"devparapalli@gmail.com",
    'description':"This is an example for a QueryResolver"
}

class ExampleResolver(BaseQueryResolver):
    def __init__(self):
        super().__init__() # Does nothing atm
        from settings import EXAMPLE
        _ = EXAMPLE['setting']
        

# Instantiate the class and export in in the EXPORTS dict
EXPORTS = {
    'resolver':ExampleResolver(),
    'metadata': META,
    'enabled': False
}
