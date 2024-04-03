import pandas as pd
import sys
import os
import tkinter as tk
from tkinter import filedialog, ttk

# Set pandas display options
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 150)

def process_csv():
    """Function to process the selected CSV file."""
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if file_path:
        try:
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

            status_label.config(text="CSV processed successfully!")

        except FileNotFoundError:
            status_label.config(text=f"Error: The selected file '{file_path}' was not found.")
    else:
        status_label.config(text="No file selected.")

# Create the main window
root = tk.Tk()
root.title("CSV Processor")

# Create a button to trigger the process
process_button = ttk.Button(root, text="Process CSV", command=process_csv)
process_button.pack()

# Create a label to display status messages
status_label = ttk.Label(root, text="")
status_label.pack()

# Start the main event loop
root.mainloop()