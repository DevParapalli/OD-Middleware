""" Main Entrypoint into OD-Middleware """
import importlib

from classes import Query

def main():
    q = Query('alpha', max_items=15)
    q.execute()
    print([file.abs_path for file in q.get_results()])

if __name__ == "__main__":
    main()
