import pandas as pd

import random

import email_handler

def read_spreadsheet(path: str) -> pd.DataFrame:
    """
    Returns values from Excel spreadsheet
    Give path as raw string for Windows style paths
    """
    return pd.read_excel(path, engine="openpyxl")

def main():
    quotes_sheet = read_spreadsheet(r".\MotivationalQuotes.xlsx")
    random_index = random.randint(0, len(quotes_sheet['Quote']))
    random_quote = quotes_sheet.iloc[random_index]['Quote']
    author = quotes_sheet.iloc[random_index]['Author']
    message = email_handler.form_email(random_quote, author)
    email_handler.send_email(message)

if __name__ == "__main__":
    main()