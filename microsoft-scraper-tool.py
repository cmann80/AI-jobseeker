from langchain.agents import initialize_agent, Tool
from langchain.tools import BaseTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
import requests
from bs4 import BeautifulSoup
import json

@tool
def microsoft_career_search(query: str) -> str:
    """Searches Microsoft's career page for jobs \
        that match a given string. Required to find \
        the base URL for a job listing. The input to this \
        tool should be a keyword of the job description title."""
        
    url = f"https://careers.microsoft.com/v2/global/en/home.html"
    headers = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' }
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text)
    
    elements = soup.select("[class*='ms-list']")
    
    return str(elements)