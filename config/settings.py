import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL","https://quotes.toscrape.com/")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10000))
MAX_ATTEMPTS = int(os.getenv("MAX_ATTEMPTS", 3))
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data")

HEADLESS = bool(os.getenv("HEADLESS", "true").lower() == "true")
