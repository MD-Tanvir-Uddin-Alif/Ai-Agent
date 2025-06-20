import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from tools import amazon_tool, daraz_tool, ebay_tool, aggregate_tool

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

tools = [amazon_tool, daraz_tool, ebay_tool, aggregate_tool]

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful online deal finder assistant. "
     "When the user gives a search query, do the following:\n"
     "1. Use all keywords given to search Amazon, Daraz, and eBay for deals. "
     "2. If the user specifies a price range or location, use it to filter results. "
     "3. If no price or location is given, just search with the keywords as is. "
     "4. Only ask for clarification if the input is empty or too vague to perform a search. "
     "5. Return a clear list of deals with title, price, rating, and link.\n"
     "Keep the response friendly and concise."
    ),
    ("user", "{input}"),
    ("ai", "{agent_scratchpad}")
])


agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
