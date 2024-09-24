import pandas as pd
import re
import os
from datetime import datetime

# List of keywords and patterns to search for, including new ones
keywords = [
    "Indian", "Hindi", "Lakh", "Hoe Werkt", "Urdu", "Lakhs", "Rs.", "Podcast",
    "Flip", "Flipping", "gym", "gymnastics", "Dog", "Cocomelon", "React",
    "Reacts", "Reaction", "Bet", "Queen", "Security Guard", "Chinese",
    "Pakistan", "₹", "Ep", "Lecture", "Documentary", "Airline", "Airplane",
    "travel", "Jet", "News", "Manga", "Step sister", "Ghost", "Detective",
    "Case", "Kendrick", "Drake", "Horror", "Telugu",
    "Live session", "Dave Ramsey", "€™", "Jay Leno", "Jay Leno's", "live stream",
    "live", "stream", "fairytale", "house", "building", "organize", "declutter",
    "strongest man", "Lucifer", "Bananas", "survive", "Dumpster Diving", "Adin Ross",
    "Date", "Ùƒ", "Hotukdeals", "India", "Come fare", "grand tours", "climate",
    "Drama", "Series", "aesthetic", "Cindy Trimm", "BBQ", "Google", "emirates",
    "qatar", "AER LINGUS", "airplane", "music", "playlist", "vlog", "GTA",
    "train", "seat", "bangla", "corrupt", "Ethereal Workshop", "Brooklyn", "Surveillance"
]

# Compile regex patterns for keywords
patterns = [re.compile(rf'{re.escape(keyword)}', re.IGNORECASE) for keyword in keywords]
patterns.append(re.compile(r'\bEp\s*\d+\b', re.IGNORECASE))  # Pattern for "Ep # (number)"
patterns.append(re.compile(r'\b#\d+\b', re.IGNORECASE))  # Pattern for "# (number)"
patterns.append(re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB70-\uFBFE\uFE70-\uFEFF]', re.UNICODE))  # Arabic script

def contains_keywords(text):
    """Check if the text contains any of the specified keywords or patterns."""
    if pd.isna(text):
        return False
    text = str(text)
    return any(pattern.search(text) for pattern in patterns)

def clean_data(input_file, output_file):
    """Load data from Excel, filter it, and save cleaned data to a new Excel file."""
    try:
        df = pd.read_excel(input_file, engine='openpyxl')
        df.columns = df.columns.str.strip()  # Remove extra spaces from column names

        print("Inspecting the first few rows of the dataframe:")
        print(df.head())

        # Filter rows where any column contains any of the specified keywords
        mask = df.applymap(contains_keywords).any(axis=1)
        df_cleaned = df[~mask]

        # Save the cleaned data to a new Excel file
        df_cleaned.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Cleaning complete. Filtered data saved to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Define input and output file paths
input_file = r'C:\Users\uie78384\Downloads\Leads3.xlsx'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'C:\\Users\\uie78384\\OneDrive - Continental AG\\Desktop\\cleaned_data_{timestamp}.xlsx'

# Execute the cleaning function
clean_data(input_file, output_file)
