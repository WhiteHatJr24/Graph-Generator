"""
Title: Data Analysis on Sales Dataset
Author: Aditya Mohanta

Description:
This program performs exploratory data analysis (EDA) on a sample sales dataset.
It demonstrates data cleaning, statistical analysis, and visualization techniques
using Python libraries such as pandas, matplotlib, and seaborn.
"""

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("⚠️ File not found. Creating a sample dataset instead.")
        # Creating a sample dataset for demonstration
        data = pd.DataFrame({
            "Region": ["East", "West", "North", "South", "East", "West"],
            "Product": ["A", "B", "C", "A", "B", "C"],
            "Sales": [200, 340, 150, 400, 320, 270],
            "Profit": [50, 80, 40, 100, 70, 65]
        })
        data.to_csv(file_path, index=False)
        print(f"Sample dataset created and saved as {file_path}")
        return data

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values and duplicates."""
    print("\n🔍 Cleaning Data...")
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    print("✅ Data cleaned successfully.")
    return df

def analyze_data(df: pd.DataFrame):
    """Perform basic statistical analysis."""
    print("\n📊 Statistical Summary:")
    print(df.describe())

    print("\n💡 Insights:")
    top_region = df.groupby("Region")["Sales"].sum().idxmax()
    print(f"- Region with highest total sales: {top_region}")

    top_product = df.groupby("Product")["Profit"].sum().idxmax()
    print(f"- Product with highest total profit: {top_product}")

def visualize_data(df: pd.DataFrame):
    """Visualize sales and profit using bar charts."""
    print("\n📈 Generating Visualizations...")
    plt.figure(figsize=(8, 4))
    sns.barplot(x="Region", y="Sales", data=df, palette="viridis")
    plt.title("Total Sales by Region")
    plt.savefig("sales_by_region.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    sns.barplot(x="Product", y="Profit", data=df, palette="magma")
    plt.title("Profit by Product")
    plt.savefig("profit_by_product.png")
    plt.close()
    print("✅ Charts saved as 'sales_by_region.png' and 'profit_by_product.png'")

def main():
    """Main function to execute all steps."""
    file_path = "sales_data.csv"
    df = load_data(file_path)
    df = clean_data(df)
    analyze_data(df)
    visualize_data(df)
    print("\n🎯 Data analysis completed successfully!")

if __name__ == "__main__":
    main()
