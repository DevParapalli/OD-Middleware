""" Main Entrypoint into OD-Middleware """
from util import (
    RESOLVERS, 
    DOWNLOADERS,
    create_query,
    resolve_query, 
    pretty_print_results
    #list_services 
)
from constants import INFO_1
from ast import literal_eval
def main():
    # The main.py file should be treated as a jank way to use the middleware
    # I am yet to add support for multiple resolvers and downloaders.
    # If you have the time to get a plugin working, create a pull request 
    print(INFO_1)
    print('AVAILABLE RESOLVERS', [key for key in RESOLVERS])
    q = create_query(
        query_string=input("Query>"),
        max_items=int(input("MaxItems(default=10)>") or 10),
        file_type=input("FileType>") or "*",
        service=input("Service>"),
        service_data= literal_eval(input("ServiceData>") or "{}")
    )

    resolve_query(q)
    pretty_print_results(q)

if __name__ == "__main__":
    #print(RESOLVERS)
    main()
