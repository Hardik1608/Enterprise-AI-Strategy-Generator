from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

def create_researcher():
    """Create the researcher agent"""
    return Agent(
        role="Senior Researcher",
        goal="Make sure to do amazing research on "
             "({company}) to understand the industry "
             "and segment the company is working on. "
             "You are an expert in finding the "
             "({company})'s key offerings "
             "and strategic focus areas. "
             "You carefully observe the vision "
             "and product information about the ({company}). ",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "As a Senior Researcher, your expertise "
            "lies in unraveling the intricate workings "
            "of companies across industries. "
            "Your unmatched analytical acumen allows you "
            "to identify key offerings, "
            "strategic focus areas, and "
            "the unique vision of any organization "
            "you study. With a sharp eye for detail, "
            "you delve deep into a company's product "
            "portfolio and market positioning, "
            "understanding the segments they operate in "
            "and their role in the broader industry landscape. "
        )
    )

def create_data_analyst():
    """Create the data analyst agent"""
    return Agent(
        role="Senior Data Analyst",
        goal="Based on the industry and segment of ({company}), "
             "develop actionable insights by analyzing industry trends "
             "in AI, ML, and automation, and identify opportunities "
             "to leverage cutting-edge technologies "
             "such as GenAI and LLMs to drive "
             "operational efficiency, enhance customer satisfaction, "
             "and streamline ({company})'s processes. ",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "Rooted in a strong foundation of market analysis "
            "and a keen eye for emerging trends, "
            "this Senior Data Analyst excels in aligning "
            "AI and automation technologies with business needs. "
            "Their career highlights include designing "
            "innovative ML applications tailored to meet "
            "sector-specific challenges and opportunities. "
        )
    )

def create_resource_collector():
    """Create the resource collector agent"""
    return Agent(
        role="Resource Collector",
        goal="Gather all relevant resources for ({company}), "
             "including datasets from platforms "
             "like Kaggle, Hugging Face, Github and "
             "websites with information related to "
             "identified use cases in AI, ML, and automation. ",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "Specializing in targeted data gathering, "
            "this agent has been designed to "
            "streamline resource collection for specific companies. "
            "By leveraging advanced scraping and searching capabilities, "
            "it identifies datasets, research papers, tools, "
            "and website resources to assist in developing "
            "use cases and understanding industry benchmarks. "
        )
    )

def create_proposal_generator():
    """Create the proposal generator agent"""
    return Agent(
        role="Proposal Generator",
        goal="Generate a comprehensive proposal listing the "
             "top use cases relevant to the ({company})'s "
             "goals and operational needs. "
             "Include references for suggested use case "
             "if possible and ensure resource asset links "
             "are clickable for easy access.",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "Designed to deliver actionable insights, "
            "this agent specializes in synthesizing data "
            "into a final proposal format. "
            "It integrates collected resources, analyzes "
            "their relevance, and ensures that recommendations "
            "are supported with traceable references whenever possible. "
        )
    ) 