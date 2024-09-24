import pandas as pd

# Function to convert subscriber count to a number
def convert_subscribers(subscriber_str):
    if pd.isna(subscriber_str):
        return None
    subscriber_str = str(subscriber_str).lower().replace(',', '')
    if 'k' in subscriber_str:
        return float(subscriber_str.replace('k', '').strip()) * 1000
    elif 'm' in subscriber_str:
        return float(subscriber_str.replace('m', '').strip()) * 1000000
    else:
        return float(subscriber_str)

# File paths
input_file_path = r'C:\Users\uie78384\Downloads\Leads3.1.csv'
output_file_path = r'C:\Users\uie78384\Downloads\Filtered_Leads.csv'

def read_csv_with_encoding(file_path):
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'windows-1252']
    for encoding in encodings:
        try:
            print(f"Trying encoding: {encoding}")
            return pd.read_csv(file_path, delimiter='\t', encoding=encoding)
        except UnicodeDecodeError:
            print(f"Failed with encoding: {encoding}")
        except pd.errors.ParserError as e:
            print(f"ParserError with encoding '{encoding}': {e}")
            break
    raise ValueError("Unable to read CSV file with available encodings.")

try:
    # Read the CSV file with error handling
    df = read_csv_with_encoding(input_file_path)

    # Ensure the DataFrame has the expected columns
    if 'Subscribers' not in df.columns:
        raise ValueError("The 'Subscribers' column is not found in the CSV file.")

    # Apply the conversion function to the 'Subscribers' column
    df['Subscribers'] = df['Subscribers'].apply(convert_subscribers)

    # Filter rows where subscribers are between 20,000 and 1,500,000
    filtered_df = df[(df['Subscribers'] >= 20000) & (df['Subscribers'] <= 1500000)]

    # Save the filtered data to a new CSV file
    filtered_df.to_csv(output_file_path, index=False)

    print(f"Filtering complete. Filtered data saved to '{output_file_path}'.")

except Exception as e:
    print(f"An error occurred: {e}")
