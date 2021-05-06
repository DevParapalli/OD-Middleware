from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Construct paths like this 
PLUGINS_DIR = BASE_DIR / 'plugins'

__VERSION__ = "0.0.1" # https://semver.org/


# Example Settings
EXAMPLE = {
    'setting':"value"
}

ODCRAWLER = {
    'search-endpoint':"https://search.odcrawler.xyz/elastic/links/_search",
    
}