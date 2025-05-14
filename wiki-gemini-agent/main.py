from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from tool import wiki_tool
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a smart agent that uses Wikipedia to answer questions."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])


tools = [wiki_tool]

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

executor = AgentExecutor(agent=agent, tools=tools, varbose=True)

question = input("Ask somethinf: ")
responce = executor.invoke({"input":question})
print("\n📘 Answer:", responce)
