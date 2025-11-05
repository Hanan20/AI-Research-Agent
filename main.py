from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool


load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: List[str]
    tools_used: List[str]


llm = ChatOpenAI(
    model="openai/gpt-4o",  # Must be a valid OpenRouter model ID
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",  # 👈 This is the missing piece!
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are a research assistant. that will help generate a reseach paper.
     Answer the user query and use necessary tools.
     Wrap the output in this format and provide no other text\n{format_instructions}
     """),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")


]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research?")
raw_response = agent_executor.invoke(
    {"query": query})

try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw response - ", raw_response)
