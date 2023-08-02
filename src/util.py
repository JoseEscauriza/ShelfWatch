from pathlib import Path
from typing import List, Any

from tabulate import tabulate

ROOT_DIR = Path(__file__).parent.parent


def display_table(table_headers: List[str], data: List[Any]):
    table = [tab for tab in data]
    print(tabulate(table, headers=table_headers, tablefmt='fancy_grid'))
