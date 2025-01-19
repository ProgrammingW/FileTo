import pandas as pd
import json
import os

def convert_csv_to_json(csv_path):
    """Convert CSV file to JSON"""
    try:
        # Read CSV file
        df = pd.read_csv(csv_path)
        
        # Generate output path
        output_path = csv_path.rsplit('.', 1)[0] + '.json'
        
        # Convert to JSON
        json_data = df.to_dict(orient='records')
        
        # Save to JSON file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)
            
        print(f"Data successfully saved to {output_path}")
        
    except Exception as e:
        print(f"Error converting CSV to JSON: {str(e)}")

def main():
    # Set CSV file path
    csv_path = input("Enter the path to your CSV file: ")
    
    if not os.path.exists(csv_path):
        print("File not found!")
        return
        
    convert_csv_to_json(csv_path)

if __name__ == "__main__":
    main() 