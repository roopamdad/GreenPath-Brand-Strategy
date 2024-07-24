import pandas as pd
import plotly.express as px

# Load processed data
data = pd.read_csv('../data/processed_feedback.csv')

# Example Dashboard using Plotly
fig = px.histogram(data, x='ProductCategory', color='SatisfactionLevel', title='Customer Feedback by Product Category and Satisfaction Level')
fig.write_html('../dashboards/CustomerFeedbackInsights.html')
