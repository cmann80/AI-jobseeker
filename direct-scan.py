from dotenv import load_dotenv
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
tools = load_tools(["serpapi", "llm-math", "PythonREPL"], llm = llm)

# one shot indicates that it will feed all messages to the model at once
agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

results = agent.run(
            """You are a job searching agent. Follow the following steps:
            1. Scan the page https://www.thesoftwarereport.com/the-top-100-software-companies-of-2022/ 
            2. Google careers for that company that contain the string "generative AI" and read the job listing
            3. If one is found, return a JSON object with the following keys: Company name, position name, URL link to the job posting
            4. If none are found, return "none found"
            """
)

print(results)
