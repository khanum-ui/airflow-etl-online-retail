import sqlite3
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Database location
database_path = project_folder / "data" / "retail.db"

# Connect to database
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Check table exists
cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='sales'"
)
table = cursor.fetchone()

# Check row count
cursor.execute("SELECT COUNT(*) FROM sales")
row_count = cursor.fetchone()[0]

# Check missing TotalSales values
cursor.execute("SELECT COUNT(*) FROM sales WHERE TotalSales IS NULL")
missing_total_sales = cursor.fetchone()[0]

connection.close()

print("Validation completed!")
print("Sales table exists:", table is not None)
print("Rows in sales table:", row_count)
print("Missing TotalSales values:", missing_total_sales)

if table is not None and row_count > 0 and missing_total_sales == 0:
    print("Data quality check: PASSED")
else:
    print("Data quality check: FAILED")
