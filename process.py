import pandas as pd
import sys

pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.max_rows", 100)  # Show up to 100 rows
pd.set_option("display.width", 150)  # Widen output
df = pd.read_csv("fort_small.csv", encoding="utf-8")

value = df[
    [
        "First Name",
        "Last Name",
        "Phone 1",
        "Property Address",
        "Property City",
        "Property State",
        "Property Zip",
    ]
]

with open("output.txt", "w") as f:
    sys.stdout = f  # Redirect stdout to the file
    print(value)
