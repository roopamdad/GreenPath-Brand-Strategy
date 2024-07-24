from crewai import Workflow, TaskSequence
from agents.data_analysis_agent import DataAnalysisAgent
from agents.dashboard_creation_agent import DashboardCreationAgent
from agents.documentation_agent import DocumentationAgent
from agents.video_presentation_agent import VideoPresentationAgent

class GreenPathWorkflow(Workflow):
    def __init__(self):
        data_analysis_agent = DataAnalysisAgent()
        dashboard_creation_agent = DashboardCreationAgent()
        documentation_agent = DocumentationAgent()
        video_presentation_agent = VideoPresentationAgent()

        self.workflow = TaskSequence(
            data_analysis_agent.perform_analysis(
                input_data_path='../data/sample_customer_feedback.csv',
                output_data_path='../data/processed_feedback.csv'
            ),
            dashboard_creation_agent.create_dashboard(
                input_data_path='../data/processed_feedback.csv',
                output_dashboard_path='../dashboards/CustomerFeedbackInsights.html'
            ),
            documentation_agent.create_presentation(
                output_pptx_path='../presentations/ExecutiveSummary.pptx'
            ),
            video_presentation_agent.create_video_presentation(
                output_video_path='../presentations/VideoPresentation.mp4'
            )
        )

    def run(self):
        self.workflow.run()
