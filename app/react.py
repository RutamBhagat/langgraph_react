from dotenv import load_dotenv, find_dotenv
from langchain import hub
from langchain.agents import create_react_agent
from langchain.prompts import PromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

_ = load_dotenv(find_dotenv())

react_prompt: PromptTemplate = hub.pull("hwchase17/react")


@tool
def triple(num: float) -> float:
    """
    :param num: A number to triple
    :return: The number tripled -> multiplied by 3
    """
    return float(num) * 3


tools = [TavilySearchResults(max_results=1), triple]

llm = ChatOpenAI()

react_agent_runnable = create_react_agent(llm, tools, react_prompt)
