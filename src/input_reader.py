from pathlib import Path

import pandas as pd


WORKBOOK_PATH = Path("data/sample_diagram_input.xlsx")


def load_workbook_data(path: Path = WORKBOOK_PATH) -> dict[str, pd.DataFrame]:
    """Load the three required worksheets from the sample Excel workbook."""
    if not path.exists():
        raise FileNotFoundError(f"Workbook not found: {path}")

    required_sheets = ["Components", "Connections", "Symbols"]
    workbook = pd.read_excel(path, sheet_name=required_sheets, dtype=str)

    for sheet_name, dataframe in workbook.items():
        if dataframe.empty:
            raise ValueError(f"Worksheet '{sheet_name}' contains no data.")
        dataframe.columns = [str(column).strip() for column in dataframe.columns]

    return workbook