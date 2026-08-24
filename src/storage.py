"""Module responsible for persisting and exporting sanitized data to CSV format.
"""

from datetime import datetime
from pathlib import Path
import pandas as pd
import logging
from config.settings import OUTPUT_DIR


def save_to_csv(data: list[dict[str, str]], output_dir: str = OUTPUT_DIR) -> None:
    """Exports structured data to a CSV file in an idempotent manner.

    Ensures the target directory exists and names the file using the current date 
    in the 'data_YYYY-MM-DD.csv' format. If a file already exists for the current 
    date, it will be overwritten to maintain data consistency.

    Args:
        data (list[dict[str, str]]): List of dictionaries containing validated records to save.
        output_dir (str, optional): Target directory path for the output file. 
            Defaults to OUTPUT_DIR.
    """
    if not data:
        logging.warning("No data to export. Skipping CSV generation.")
        return

    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    file_date = datetime.now().strftime("%Y-%m-%d")
    file_name = f"data_{file_date}.csv"
    file_path = target_dir / file_name

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding="utf-8-sig")
    logging.info(f"Data successfully exported: {file_path}")