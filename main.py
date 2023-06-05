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

# streamlit interface elements
st.write("Searching for jobs at all companies at https://www.thesoftwarereport.com/the-top-100-software-companies-of-2022/")
submit = st.button("Search")

results = agent.run(
            """You are a job searching agent. Follow the following steps:
            1. Scan the page https://www.thesoftwarereport.com/the-top-100-software-companies-of-2022/ , find each of the company's job page 
            2. Google each of the companies' careers page
            3. On that page, identify each job listing that includes the word "junior"
            4. Create a JSON object with the following keys: Company name, position name, URL link to the job posting
            """
)

# logic connected to the submit button
if submit:
    st.header("Response")
    with st.spinner(text = "Please Wait"):
        st.write(results)