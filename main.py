import pandas as pd

import traceback
import random
from pathlib import Path
from datetime import datetime


import email_handler


LOG_FILE = Path(__file__).parent / "error.log"
BASE_DIR = Path(__file__).parent

def read_spreadsheet(path: Path) -> pd.DataFrame:
    """
    Returns values from Excel spreadsheet
    Give path as raw string for Windows style paths
    """
    return pd.read_excel(path, engine="openpyxl")

def main():
    quotes_sheet = read_spreadsheet(BASE_DIR / "MotivationalQuotes.xlsx")
    random_index = random.randint(0, len(quotes_sheet['Quote']))
    random_quote = quotes_sheet.iloc[random_index]['Quote']
    author = quotes_sheet.iloc[random_index]['Author']
    message = email_handler.form_email(random_quote, author)
    email_handler.send_email(message)

if __name__ == "__main__":
    # logging errors in case they occur while console is not visible
    try:
        main()
    except Exception:
        with open(LOG_FILE, "w") as f:
            f.write(f"\n ---{datetime.now()} ---\n")
            f.write(traceback.format_exc())