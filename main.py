"""Main entry point module responsible for orchestrating the scraping and export pipeline.
"""

from playwright.sync_api import Playwright, sync_playwright
from config.logger import setup_logger
from src.browser import open_page, navigate_with_retry
from src.scraper import extract_all_quotes
from src.storage import save_to_csv
from config.settings import BASE_URL
from src.cleaner import cleaner

setup_logger()

def run(playwright: Playwright) -> None:
    """Executes the end-to-end ETL pipeline in a sequential and controlled manner.

    Orchestrates browser initialization, resilient navigation, raw data extraction, 
    data sanitization, and CSV persistence. Ensures proper resource cleanup by 
    closing browser contexts inside the 'finally' block.

    Args:
        playwright (Playwright): Main Playwright lifecycle manager.
    """
    browser = None
    context = None

    try:
        browser, context, page = open_page(playwright)

        navigate_with_retry(page, BASE_URL)

        quotes = extract_all_quotes(page)

        clean_quotes = cleaner(quotes)

        save_to_csv(clean_quotes)

    finally:
        if context:
            context.close()
        if browser:
            browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)