import os
from dotenv import load_dotenv

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Load environment variables
load_dotenv(os.path.join(BASEDIR, 'config.env'))
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
# CHROMEDRIVER_PATH = 'C:\Users\Rendy Theoanantyo\Documents\webdrivers\chromedriver'

# URLs
BOOKSTOSCRAPE_URL = 'https://books.toscrape.com/'
GOLDBUGS_URL = 'https://www.thegoldbugs.com/'
IMGUR_UPLOAD_URL = 'https://imgur.com/upload'
JQUERYUI_URL = 'https://jqueryui.com/'
PYTHON_URL = 'https://www.python.org/'
PYTHON_DOWNLOAD_URL = 'https://www.python.org/downloads/'
QUOTESTOSCRAPE_URL = 'https://quotes.toscrape.com/'
SELENIUM_DOCS_SEARCH_URL = 'https://selenium-python.readthedocs.io/search.html'
SELENIUM_URL = 'https://www.selenium.dev'
WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Main_Page'
WIKIPEDIA_SEARCH_URL = 'https://en.wikipedia.org/w/index.php?search='


# Constants
WAIT_TIME = 20  # seconds
