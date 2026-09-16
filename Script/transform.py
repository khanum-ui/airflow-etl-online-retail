import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the extracted CSV file
input_file = project_folder / "data" / "raw_sales.csv"

df = pd.read_csv(input_file)

print("Original rows:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing descriptions
df = df.dropna(subset=["Description"])

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create TotalSales
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

# Save transformed data
output_file = project_folder / "data" / "transformed_sales.csv"
df.to_csv(output_file, index=False)

print("Transformed rows:", len(df))
print("Transformed file:", output_file)
print("\nTransformation completed successfully!")