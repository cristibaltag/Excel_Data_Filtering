import pandas as pd
import re
import os
from datetime import datetime

# List of keywords to search for
keywords = [
    "ndian", "Hindi", "Lakh", "Hoe Werkt", "Urdu", "Lakhs", "Rs.", "Podcast",
    "Flip", "Flipping", "gym", "gymnastics", "Dog", "Cocomelon", "React",
    "Reacts", "Reaction", "Bet", "Queen", "Security Guard", "Chinese",
    "Pakistan", "₹", "Ep", "Lecture", "Documentary", "Airline", "Airplane",
    "travel", "Jet", "News", "Manga", "Step sister", "Ghost", "Detective",
    "Case", "Kendrick", "Drake", "Horror"
]

# Compile regex patterns for keywords, including any number patterns for specific keywords
patterns = [re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE) for keyword in keywords]
patterns.append(re.compile(r'\bEp\s*\d+\b', re.IGNORECASE))  # Pattern for "Ep # (number)"
patterns.append(re.compile(r'\b#\d+\b', re.IGNORECASE))  # Pattern for "# (number)"

# Pattern for Arabic script (using Unicode range for Arabic)
arabic_range = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB70-\uFBFE\uFE70-\uFEFF]', re.UNICODE)
patterns.append(arabic_range)

def contains_keywords(text):
    if pd.isna(text):
        return False
    text = str(text)
    return any(pattern.search(text) for pattern in patterns)

# Load the CSV file
input_file = r'C:\Users\uie78384\OneDrive - Continental AG\Desktop\filtered_data2.csv'
df = pd.read_csv(input_file)

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()

# Print the first few rows to inspect
print("Inspecting the first few rows of the dataframe:")
print(df.head())

# Remove rows where any column contains any of the specified keywords
mask = df.applymap(contains_keywords).any(axis=1)
df_cleaned = df[~mask]

# Create a unique filename with a timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'C:\\Users\\uie78384\\OneDrive - Continental AG\\Desktop\\cleaned_data_{timestamp}.csv'

# Save the cleaned data to a new CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaning complete. Filtered data saved to '{output_file}'.")
