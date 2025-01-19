import pandas as pd
import os

def convert_excel_to_csv(excel_path):
    """Convert Excel file to CSV"""
    try:
        # Read Excel file with error handling for different Excel formats
        try:
            df = pd.read_excel(excel_path, engine='openpyxl')
        except:
            # Try with older Excel format
            df = pd.read_excel(excel_path, engine='xlrd')
        
        # Clean column names
        df.columns = df.columns.str.strip()
        
        # Generate output path
        output_path = excel_path.rsplit('.', 1)[0] + '.csv'
        
        # Save to CSV with proper encoding
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"Successfully converted {excel_path} to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error converting Excel to CSV: {str(e)}")
        return False

def main():
    try:
        # Set Excel file path
        excel_path = input("Enter the path to your Excel file: ").strip()
        
        if not os.path.exists(excel_path):
            print("File not found!")
            return
            
        if not excel_path.lower().endswith(('.xlsx', '.xls')):
            print("File must be an Excel file (.xlsx or .xls)")
            return
            
        convert_excel_to_csv(excel_path)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 