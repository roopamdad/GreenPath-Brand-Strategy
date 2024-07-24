from crewai import Agent, Task
import pandas as pd
import plotly.express as px

class DashboardCreationAgent(Agent):
    @Task()
    def create_dashboard(self, input_data_path: str, output_dashboard_path: str):
        # Load processed data
        data = pd.read_csv(input_data_path)

        # Example Dashboard using Plotly
        fig = px.histogram(data, x='ProductCategory', color='SatisfactionLevel', title='Customer Feedback by Product Category and Satisfaction Level')
        fig.write_html(output_dashboard_path)
