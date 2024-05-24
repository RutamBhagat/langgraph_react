from dotenv import load_dotenv, find_dotenv
from langgraph.prebuilt import ToolExecutor
from app.state import AgentState
from react import react_agent_runnable, tools

_ = load_dotenv(find_dotenv())


def run_agent_reasoning_engine(state: AgentState):
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}
