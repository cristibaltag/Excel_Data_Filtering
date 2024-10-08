import pandas as pd
import os

# Load the CSV file using the correct file path
file_path = r'C:\Users\uie78384\Downloads\all leads september 2024.csv'  # Using raw string
df = pd.read_csv(file_path)

# Filter rows where the 'Video Course' column contains "Yes", "Ye", or "y"
filtered_df = df[df['Video Course'].str.strip().str.lower().isin(['yes', 'ye', 'y'])]

# Save the filtered data to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)

print("Filtered data saved to 'filtered_data.csv'")
print("Current working directory:", os.getcwd())