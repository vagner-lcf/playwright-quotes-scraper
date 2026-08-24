"""Module responsible for scraping raw quote data and handling pagination.
"""

from playwright.sync_api import TimeoutError, Page
import logging


def extract_all_quotes(page: Page) -> list[dict[str, str]]:
    """Extracts all quotes across available pages by navigating sequentially.

    Scrapes raw author and quote text from each page and automatically advances 
    when a next page control is detected. Includes an internal reload fallback 
    mechanism if element rendering times out.

    Args:
        page (Page): Active Playwright page instance.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing raw scraped data 
            with 'author' and 'quote' keys.
    """
    quotes: list[dict[str, str]] = []    
    page_number = 1

    while True:
        logging.info(f"Scrapping page {page_number}")

        try:
            page.locator(".quote").first.wait_for(timeout=5000)
        except TimeoutError:
            logging.warning(f"Failed to load page number {page_number}. Reloading...")

            try:
                page.reload()
                page.locator(".quote").first.wait_for(timeout=5000)
            except TimeoutError:
                logging.error(f"Unable to load the page {page_number}. Saving scrapped data...") 
                break

        all_quotes = page.locator(".quote").all()           

        for quote in all_quotes:
            raw_quote = quote.locator(".text").inner_text()
            raw_author = quote.locator(".author").inner_text()

            quotes.append({"author": raw_author, "quote": raw_quote})

        next_button = page.get_by_role("link", name="Next")
        if not next_button.is_visible():
            break
        
        next_button.click()
        page_number += 1

    logging.info(f"Total of raw registers: {len(quotes)}")

    if not quotes:
        logging.error("No data recorded. CSV export was cancelled")

        return quotes

    return quotes     