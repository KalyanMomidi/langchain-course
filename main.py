import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
 

# Load environment variables
load_dotenv()


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
         query: The query to search for 
    Returns:
        The search Result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model = llm, tools = tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content = "What is the weather in tokyo")})
    print(result)

 

if __name__ == "__main__":
    main()



