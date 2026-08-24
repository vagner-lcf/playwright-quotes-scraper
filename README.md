# Playwright Quotes Scraper 

A lightweight Python ETL (Extract, Transform, Load) pipeline for automated and resilient web scraping and pagination on [Quotes to Scrape](https://quotes.toscrape.com/) via Playwright, processing data according to project business rules, and persisting results in CSV format.

🌐 *Read this in [Português](README.pt-br.md).* 

## Features

- **Browser Management & Access:** Resiliently handles Chromium browser initialization and navigation.
- **Resilience:** Implements timeout handling, navigation retries, and page reload fallback for failed content loading.
- **Data Transformation:** Cleans, sanitizes (removes quotes and NBSP spaces), discards incomplete entries, and deduplicates records using a set for average O(1) membership checks.
- **Persistence:** Exports processed data to a date-based CSV file, overwriting the existing file for the same execution date.
- **Unit Testing:** Unit tests with Pytest covering the data sanitization, validation, and deduplication rules.

## Technologies & Core Concepts

- **Python 3.11+**
- **Playwright:** Web automation and browser navigation management.
- **Pandas:** Data structuring and export.
- **Pytest:** Unit test coverage.
- **Centralized Configuration Management:** Execution parameters (base URL, timeouts, retry attempts, and headless mode) parameterized and isolated within the `config/settings.py` module.
- **Separation of concerns & PEP 8:** Decoupled layers (browser, scraper, cleaner, storage) with type hints and docstrings.

## Installation & Usage

### Quickstart

Clone the repository and enter the project folder:
```bash
git clone [https://github.com/vagner-lcf/playwright-quotes-scraper.git](https://github.com/vagner-lcf/playwright-quotes-scraper.git)
cd playwright-quotes-scraper
```

### Create and Activate a Virtual Environment

On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

On Linux/macOS (Bash):
```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies & Browsers

```bash
pip install -r requirements.txt
playwright install chromium
```

### Execute the ETL Pipeline

```bash
python main.py
```

### Output

The processed datasets will be saved in the `data/` directory:

- `data_yyyy-mm-dd.csv` — CSV encoded in `UTF-8-sig` for compatibility with Excel and Power BI.

Tip: open the folder after execution to inspect the generated files:

Windows PowerShell:
```powershell
explorer.exe .\data
```

Linux/macOS:
```bash
xdg-open data || open data
```

## Testing

Execute a suíte de testes com `pytest`:

```bash
python -m pytest
```

## Project Structure

```
playwright-quotes-scraper/
├── config/
│   ├── logger.py          # System logging configuration and formatting
│   └── settings.py        # Centralized execution parameters and constants
├── data/                  # Generated datasets (.csv)
├── src/
│   ├── browser.py         # Browser management and navigation resilience
│   ├── scraper.py         # Data extraction and pagination
│   ├── cleaner.py         # Sanitization, validation, and deduplication
│   └── storage.py         # Persistence and CSV file export handlers
├── tests/
│   └── test_cleaner.py    # Unit test suite
├── main.py                # Main pipeline orchestrator
├── requirements.txt
├── README.md
└── README.pt-br.md
```