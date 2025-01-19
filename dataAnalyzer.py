import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_excel(excel_path):
    """Analyze Excel file and create visualizations"""
    try:
        # Read Excel file
        df = pd.read_excel(excel_path, engine='openpyxl')
        
        # Create output directory for plots
        output_dir = 'analysis_output'
        os.makedirs(output_dir, exist_ok=True)
        
        # Get numerical columns
        numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
        
        if len(numerical_cols) == 0:
            print("No numerical columns found for analysis")
            return False
            
        # Create different types of plots
        # 1. Correlation Heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/correlation_heatmap.png')
        plt.close()
        
        # 2. Box Plots
        plt.figure(figsize=(12, 6))
        df[numerical_cols].boxplot()
        plt.xticks(rotation=45)
        plt.title('Box Plots of Numerical Columns')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/boxplots.png')
        plt.close()
        
        # 3. Histograms
        df[numerical_cols].hist(figsize=(12, 8))
        plt.suptitle('Histograms of Numerical Columns')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/histograms.png')
        plt.close()
        
        # Basic statistical analysis
        stats = df[numerical_cols].describe()
        stats.to_csv(f'{output_dir}/statistical_summary.csv')
        
        print(f"Analysis complete! Check the '{output_dir}' folder for results")
        print("\nBasic Statistics:")
        print(stats)
        return True
        
    except Exception as e:
        print(f"Error analyzing Excel file: {str(e)}")
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
            
        analyze_excel(excel_path)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 