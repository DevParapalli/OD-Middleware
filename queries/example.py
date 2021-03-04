##########IGNORE################
search = [i for i in range(32)]

################################


from classes import Query


def process(Query: Query):
    # if the search requires additional parameters such as file path (Local Indexing/ Custom Endpoint) or additional 
    # restrictions/parameters, extract them from Query.service_data
    # Do the query logic and set parameters into it.
    return [ unified_format(item) for item in search[:Query.max_items] ]
    ## format the search into a dict containing: 
    # name, type, size, path or defaults thereof.

def unified_format(item):
    ## Custom logic for each seperate search tool or indexer.
    # Process the file if needed to get more data
    return {
        "file_name":"example.dev",
        "file_type":"", # MIME Type ?? Extension ?? Custom ??
        "file_size":"1.02M", # Not Necessarry to include this, just have NULL here
        "abs_path":f"{item}" # Absolute Path to the resource. Sort of like click this to download resource or input into downloader directly
    }