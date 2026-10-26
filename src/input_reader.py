
from pathlib import Path
import pandas as pd

# Location of the Excel workbook
file_path = Path("data/sample_diagram_input.xlsx")


def load_workbook_data(path=file_path):
    # Step 1: Check whether the Excel file exists
    if not path.exists():
        raise FileNotFoundError(f"Excel file not found: {path}")

    # Step 2: Define the worksheet names we need
    sheet_names = ["Components", "Connections", "Symbols"]

    # Step 3: Read all three worksheets into Python
    data = pd.read_excel(
        path,
        sheet_name=sheet_names,
        dtype=str
    )

    # Step 4: Check each worksheet
    for sheet_name in sheet_names:
        table = data[sheet_name]

        # Stop if the worksheet has no data
        if table.empty:
            raise ValueError(
                f"The worksheet '{sheet_name}' is empty."
            )

        # Remove extra spaces from column names
        table.columns = table.columns.str.strip()

    # Step 5: Return all three worksheets
    return data
