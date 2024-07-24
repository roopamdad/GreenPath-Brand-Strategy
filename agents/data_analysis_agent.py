from crewai import Agent, Task
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysisAgent(Agent):
    @Task()
    def perform_analysis(self, input_data_path: str, output_data_path: str):
        # Load sample customer feedback data
        data = pd.read_csv(input_data_path)

        # Perform basic data analysis
        print("Data Head:\n", data.head())
        print("\nSummary Statistics:\n", data.describe())

        # Data Cleaning
        data.dropna(inplace=True)

        # Data Analysis - Example: Customer Interest in Zero-Waste Products
        interest_data = data[data['Interest'] == 'Zero-Waste']
        print("\nInterest in Zero-Waste Products:\n", interest_data)

        # Visualization
        plt.figure(figsize=(10, 6))
        sns.countplot(x='SatisfactionLevel', data=interest_data)
        plt.title('Customer Satisfaction Levels for Zero-Waste Products')
        plt.xlabel('Satisfaction Level')
        plt.ylabel('Count')
        plt.savefig('../docs/zero_waste_satisfaction_analysis.png')
        plt.show()

        # Save processed data
        data.to_csv(output_data_path, index=False)
