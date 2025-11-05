from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


# custom tool
def save_to_txt(data: str, filename: str = "reseach_output.txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

# if you want a tool that calls an api or does something more complex, you can do that , just write a python function and wrap as tool and you can pass as many of these to you agent as you want.


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web for relevant information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
