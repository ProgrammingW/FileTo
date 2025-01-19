# PDF Table Extractor

A Python script that extracts tables from PDF files and converts them to either CSV or JSON format.

## Features
- Extract tables from specific PDF pages
- Convert tables to CSV or JSON format
- Support for multiple pages
- Error handling for invalid pages or missing tables

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

3. Create a virtual environment:
```bash
python -m venv .venv
```

4. Activate the virtual environment:
```bash
source .venv/bin/activate
```

5. Install the required packages:
```bash
python3 -m pip install pandas pdfplumber
```

6. Run the script:
```bash
chmod +x run.sh
./run.sh
```

The script will prompt you to:
1. Select a page number from the PDF
2. Choose output format (CSV or JSON)

## Output
The converted file will be saved in the same location as the input PDF with either `.csv` or `.json` extension.

## Notes
- The script assumes that the PDF has a table on the specified page. If the table is not found, the script will print an error message.
- The script uses the `pdfplumber` library to extract the tables from the PDF.
- The script uses the `pandas` library to convert the tables to CSV or JSON format.
