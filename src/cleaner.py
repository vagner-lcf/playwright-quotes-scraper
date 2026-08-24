"""Module responsible for sanitizing, validating, and deduplicating quote data.
"""

import logging


def cleaner(data: list[dict[str, str]]) -> list[dict[str, str]]:
    """Sanitizes, filters, and deduplicates a list of quote records.

    Cleans each record by stripping typographical quotes and excess whitespace 
    (including NBSP characters). Discards incomplete entries and ensures quote 
    uniqueness using O(1) constant-time tracking.

    Args:
        data (list[dict[str, str]]): List of dictionaries containing raw scraped 
            data with 'author' and 'quote' keys.

    Returns:
        list[dict[str, str]]: A new list of dictionaries containing only sanitized, 
            validated, and unique records.
    """
    cleaned_data: list[dict[str, str]] = []
    seen_quotes: set[str] = set()

    for item in data:
        text = item.get("quote", "").replace('\xa0', ' ').strip('“"”').strip()
        author = item.get("author", "").strip()

        if not text or not author:
            logging.warning("Skipping incomplete record found during cleaning.")
            continue

        if text in seen_quotes:
            logging.info(f"Skipping duplicate quote: '{text[:20]}...'")
            continue

        seen_quotes.add(text)
        cleaned_data.append({
            "author": author,
            "quote": text
        })

    logging.info(f"Total of cleaned registers: {len(cleaned_data)}")

    return cleaned_data


        