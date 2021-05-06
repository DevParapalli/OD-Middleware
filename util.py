from __future__ import annotations

import importlib
import pkgutil

from classes import Query, BaseQueryResolver
from settings import BASE_DIR



def import_plugin(plugin_name):
    return importlib.import_module(f'plugins.{plugin_name}')

def _get_plugins():
    resolvers = {}
    downloaders = {}
    
    plugins = [name for _, name, _ in pkgutil.iter_modules([f"{BASE_DIR / 'plugins'}"])]
    for plugin_name in plugins:
        if plugin_name.startswith('resolver_'):
            plugin = import_plugin(plugin_name)
            resolvers[plugin_name] = plugin.EXPORTS
        elif plugin_name.startswith('downloader_'):
            plugin = import_plugin(plugin_name)
            downloaders[plugin_name] = plugin.EXPORTS
        elif plugin_name.startswith(('base_', 'handler_')):
            continue
        else:
            print(f"[WARN] Plugin {plugin_name} is of unknown type.")
    return {key: resolvers[key] for key in resolvers if resolvers[key]['enabled']}, downloaders

# Exports this shit too
RESOLVERS, DOWNLOADERS = _get_plugins()

def create_query(query_string, max_items=10, file_type="*", service="example", service_data=None):
    return Query(query_string, max_items, file_type, service, service_data)


def resolve_query(query: Query):
    plugin_name = f"resolver_{query.service}"
    RESOLVERS[plugin_name]['resolver'].process(query)

def pretty_print_results(resolved_query:Query):
    if resolved_query.state != 'resolved':
        print("[WARN] Query is not completely resolved. The results may be incorrect.")
    print("###")
    for item in resolved_query.get_results():
        print(f"{item.file_name}\n{item.abs_path}\n###")