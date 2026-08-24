"""Module responsible for managing browser initialization and resilient navigation.
"""

from playwright.sync_api import Playwright, TimeoutError, Browser, BrowserContext, Page
import logging
from config.settings import HEADLESS, DEFAULT_TIMEOUT, MAX_ATTEMPTS


def open_page(playwright: Playwright) -> tuple[Browser, BrowserContext, Page]:
    """Initializes the Chromium browser, creates an isolated context, and opens a new page.

    Args:
        playwright (Playwright): Main Playwright lifecycle manager.

    Returns:
        tuple[Browser, BrowserContext, Page]: A tuple containing the initialized 
            browser, context, and configured page instances.
    """
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()

    page.set_default_timeout(DEFAULT_TIMEOUT)

    return browser, context, page

def navigate_with_retry(page: Page, url: str, max_attempts: int = MAX_ATTEMPTS) -> None:
    """Navigates to the specified URL using a retry mechanism for network resilience.

    Args:
        page (Page): Active Playwright page instance.
        url (str): Target web address to access.
        max_attempts (int, optional): Maximum number of retry attempts upon timeout. 
            Defaults to MAX_ATTEMPTS.

    Raises:
        Exception: Raised when the maximum number of attempts is reached without success.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            logging.info(F"Attempt {attempt} of {max_attempts}: Connecting to {url}...")
            page.goto(url)
            logging.info("Connected successfully!")
            break
        except TimeoutError:
            logging.warning(f"Connection attempt {attempt} failed.")
            if attempt == max_attempts:
                logging.error(f"Maximum of {max_attempts} attempts reached. Connection failed...")

                raise Exception(f"Failes to connect after {max_attempts} attempts.") from None