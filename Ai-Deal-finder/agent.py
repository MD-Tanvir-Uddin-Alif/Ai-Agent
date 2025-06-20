from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatMessagePromptTemplate
from dotenv import load_dotenv
from tools import amazon_tool, daraz_tool, ebay_tool, aggregate_tool
import os


llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

tools = [amazon_tool, daraz_tool, ebay_tool, aggregate_tool]

prompt = ChatMessagePromptTemplate.format_messages9([
    ("system", 
     "You are a smart online deal finder. Your job is to find the best deals from Amazon, Daraz, and eBay using available tools. "
     "Use the 'Aggregate Deal Finder' tool to get top 10 best-priced results. Respond with helpful and clear information."),
    ("user", "{input}")
])


agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)