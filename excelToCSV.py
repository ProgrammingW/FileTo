import pandas as pd
import os

def convert_excel_to_csv(excel_path):
    """Convert Excel file to CSV"""
    try:
        # Read Excel file
        df = pd.read_excel(excel_path)
        
        # Generate output path
        output_path = excel_path.rsplit('.', 1)[0] + '.csv'
        
        # Save to CSV
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")
        
    except Exception as e:
        print(f"Error converting Excel to CSV: {str(e)}")

def main():
    # Set Excel file path
    excel_path = input("Enter the path to your Excel file: ")
    
    if not os.path.exists(excel_path):
        print("File not found!")
        return
        
    convert_excel_to_csv(excel_path)

if __name__ == "__main__":
    main() 