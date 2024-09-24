import pandas as pd
import os
from datetime import datetime

# Function to convert subscriber count to a number
def convert_subscribers(subscriber_str):
    if pd.isna(subscriber_str):
        return None
    subscriber_str = str(subscriber_str).lower().replace(',', '').strip()
    if 'k' in subscriber_str:
        return float(subscriber_str.replace('k', '').strip()) * 1000
    elif 'm' in subscriber_str:
        return float(subscriber_str.replace('m', '').strip()) * 1000000
    try:
        return float(subscriber_str)
    except ValueError:
        print(f"Unrecognized format: {subscriber_str}")
        return None

# Load the Excel file using openpyxl engine
input_file_path = r'C:\Users\uie78384\Downloads\Leads3.xlsx'
df = pd.read_excel(input_file_path, engine='openpyxl')

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()

# Display the first few rows of the 'Subscribers' column to inspect
print("Inspecting the first few rows of 'Subscribers' column:")
print(df['Subscribers'].head(10))

# Apply the conversion function to the 'Subscribers' column
df['Subscribers'] = df['Subscribers'].apply(convert_subscribers)

# Filter rows where subscribers are between 50,000 and 1,000,000
filtered_df = df[(df['Subscribers'] >= 50000) & (df['Subscribers'] <= 1000000)]

# Generate the current date and time
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

# Generate the output file path in the same directory as the input file
input_folder = os.path.dirname(input_file_path)
output_file_name = f"filtered_by_views_{current_time}.xlsx"
output_file_path = os.path.join(input_folder, output_file_name)

# Save the filtered data to a new Excel file
filtered_df.to_excel(output_file_path, index=False)

print(f"Filtering complete. Filtered data saved to '{output_file_path}'.")
