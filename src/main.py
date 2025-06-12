import warnings
from crewai import Crew, Process
from IPython.display import Markdown

from config.config import load_env
from agents.agents import (
    create_researcher,
    create_data_analyst,
    create_resource_collector,
    create_proposal_generator
)
from tasks.tasks import (
    create_research_task,
    create_use_case_task,
    create_resource_collection_task,
    create_final_proposal_task
)

# Suppress warnings
warnings.filterwarnings('ignore')

def create_crew(company_name):
    """Create and configure the crew with all agents and tasks"""
    # Create agents
    researcher = create_researcher()
    data_analyst = create_data_analyst()
    resource_collector = create_resource_collector()
    proposal_generator = create_proposal_generator()

    # Create tasks
    research_task = create_research_task(researcher)
    use_case_task = create_use_case_task(data_analyst)
    resource_task = create_resource_collection_task(resource_collector)
    proposal_task = create_final_proposal_task(proposal_generator)

    # Create and return the crew
    return Crew(
        agents=[
            researcher,
            data_analyst,
            resource_collector,
            proposal_generator
        ],
        tasks=[
            research_task,
            use_case_task,
            resource_task,
            proposal_task
        ],
        process=Process.sequential,
        memory=True,
        verbose=True
    )

def main():
    """Main function to run the use case generation process"""
    # Load environment variables
    load_env()

    # Define target company
    target_company = {
        'company': 'Amazon'  # This can be made configurable
    }

    # Create and run the crew
    crew = create_crew(target_company['company'])
    result = crew.kickoff(inputs=target_company)

    # Display results
    Markdown(result)

if __name__ == "__main__":
    main() 