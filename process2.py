import pandas as pd
import sys
import os

pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.max_rows", 100)  # Show up to 100 rows
pd.set_option("display.width", 150)  # Widen output

# Get user input for the folder path
folder_path = input("Enter the full path to the folder containing the CSV file: ")

# Validate the folder path
if not os.path.isdir(folder_path):
    print(f"Error: The specified path '{folder_path}' is not a valid directory. Please check the path and try again.")
    exit()

# Get the list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

if not csv_files:
    print(f"No CSV files found in the specified folder: {folder_path}")
    exit()

# Prompt the user to choose a CSV file from the list
for i, filename in enumerate(csv_files):
    print(f"{i + 1}. {filename}")

choice = input("Enter the number of the CSV file you want to use: ")

try:
    choice = int(choice) - 1  # Adjust for 1-based indexing
    filename = csv_files[choice]
    file_path = os.path.join(folder_path, filename)

    df = pd.read_csv(file_path, encoding="utf-8")

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

except (IndexError, ValueError):
    print("Invalid choice. Please enter a valid number from the list.")