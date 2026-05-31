from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pelicanconf import *  # noqa: F403

SITEURL = "https://atli2001.github.io"
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
