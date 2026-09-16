import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Location of the raw dataset
input_file = project_folder / "data" / "Online Retail.xlsx"

# Location to save extracted data
output_file = project_folder / "data" / "raw_sales.csv"

# Extract: read the Excel file
df = pd.read_excel(input_file)

# Save extracted data as CSV
df.to_csv(output_file, index=False)

print("Extract completed successfully!")
print("Rows extracted:", len(df))
print("Extracted file:", output_file)