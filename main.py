def display_menu():
    print("\n=== File Converter & Analyzer ===")
    print("1. PDF to CSV/JSON")
    print("2. Excel to CSV")
    print("3. CSV to JSON")
    print("4. Analyze Excel Data")
    print("5. Exit")
    return input("\nChoose an option (1-5): ")

def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            import pdfToCSV
            pdfToCSV.main()
        elif choice == '2':
            import excelToCSV
            excelToCSV.main()
        elif choice == '3':
            import csvToJSON
            csvToJSON.main()
        elif choice == '4':
            import dataAnalyzer
            dataAnalyzer.main()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main() 