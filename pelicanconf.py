from pathlib import Path
import sys
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parent))

from publication_data import PUBLICATIONS

PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "monthly",
        "pages": "monthly",
    },
}

AUTHOR = "Austin T. Li"
SITENAME = "blank"
SITEURL = ""
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

DISPLAY_NAME = "Austin T. Li"
FOOTER_TEXT = "Powered by Pelican. Hosted by GitHub Pages."
CURRENT_YEAR = date.today().year

STATIC_PATHS = ["extra", "images", "pdfs"]
EXTRA_PATH_METADATA = {"extra/robots.txt": {"path": "robots.txt"}}

THEME = "themes/al-folio-simple"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

MENUITEMS = [
    ("About", "/"),
    ("Publications", "/publications/"),
    ("Teaching", "/teaching/"),
    ("Awards", "/awards/"),
]

NAVBAR_FIXED = True
FOOTER_FIXED = True
ENABLE_DARKMODE = False

RELATIVE_URLS = True

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True
