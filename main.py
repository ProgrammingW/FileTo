def display_menu():
    print("\n=== File Converter ===")
    print("1. PDF to CSV/JSON")
    print("2. Excel to CSV")
    print("3. CSV to JSON")
    print("4. Exit")
    return input("\nChoose an option (1-4): ")

def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            import pdfToCSV
            pdfToCSV.main()
        elif choice == '2':
            print("Excel to CSV conversion - Coming soon!")
        elif choice == '3':
            print("CSV to JSON conversion - Coming soon!")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main() 