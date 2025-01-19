# File Converter

A Python-based file conversion tool that supports multiple file formats.

## Features
- PDF tables to CSV/JSON conversion
- Excel to CSV conversion
- CSV to JSON conversion
- User-friendly menu interface

## Prerequisites
- Python 3.x
- Virtual environment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ProgrammingW/FileTo.git
```

2. Navigate to the project directory:
```bash
cd FileTo
```

3. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install required packages:
```bash
python3 -m pip install pandas pdfplumber openpyxl
```

## Usage

1. Make the run script executable (one-time setup):
```bash
chmod +x run.sh
```

2. Run the application:
```bash
./run.sh
```

3. Choose from the available conversion options in the menu:
   - Option 1: Convert PDF tables to CSV/JSON
   - Option 2: Convert Excel files to CSV
   - Option 3: Convert CSV files to JSON
   - Option 4: Exit

## Supported Conversions
- PDF tables to CSV/JSON
- Excel (.xlsx, .xls) to CSV
- CSV to JSON

## Notes
- Each converter has its own specific requirements and limitations
- Make sure your input files are in the correct format
- For PDF conversion, tables must be present in the document
- For Excel conversion, the first sheet will be converted by default
