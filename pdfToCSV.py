import pdfplumber
import pandas as pd
import json
import sys

def extract_pdf_data(pdf_path, page_number):
    """Extract data from specified PDF page"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Check if page number is valid
            if page_number < 1 or page_number > len(pdf.pages):
                raise ValueError(f"Invalid page number. PDF has {len(pdf.pages)} pages.")
            
            # Extract table from the specified page (subtract 1 as pages are 0-indexed)
            page = pdf.pages[page_number - 1]
            tables = page.extract_tables()
            
            if not tables:
                raise ValueError("No tables found on the specified page.")
            
            return tables
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
        return None

def save_to_csv(data, output_path):
    """Save extracted data to CSV file"""
    try:
        # Convert table data to pandas DataFrame
        df = pd.DataFrame(data[0][1:], columns=data[0][0])
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving to CSV: {str(e)}")

def save_to_json(data, output_path):
    """Save extracted data to JSON file"""
    try:
        # Convert table data to dictionary
        headers = data[0][0]
        rows = data[0][1:]
        json_data = [dict(zip(headers, row)) for row in rows]
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)
        print(f"Data successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving to JSON: {str(e)}")

def main():
    # Set PDF file path directly
    pdf_path = "/Users/jrodriguez/Downloads/mercado.pdf"
    
    try:
        # Open PDF to get page count
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"PDF has {total_pages} pages")
        
        # Get page number from user
        page_number = int(input(f"Enter the page number to extract (1-{total_pages}): "))
        
        # Get output format preference
        format_choice = input("Choose output format (csv/json): ").lower()
        
        # Extract data
        data = extract_pdf_data(pdf_path, page_number)
        
        if data:
            # Generate output filename
            output_path = pdf_path.rsplit('.', 1)[0]
            
            if format_choice == 'csv':
                save_to_csv(data, f"{output_path}.csv")
            elif format_choice == 'json':
                save_to_json(data, f"{output_path}.json")
            else:
                print("Invalid format choice. Please choose 'csv' or 'json'.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
