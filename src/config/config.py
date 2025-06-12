import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    """Load environment variables from .env file"""
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    """Get OpenAI API key from environment variables"""
    load_env()
    return os.getenv("OPENAI_API_KEY")

def get_serper_api_key():
    """Get Serper API key from environment variables"""
    load_env()
    return os.getenv("SERPER_API_KEY")

def get_openai_model_name():
    """Get OpenAI model name from environment variables"""
    load_env()
    return os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

# Initialize API keys
OPENAI_API_KEY = get_openai_api_key()
SERPER_API_KEY = get_serper_api_key()
OPENAI_MODEL_NAME = get_openai_model_name() 