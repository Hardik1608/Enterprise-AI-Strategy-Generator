from crewai import Task

def create_research_task(researcher):
    """Create the research task"""
    return Task(
        description=(
            "Use a Web browser tool and understand the industry and "
            "segment the ({company}) is working in "
            "(e.g., Automotive, Manufacturing, Finance, Retail, Healthcare, etc.). "
            "Identify the company's key offerings and strategic focus areas "
            "(e.g., operations, supply chain, customer experience, etc.). "
            "A vision and product information on the industry should be fine as well. "
        ),
        expected_output=(
            "A summary of the industry and segment the company operates in, "
            "highlighting key offerings, strategic focus areas, vision, and product information. "
        ),
        agent=researcher,
    )

def create_use_case_task(data_analyst):
    """Create the use case generation task"""
    return Task(
        description=(
            "Based on the industry conducted, analyze industry trends"
            "and standards within the ({company})'s sector"
            "related to AI, ML, and automation."
            "Propose relevant use cases where ({company})"
            "can leverage GenAI, LLMs, and ML technologies"
            "to improve their processes, enhance customer satisfaction,"
            "and boost operational efficiency."
        ),
        expected_output=(
            "A list of industry trends and standards in AI, ML, and automation, "
            "along with proposed use cases for ({company}) "
            "to leverage these technologies."
            "Each use case should include a brief description,"
            "potential benefits, and relevance to ({company})'s operations."
        ),
        agent=data_analyst
    )

def create_resource_collection_task(resource_collector):
    """Create the resource collection task"""
    return Task(
        description=(
            "Collect the above use cases generated and search for "
            "relevant datasets on platforms like Kaggle, HuggingFace, and GitHub. "
            "Save the resource links fetched in a text or markdown file. "
        ),
        expected_output=(
            "A markdown or text file containing a list of use cases, "
            "brief description of each use case"
            "with their corresponding reference links, "
            "including datasets and tools from platforms "
            "like Kaggle, HuggingFace, and GitHub. "
        ),
        output_file='resources.md',
        agent=resource_collector
    )

def create_final_proposal_task(proposal_generator):
    """Create the final proposal task"""
    return Task(
        description=(
            "List down the top use cases "
            "that can be delivered to the customer,"
            "ensuring they are relevant to "
            "({company})'s goals and operational needs."
            "Ensure to add references through which"
            "certain use cases were suggested"
            "Resource Asset links should be clickable."
        ),
        expected_output=(
            "A markdown file containing "
            "the use cases aligned with "
            "({company})'s goals and operational needs. "
            "Each use case should include a brief description, "
            "AI Application, and cross-functional benefits. "
        ),
        output_file='proposal.md',
        agent=proposal_generator
    ) 