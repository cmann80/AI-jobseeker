from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

load_dotenv()

# setting temperature to 0 to get reliable JSON output
chat = ChatOpenAI(temperature=0)
llm = OpenAI(temperature=0)

# serpapi allows the access of Google
tools = load_tools(["serpapi", "llm-math"], llm = llm)

# one shot indicates that it will feed all messages to the model at once
agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

results = agent.run(
            """You are a job searching agent. Follow the following steps:
            1. Scan the page https://www.thesoftwarereport.com/the-top-100-software-companies-of-2022/ 
            2. Google the careers page of a random company on that list
            3. Create a Python function to scrape the careers page of the page you Googled, by the following steps:\
                a. search for jobs with the keyword "AI"
                b. follow the link to the first entry of the results
                d. create a JSON object for the the following information from the job description: \
                company name, job title, job description URL
            4. Run the function using PythonREPL to confirm it returns something
            5. output the function, along with these instructions
            """
)