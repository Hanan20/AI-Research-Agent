# AI-Research-Agent
An intelligent AI-powered research assistant that automatically gathers, summarizes, and saves structured research data using multiple tools — including DuckDuckGo Search, Wikipedia, and a custom text-saving utility. Built with the LangChain framework and OpenAI’s GPT-4o model through OpenRouter.
<img width="1847" height="943" alt="Screenshot 2025-11-05 152345" src="https://github.com/user-attachments/assets/24741a7f-4a6c-46f2-a87e-14ff05b140ac" />
<img width="1839" height="424" alt="Screenshot 2025-11-05 152429" src="https://github.com/user-attachments/assets/779b4d77-acc8-45a0-981c-6fe97c79a405" />

🚀 Overview

This project is designed to act as a co-pilot for research tasks.
You can give it any query — for example, “Explain the impact of renewable energy on emerging economies” — and it will:

Search the web and Wikipedia for relevant information

Summarize findings in a structured format (topic, summary, sources, tools used)

Save the results to a local file with a timestamp

It provides an automated way to perform quick literature or web research without manually switching between multiple sources.

🧩 Features

🌍 Web & Wikipedia Search Integration using LangChain tools

🧾 Structured Output Parsing via PydanticOutputParser

💾 Auto-Save Research Outputs into timestamped .txt files

🧠 Agentic Workflow powered by LangChain’s create_tool_calling_agent

🔐 Environment Variable Management with .env for API keys

🧰 Extensible Tooling System — easily add more tools for custom data collection

🛠️ Tech Stack

Python 3.10+

LangChain

OpenAI GPT-4o via OpenRouter API

DuckDuckGo Search API

Wikipedia API

dotenv for secure API key management

pydantic for structured response validation


AI-Research-Agent/
│
├── main.py               # Main script that runs the agent
├── tools.py              # Custom tools: search, wiki, save_to_txt
├── research_output.txt   # Saved research results (auto-generated)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (contains API key)
└── screenshots/          # Example UI outputs (images)

⚙️ Setup Instructions

Clone the repository

git clone https://github.com/Hanan20/AI-Research-Agent.git
cd AI-Research-Agent


Install dependencies

pip install -r requirements.txt


Add your API key

Create a .env file in the project root.

Add your OpenAI / OpenRouter API key:

OPENAI_API_KEY=your_openrouter_api_key_here


Run the agent

python main.py


Provide a research query when prompted

What can I help you research?
> The economic effects of AI automation


The agent will generate structured research and automatically save it in research_output.txt.

🧠 Example Output
--- Research Output ---
Timestamp: 20251007_124343

Topic: Population of North America  
Summary: As of 2023, the population of North America is estimated to be over 600 million people...
Sources: [Wikipedia, DuckDuckGo]
Tools Used: ["Search", "WikipediaQueryRun", "SaveTool"]


💡 Future Improvements

Integrate Google Scholar API for academic sources

Add vector database (e.g., FAISS) for semantic retrieval

Build a Gradio or Streamlit interface

Enable multi-query batch research mode

🤝 Contributing

Feel free to fork the repository and submit pull requests!
You can also open an issue if you’d like to suggest new features or tool integrations.
